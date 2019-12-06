# Output the quadrant number (1, 2, 3 or 4) for the point (x,y).

x = input()
y = input()

if int(x)>=0 and int(y)>=0:
  print("1")
elif int(x)>=0 and int(y)<=0:
  print("4")
elif int(x)<=0 and int(y)>=0:
  print("2")
else:
  print("3")
