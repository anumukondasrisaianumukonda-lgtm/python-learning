#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="sai"
    maild="saianumu@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''    


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="sai",mailid="sai@gmail.com")
    
def Details(id,name,mailid):
    print(id,name,mailid)
Details(20,"sai","sai@gmail.com")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details("sai@gmail.com",50,"sai")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(mailid="sai@gmail.com",id=25,name="sai")'''    


'''def details(id,name,mailid):
    print(id,name,mailid)
details(id=20,name="sai",mailid="sai@gmail.com")'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %f" %price)
grocery("rice",1000)'''    


'''def grocery(item="sugar",price=1000):
    print("item is %s" %item)
    print("price is %f" %price)
grocery()'''    


'''def grocery(item,price=300):
    print("item is %s" %item)
    print("price is %f" %price)
grocery("dhal")'''    

'''def grocery(item="ghee",price):
    #non def arg follows def arg   
    print("item is %s" %item)
    print("price is %f" %price)
grocery(1000)'''


'''def bakery(cake_name,price,quantity):
    print("cake_name is %s" %cake-name)
    print("price is %f" %price)
    print("quantity is %f" %quantity)
bakery("redvelevetcake",500,25)

def bakery(cake_name="choclate",price=500,quantity=2):
    print("cake_name is %s" %cake_name)
    print("price is %f" %price)
    print("quantity is %f" %quantity)
bakery()   


def bakery(cake_name,price,quantity=2):
    print("cake_name is %s" %cake_name)
    print("price is %f" %price)
    print("quantity is %f" %quantity)
bakery("blackforest",600)   

def bakery(cake_name="pineapple",price=500,quantity):
    print("cake_name is %s" %cake-name)
    print("price is %f" %price)
    print("quantity is %f" %quantity)
bakery(2)'''

# * star arguments(* is used to unpack the elemnts)
'''a=[1,2,3,4,5]
print(a)
print(*a)'''

'''a=(1,2,3,4,5)
print(a)
print(*a)'''

'''a={1,2,3,4,5}
print(a)
print(*a)'''

'''d={"name":"sai","year":2008,"month":2}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''#error

'''a,b,c=3,4,5
print(a)
print(b)
print(c)'''


'''a,b,*c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''

#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7]
check(*b)
c={2,3,4,5,6}
check(*c)
d={"year":2026,"month":7}
check(*d)'''

'''def check1(*a):
    d=13#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,2.5,3.5)
check1(2,3,4.2,5.2,"sai")'''#error


'''def check(*a):
    d=5 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check(2,3,4,5.6,"sai")'''            
    

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["sai","eswar","pooja"],"marks":[10,20,30],"status":["p","a","p"]}
details(**d)'''
        
'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["sai","eswar","pooja"],"marks":[10,20,30],"status":["p","a","p"]}
details(**d)'''


'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,4.5)
final(*data)
d={"names":["sai","eswar","pooja"],"marks":[10,20,30],"status":["p","a","p"]}
final(**d)
final(*data,**d)'''

#railwayticket
'''def ticket(age,gender,price):
    if age>60:
        if gender=="male":
            d_price=price*0.7
        else:
            d_price=price*0.5
    else:
        if gender=="male":
            d_price=price
        else:
            d_price=price*0.7
    return d_price
age=int(input("age"))
gender=input("male or female")
price=int(input("price"))
print(ticket(age,gender.lower(),price))'''

        


        

