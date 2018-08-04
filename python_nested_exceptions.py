try:
    raise Exception('1')
except:
    try:
        raise Exception('2')
    except:
        raise
finally:
    print 'hello'
