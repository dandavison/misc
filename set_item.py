from itertools import chain, repeat
import sys
import types

# byte offsets for structures
if hasattr(sys, 'gettotalrefcount'):
    # under PyDEBUG builds
    _f_localsplus_offset = 392
    _ob_item_offset = 40
else:
    # under normal builds
    _f_localsplus_offset = 376
    _ob_item_offset = 24


def tuple_setitem(t, ix, value):
    """``setitem`` for tuples.

    Parameters
    ----------
    t : tuple
        The tuple to assign into.
    ix : int
        The index to assign to (without bounds checking).
    value : any
        The value to store at index ``ix``.
    """
    # the maximum allowed offset from the address of the frame's locals
    # to the target address measured in pointer counts.
    range_ = 2 ** 16

    # create python code that emits one branch per value in range of:
    #
    #     if this_branch():
    #         _n = None
    #
    # where ``this_branch`` is a callable that checks if we should assign to
    # the given index. None will be replaced with ``value``.
    python_template = (
        'def f():\n    this_branch = (yield None)\n    ' +
        '\n    '.join(
            f'if this_branch():\n        _{n} = None' for n in range(range_)
        )
    )
    code_template = compile(python_template, '', 'exec').co_consts[0]

    # the target address is the id of the tuple + the offset of the first
    # element + the index * the size of a pointer
    target_address = id(t) + _ob_item_offset + ix * 8

    # collection of frames to prevent deallocation
    frames = []
    while True:
        # spray the heap with generators looking for a location where the
        # frame's local variables are  withing ``range_ * 8`` bytes of the
        # target address
        code = types.CodeType(
            0,
            0,
            1,
            1,
            99,
            code_template.co_code,
            (value,),  # make co_consts[0] ``value`` to replace None
            (),
            ('this_branch',),
            '<string>',
            '<tuple-set-helper>',
            1,
            b'',
        )
        generator = types.FunctionType(code, {})()

        locals_address = id(generator.gi_frame) + _f_localsplus_offset

        offset_bytes = target_address - locals_address
        # subtract 1 because 'this_branch' is local variable 0
        offset_index = offset_bytes // 8 - 1
        if offset_index < range_:
            # we found a frame that is close enough to the target address;
            # clear the saved frames and continue
            frames.clear()
            break
        else:
            # this frame isn't close enough; save it in memory so we don't try
            # here again
            frames.append(generator.gi_frame)

    # make sure we set None to ``value`` and prime the generator
    assert next(generator) is value, 'yielded the wrong value'

    # the branch selector is a function which returns False ``offset_index``
    # times then True, then raises ``StopIteration``.
    branch_selector = chain(repeat(False, offset_index), [True]).__next__
    try:
        # send the selector into the generator; this gets bound as
        # ``this_branch``
        generator.send(branch_selector)
    except StopIteration:
        # the branch after ``branch_selector`` returns True will raise a
        # ``StopIteration``
        pass

t = (0, 1)
tuple_setitem(t, 0, 99)
print(t)
