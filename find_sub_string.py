
# make function has one string paramter
def test(str1:str):
  if len(str1)<2:
    return str1
  #make empty string variable 
  start_p=0
  end_p=len(str1)-1
  while str1[start_p]in str1[start_p+1:]:
    start_p+=1
  while str1[end_p]in (str1[start_p:end_p]):
    
    end_p-=1
  return str1[start_p:end_p+1]
word="asdaewsqgtwwsa"
print(test(word))#daewsqgt
