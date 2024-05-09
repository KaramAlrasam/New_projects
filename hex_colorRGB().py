def convertHEX_into_Tuple(str1:str):
  a=int(str1[1:3],16)
  b=int(str1[3:5],16)
  c=int(str1[5:7],16)
  return (a, b, c)
print("#FF6347")
print(convertHEX_into_Tuple("#FF6347"))
# and oppist
def convert_tuple_into_hex_color(m_tuple:tuple):
  
  return("#"+"".join(f"{num:02x}"for num in m_tuple))
print(convert_tuple_into_hex_color(convertHEX_into_Tuple("#FF6347")))