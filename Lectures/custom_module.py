# We can have variable definitions 
x = 10

# We can have functions as well
def welcome(who,what='Python'):
    x='Good morning '+who+', Welcome to a class on '+what
    print(x)

def ToH(n,source,dest,inter):           
    if n == 1:
        print(n,'from',source,'to',dest)
        return
    ToH(n-1, source,inter,dest)
    print(n,'from',source,'to',dest)
    ToH(n-1,inter,dest,source)

def scope_check():
    print(x)

# I'm here to mess up your code 3:)
def sum():
    pass

## This function would be added later
# def later_added():
#     print('I was added at a later time')

# print('Oh No!')
