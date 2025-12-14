x = 5.0
if (type(x)is not float):
 print("true")
else:
 print("false")

a = 5 
if (type(a)is int):
  print ("true")
else:
  print("false")

b = 20
c = 20
if (b is c):
  print ("b & c SAME identity")
c = 30 
if (b is not c ):
  print ("b & c have DIFFERENT identity")