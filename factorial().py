N=int(input("Enter number: ").strip())
result=2
if N>2:
  for i in range(3,N+1):
    
    result*=(i)
print("result= ",result)
print("="*20)
##############
#take input from the user integer
Num=int(input("N= ").strip())
#make variable its value = 1 .
i=1
#make another variable its value same value of num from the user
result=Num#=5
#make condition if the Num < from 2 return 1
if Num==0:
  result=1
else:
  #make while loop and make its condition as this
  #4<(5-1)==False
  while i<Num-1:
    result*=(Num-i)#5*(5-1)=20*(5-2)=60*(5-3)=120
    i+=1

print("Result= ",result)