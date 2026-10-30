a=float(input())
if a <=50:
  b=a*1
elif 51<=a<=150:
  b=50*1+(a-50)*2
elif 151<=a<=250:
  b=50*1+100*2+(a-150)*3
else:
  b=50*1+100*2+100*3+(a-250)*4
if b>150:
  b=b+b*0.20
if a.is_integer:
  print(int(b))
else:
  print(b)
  
