from collections import Counter
def remove_duplicate_words(str1:str):
  #use split function to make them as list
  m_list=Counter(str1.split(" "))
  return " ".join(m_list)
print(remove_duplicate_words("Python Exercises Practice Solution Exercises"))
#Python Exercises Practice Solution  
def remove_duplicate_words2(str1:str):
  l=str1.split(" ")
  res=[   ]
  for w in l:
    if w not in res:
      res.append(w)
  return "".join(res)
print(remove_duplicate_words("Python Exercises Practice Solution Exercises"))