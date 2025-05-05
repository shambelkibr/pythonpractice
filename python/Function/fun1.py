def arthematicoprate( x,y):
    return x+y
# print( "the sum of two",arthematicoprate(2,4))


'''the using parametr default value for argument '''
def grettingname(name="world"):
    print("hello :",name)
    
# grettingname("shambel")
# grettingname()

def print_args(*args):
    for i in args:
        print(i,end=" ")
print_args(1,2,3,4,5)


def printargas(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value} ')
printargas(a=2,b=3,c=4)