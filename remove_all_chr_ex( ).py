
word="karam alrasam"
# Function to remove all chars except given char
def remove_all_chr_ex(str1:str,s:str):
  #make list comperhention with condition to get only chr which is existent in
  #str1 and then make hoin to it
  return "".join([l for l in str1 if l==s])
print(remove_all_chr_ex(word,"")) 
