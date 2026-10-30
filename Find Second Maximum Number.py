a=int(input())
b=int(input())
c=int(input())
if (a>b or a>c) and (b>a or c>a):
  print(a)
elif (b>a or b>c) and (a>b or c>b):
  print(b)
elif (c>a or c>b) and (b>c or a>c):
  print(c)
else:
  print("No second max")
