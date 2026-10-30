sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
total=sub1+sub2+sub3+sub4+sub5
average=total/5 
if average.is_integer():
  print(int(average))
else:
  print(f"{average:.2f}")
