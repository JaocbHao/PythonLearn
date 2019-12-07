# The input consists of two lines. The first line is the “aaah” Jon Marius is able to say that day. The second line is the “aah” the doctor wants to hear. Only lowercase ’a’ and ’h’ will be used in the input, and each line will contain between 0 and 999 ’a’s, inclusive, followed by a single ’h’
a = input()
b = input()
x = len(a)
y = len(b)

#print(x)
#print(y)
if x < y:
  print("no")
else:
  print("go")
