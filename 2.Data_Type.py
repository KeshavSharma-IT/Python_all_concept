
# veriables
# x=5
# z=5.5
# p=x+z
# print(p)
# print(x)
# y="keshav"
# print(y)

#DATA TYPES python is dynamic type means u not need to define any veriable

#1.Numbers
# x=12
#
# print(type(x))
# print(type(p))
# m=12
# print(type(m))
# m=float(12)
# print(type(m))
#2.String

# a="k"
# b="keshav"
# c='keshav2'
# d='''hi this is
# multible line
# function'''
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(a)
# print(b)
# print(c)
# print(d)

#method in string
# w="water"
# k="keshav sharma"
# print(w.upper())
# print(w.title())
# print(k.split())
# print(k.count('s'))
# print(k.find('a'))
# print(k.endswith('a'))

# indexing
# x="keshav"
# print(x[1])
# print(x[-1])
# print(x.replace('e','a'))
# print(x)
#split

# y="hello keshav"
# print(y[0:5])
# print(y[6:])
# print(y[:5])

#formating

# x="my"
# y="name"
# z="is"
# w="keshav"
# o=23
# p=x+" "+y+" "+z+" "+w
# print(p)
#
# print(f"{x} {y} {z} {w}".format(x,y,z,w))
# print(f"AGE of {w} is {o}".format(w,o))

#list-changeable. Allows duplicate members.
# x=["red","blue","green","white"]
# print(x)
# print(type(x))
# print(x[1])
# print(x[-1])
# print(x[1:3])
# print(len(x))
# print(x.pop())
# print(x.append("yellow"))
# print(x)
# print(x.remove("yellow"))
# print(x)
# del x
# print(x)

#tuple- unchangeable. Allows duplicate members.

# x=("red","blue","green","white")
# print(x)
# print(type(x))
# print(x[1])
# print(x[-1])
# print(x[1:3])
# print(len(x))
# #   cannnot use this print(x.pop())
# # cannnot use this print(x.append("yellow"))
# print(x)
# cannnot use this print(x.remove("yellow"))


# dictonary- key :value,changeable. No duplicate members.
# x={"number":1,
#    "name":"blue"
#    ,"age":20}
# print(x["name"])
#
# x["age"]=55
# print(x["age"])
# print(len(x))
# x["year"]=1990 #add
# print(x)
# print(x.pop("age"))
# print(x)
# print(x.popitem())
# print(x)

#set  unordered, unchangeable, and do not allow duplicate values.

# x={1,2,3,4,4}
# print(x) #it will not print 4 twice rest is same

# 3.Boolean
print(4>5)
print(1<0)
