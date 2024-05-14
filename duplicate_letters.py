#import collection and use its method counter
from collections import Counter
#make function has one string paramter
def duplicate_letters1(str1:str):
#use split function to make list of words
  m_list=str1.split(" ")
# use for loop with condition to discove which word has duplicate letter
  for item in m_list:
    dic=Counter(item)
    for l in dic:
      if dic[l]>1:
        return False
# use del to drain the content of Counter
    # dic={}
  return True
print(duplicate_letters1("The wait is over."))
#####################
print("="*30)
def duplicate_letters(str1:str):
  m_list=str1.split(" ")
  for w in m_list:
    if len(w)>len(set(w)):
      return False
  return True
  
print(duplicate_letters("The wait is over."))
print(duplicate_letters("Python Exercise."))
