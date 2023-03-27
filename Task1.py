def oops():
    # raise IndexError
    raise KeyError

def test():
    try:
        oops()
        print('YES')
    except IndexError:
        print('NO')

test()
# An error occurs if oops() is changed