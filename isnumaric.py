
print("\nAnother way:\n")
############
# Define a function to add two numbers represented as strings
def test(n1, n2):
  if (n1.isnumeric())and (n2.isnumeric()):
    return int(n1)+int(n2)
  else:
    return "Error in input!"
print(test("10", "\u0030"))
print(test("10", "10km2"))
print(test("100", "-200")) 
print(test("100", "2.4")) 

##############

def m_isnumeric(s:str):
  for item in s:
    if not item.isdigit():
       return False
  return True

# Test cases
print("="*20)
print("\nimplementation for isnumeric():\n")

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"
print(m_isnumeric(a))#True
print(m_isnumeric(b))#True
print(m_isnumeric(c))#False
print(m_isnumeric(d))#False
print(m_isnumeric(e))#False


