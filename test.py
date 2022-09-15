
#Decorators

def div(a,b):
    print(a/b)


def div_smart(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


div1 = div_smart(div)
div1(2,4)
