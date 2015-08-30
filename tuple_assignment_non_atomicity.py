x = ([0],)

print x
try:
    x[0] += [1]
except Exception as ex:
    print ex
    print 'there was an error; doing nothing'
print x
