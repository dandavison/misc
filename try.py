try:
    a = 1/0
except:
    import ipdb ; ipdb.set_trace()
else:
    print a
