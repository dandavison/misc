def gen():
    # None received, causing it to execute until first yield
    print("line 1")
    x = yield "doesnt matter!"  # <--- never gets emitted
    # print(received1)
    print("line 2")
    # received2 = yield 2  # <-- this is the first value emitted by the corotuine!
    # print(received2)
    return "result"


g = gen()

print("--- g.send(None)")
print(g.send(None))

print("--- g.send(None)")
print(g.send(None))
# print("--- print(next(g))")
# print(next(g))

# print("--- print(next(g))")
# print(next(g))
# print(g.send(77), "888")


# print(next(g))
# print(next(g))
# try:
#     print(next(g))
# except Exception as si:
#     print(si.value)
