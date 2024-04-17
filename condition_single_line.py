########## as usual ###########
x = 10
if x%2 == 0:
  print("Even")
else:
  print("Odd")

######### shortcut ########
x = 10
print("Even") if x%2 == 0 else print("Odd")


########## as usual ###########

x = 10
if x > 5:
  print("greater than 5")
elif x==5:
  print("equal to 5")
else:
  print("less than 5")

######### shortcut ########

x=4
print("greater than 5") if x > 5 else  print("equal to 5") if x==5 else print("less than 5")
