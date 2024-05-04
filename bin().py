#take int input from the use
N=int(input("N= ").strip())
#use bin function to convert int number
print("Binary= ",bin(N))

print("="*20)
################
def m_bin(int1:int):
  #Thus variable will save the result of binary
  result=0
  #this list for reminders of int1
  m_l=[]
  #to make condition to while we made varible same value of int1
  num=int1
  while num!=0:
    #we made variable to save the remiander of num
    r=num%2
    #and append the result in m_l
    
    m_l.append(r)
    #use floor division until to make it 0
    num//=2
  print(m_l)
  #make loop on length of m_l 
  for i in range(len(m_l)):
    #make this formila 
    #(m_l[0]=1,m_l[1]=1,m_l[2]=0, m_l[3]=1,m_l[4]=1)*10^(i=0,i=1,i=2,i=3,i=4, i=5, i=6)
    result+=m_l[i]*10**i
    
    
  return result
print(m_bin(27))
print("="*20)
def m_bin1(int1:int):
  i=res=0
  while int1!=0:
    res+=(int1%2)*10**i
    int1//=2
    i+=1
  return "0b"+str(res)
print(m_bin1(27))