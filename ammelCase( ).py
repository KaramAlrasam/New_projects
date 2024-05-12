
# def cammlCase(str1:str):
#   #use stip fuction to get rid of spaces or charcters
#   #use split function to make list
#   m_list=m_split(m_strip(str1))
#   #make for loop on the list
#   return m_list[0].lower()+"".join(item.capitalize() for item in m_list[1:])
#   #use capitalize to each word
#   #make condition to spicify the possion of (_,-," ")
# def m_strip(str1:str):
#   start_p=0
#   end_p=len(str1)-1
#   while not str1[start_p].isalpha():
#     start_p+=1
#   while not str1[end_p].isalpha():
#     end_p-=1
#   return str1[start_p:end_p+1]
# def m_split(str1:str):
#   m_list=[]
#   start_p=0
#   for i in range(len(str1)):
#     if not str1[i].isalpha():
#       m_list.append(str1[start_p:i])
#       start_p=i+1
#   m_list.append(str1[start_p:])
#   return m_list
# # print(m_split("foo.bar"))
# print(cammlCase("     ,/-karam alrasam     ><"))
# print(cammlCase("JavaScript"))
# print(cammlCase("Foo-Bar"))
# print(cammlCase("foo_bar"))
# print(cammlCase("--foo.bar"))
# print(cammlCase("Foo-BAR"))
# print(cammlCase('fooBAR'))
# print(cammlCase('foo bar'))
# Import the 'sub' function from the 're' module for regular expression substitution
from re import sub

# Define a function to convert a string to camel case
def camel_case(s):
  #use sub fuction to replace any(_,-) with space
  #after that use title funtion and replace function with 
  s=sub(pattern="(_|-)+",repl=" ",string=s).title().replace(" ","")
  #convert first chr with lowercase and conctenate it with the stratech of string
  return s[0].lower()+s[1:]

# Test the function with different input strings and print the results
# print(camel_case('JavaScript'))
# print(camel_case('Foo-Bar'))
print(camel_case('foo_bar'))
# print(camel_case('--foo.bar'))
# print(camel_case('Foo-BAR'))
# print(camel_case('fooBAR'))
# print(camel_case('foo bar')) 
