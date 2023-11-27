
weight= input("whats your weight? ")
c= input("K(kg)or L(lbz)? ")
x = float(weight)

if (c.upper()=="K"):
    print(x+"kgs")
elif (c.upper()=="L"):
    print((x*2.2)+"kgs")
else:
    print("please enter valid units")







# age= input("whats your age? ")
# x = int(age)

# if (x>0 and x<=19):
#     print("teens")
# elif (x>19 and x<=35):
#     print("adulthood")
# elif (x>35 and x<=65):
#     print("adult".upper())
# elif (x>65):
#     print("senior")

