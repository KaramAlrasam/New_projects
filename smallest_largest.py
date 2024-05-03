#make function has one string paramter
def smallest_largest(str1:str):
  #use split function to make it as list
  m_list=str1.split(" ")
  #usr sorted function to orgnize its items
  m_sorted=sorted(m_list,key=len)
  return (m_sorted[0], m_sorted[-1])

print(smallest_largest("Write a Java program to sort an array of given integers using Quick sort Algorithm."))