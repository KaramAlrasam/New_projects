#make function has one int paramter
def m_bin(num:int):
  #make varible has zero value
  i=res=0
  #make while loop and let its condition num
  while num!=0:
    #use fomila for getting binary number
    res+=(num%2)*10**i
    i+=1
    num//=2
  return "0b"+str(res)

#################

 
##################
def m_octal(num:int):
  #make empty list
  octal=[]
  #make while loop on the num and make its condition it's until becaume zero
  while num!=0:
    octal+=[str(num%8)]
    num//=8
  octal.reverse()
  return "".join(octal)
##################
def m_hexadecimal(num):
  #make dictionary has keys from 1 to 16
  dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
  #make empty list to save the reminders hexadecimal numbers
  hexadecimal=[]
  #make while loop and let its condtion num !=0
  while num!=0:
    #make variable and let its value the remiander of num
    remiander=num%16
    #make condition  for the remiander
    if remiander>9:
      hexadecimal.append(dic[remiander])
    else:
      hexadecimal.append(str(remiander))
    #complete the condition to stop the loop
    num//=16
  #use reverse method to reverse the  the content of the list
  hexadecimal.reverse()
  #return the content of list and merge them all togather by using join()function
  return "".join(hexadecimal)
print(25," ",m_octal(25)," ",m_hexadecimal(25)," ",m_bin(25))

print("="*20)
print(int(m_bin(25),2))