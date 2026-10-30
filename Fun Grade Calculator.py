sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
total=sub1+sub2+sub3+sub4+sub5
average=total/5 
if 0<= average<=100:
  if average >=90:
    print("Excellent!")
  elif average <90 and average >= 80:
    print("Great Job!")
  elif average <80 and average >=70:
    print("Good Effort!")
  elif average <70 and average>=50:
    print("Keep Trying!")
  else:
    print("Better Luck Next Time!")
