#make function has one string paramter
def move_space(str1:str):
  #count whole spaces in the string
  num=str1.count(" ")
  #make empty variable to save a new string
  result=""
  #conctnate whole letters without spaces
  for l in str1:
    if l !=" ":
      result+=l
  return " "*num+result

print(move_space("          karam        alrasam        "))
def move_space2(str1:str):
  #make list comprehantion without spaces
  chr_w=[l for l in str1 if l != " "]
  #make aquation to get the length of spaces
  space=len(str1)-len(chr_w)
  #return ch_w and conctemate it with space
  return " "*space+"".join(chr_w)

print(move_space2("          karam        alrasam        "))