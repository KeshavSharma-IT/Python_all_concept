# there are mainly two loops
# 1.for
# 2.while

# 1. FOR Loop

# x=[1,2,3,4,5,6,7,8,9,10]
# print(x[0])
# print(x[1])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])
# print(x[7])
# print(x[8])
# print(x[9])

# the above method is very long so we use loops here
# for item in x:
#     print(item)
# Loop save our time and memory


# y=["red","green","yellow","pink","white"]
# for ele in y:
#     print(ele)

# x=[0,1,2,3,4,5,6,7,8]
# for i in x:
#     x[i]=input("enter your name")
# print(x)

# 2.While loop
# i=0
# while i<6:
#     print(i)
#     i+=1

# x="keshav"
# for i in x:
#     print(i)

# Direct use of string
# for i in "pawan":
#     print(i)

# Break statement
# x=["red","blue","green","yellow","white"]

# for i in x:
#     if i=="yellow":
#         break
#     print(i)
#
# x=[1,2,3,4,5,6,7,8,9]
# for i in x:
#     if i==6:
#         break
#     print(i)

# continue statement

# x=["red","blue","green","black","yellow","white"]
# for i in x:
#     if i=="black":
#         continue
#     print(i)

# x=[1,2,3,4,5,6,7,8,9]
#
# for i in x:
#     if i==5:
#         continue
#     print(i)

# range function  (start,end,gap or stap size)

# for x in range(10):
#     print(x)

# for x in range(4,10):
#     print(x)



# for x in range(4,100,4):
#     print(x)


# use of else in loop
# for x in range(10):
#     print(x)
# else:
#     print("loop completed")

#  nested loop
x=["big","small","bold","light","heavy"]
y=["iron","gold","silver","platinum","diamond"]
for i in x:
    for j in y:
        print(i,j)
