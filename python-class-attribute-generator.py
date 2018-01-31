#!/usr/bin/env python3

a = 1
class X:
    a = 2
    def f():
        return a + 1
    b = f()
print(X().b)




# # a = [1]
# # b = list(i for i in a)
# # print(b)


# # a = [1]
# # b = list(i for i in [2] if i not in a)
# # print(b)


# #!/usr/bin/env python3

# A generator does work as expected in a class definition:
# ```
# class X:  # (object):
#     a = [1]
#     b = list(i for i in a)
# print(X().b)
# # [1] in py2 and py3
# ```

# But this does not work!
# ```
# class X:  #(object):
#     a = [1]
#     b = list(i for i in [2] if i not in a)
# print(X().b)
# # py2: NameError: global name 'a' is not defined
# # py3: NameError: name 'a' is not defined
# ```


# Using a list comprehension works in python2. But it looks like python3
# implements the list comprehension in the same way as the generator comp.
# ```
# class X:  # (object):
#     a = [1]
#     b = list([i for i in [2] if i not in a])
# print(X().b)
# # py2: [2]
# # py3: NameError: name 'a' is not defined
# ```
