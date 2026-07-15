'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def caluclate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
caluclate(10,20)
caluclate(100,200)
caluclate(1000,2000)'''


'''def caluclate(a,b):
    print("the power is",a**b)
    print("the modulus is",a%b)
    print("the division is",a//b)
caluclate(10,20)
caluclate(10,5)'''


'''def add(a,b):
    print(a+b)
add(4,6)'''

'''while True:
        def add():
            a = int(input("a value"))
            b = int(input("b value"))
            print(a+b)
        add()'''


'''def add():
    a= int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname = input("first name")
    lname = input("last name")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(4,3)'''    

'''def mul(a,b):
    return a*b
print(mul(7,3))'''


#print vs return

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,5)'''    

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    return(d)
    #return(e)
print(cal(4,3))'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return(c,d,e)
print(cal(4,3))'''


#splibill
'''def splitbill():
    a=int(input("enter total members"))
    b=int(input("enter amount"))
    print(b//a)
splitbill()'''

def splitbill():
    '''a = int(input("enter members"))
    b = int(input("enter amount"))
    c=b//a
    print("per head is {}".format(c))
    print(f"perhead is {c}")
splitbill()'''

'''def splitbill():
    a = int(input("enter members"))
    b = int(input("enter amount"))
    print("per head is {}".format(b//a))
    print(f"perhead is {b//a}")
splitbill()'''


'''def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
a=10
b=20
print("1.Add")
print("2.Subtract")
print("3.Multiply")
choice = int(input("enter your choice"))
if choice == 1:
    print("addition is",add(a,b))
elif choice == 2:
    print("subtraction is",subtract(a,b))
elif choice == 3:
    print("multiplication is",multiply(a,b))
else:
    print("invalid choice")'''




