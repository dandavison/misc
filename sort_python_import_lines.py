#!/usr/bin/env python

def sort_import_lines(text):
    def is_import(line):
        return line.startswith('import') or line.startswith('from')

    def is_blank(line):
        return not line.strip()

    def is_comment(line):
        return line.lstrip().startswith('#')

    def is_single_line_docstring(line):
        return line.startswith('"""') and line.endswith('"""')

    def is_triplequote(line):
        return line.strip() == '"""'

    def is_code(line):
        return not (is_import(line) or
                    is_comment(line) or
                    is_blank(line))

    lines = text.splitlines(True)
    if not lines:
        return None

    header_lines = []

    # TODO: comment / shebang before docstring

    # Skip initial docstring
    if is_single_line_docstring(lines[0]):
        header_lines.append(lines.pop(0))
    elif is_triplequote(lines[0]):
        header_lines.append(lines.pop(0))
        while True:
            line = lines.pop(0)
            header_lines.append(line)
            if is_triplequote(line):
                break

    block = []
    changed = False
    while lines:
        line = lines.pop(0)

        if block:
            if not is_import(line):
                # Exit a block
                sorted_block = sorted(block)
                if sorted_block != block:
                    changed = True
                header_lines.extend(sorted_block)
                header_lines.append(line)
                block = []
            else:
                # Continue a block
                block.append(line)
        else:
            if is_import(line):
                # Enter a block
                block = [line]
            elif not is_code(line):
                # Continue a non-block
                header_lines.append(line)

        if is_code(line):
            lines = [line] + lines
            break

    if changed:
        return ''.join(header_lines + lines)
    else:
        return None


def process_file(path):
    with open(path) as fp:
        text = fp.read()

    altered_text = sort_import_lines(text)
    if altered_text:
        with open(path, 'w') as fp:
            fp.write(altered_text)


if __name__ == '__main__':
    import sys
    for path in sys.argv[1:]:
        process_file(path)
