def to_string(*args, sep=' ', end='\n'):
    return sep.join([str(i) for i in args]) + end


print(to_string(1, 2, 3))

