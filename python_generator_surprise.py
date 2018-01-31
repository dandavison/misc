#!/usr/bin/env python3


def helper_function_that_happens_to_involve_generator(a):
    val = next(a + i for i in [0] if i > 0)
    return val


def i_didnt_expect_this_to_return_a_list_of_length_0():
    return list(helper_function_that_happens_to_involve_generator(i)
                for i in [1, 2, 3])


print(i_didnt_expect_this_to_return_a_list_of_length_0())
