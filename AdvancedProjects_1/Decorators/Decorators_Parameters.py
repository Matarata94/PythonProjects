def Params(oldFunc):
    def inside(*args, **kwargs):
        print('Params: ', args, kwargs)
        return oldFunc(*args, **kwargs)
    return inside

@Params
def Mult(x, y=10):
    print(x*y)

Mult(4, 4)
Mult(3)
Mult(x=1, y=3)