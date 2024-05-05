import time
start=time.time()
def FindIndex_sub(str1:str,str2:str):
  
  #make condtion for the string 2 
  if str2 not in str1:
    return "Not Found"
  else:#karam salrasam #sub=sam
    for i in range(len(str1)):
      if str1[i]==str2[0]:
        for x in range(1,len(str2)):
          if str2[x]==str1[i+x]:
            ...
            if x==len(str2)-1 and str2[x]==str1[i+x]:
              return i
          else:
            break
print(time.time()-start)
print(test("Python Exercises ","Ex"))
print("="*20)
#################
start=time.time()

# Function to find index of substring
def find_Index(str1, pos):
  # Check if pos longer than str1
  if len(pos) > len(str1):
    return 'Not found'
  # Iterate through str1
  for i in range(len(str1)):
    # Iterate through pos
    for j in range(len(pos)):
      # If match found, return index
      if str1[i + j] == pos[j] and j == len(pos) - 1:
        return i
      # Break if mismatch
      elif str1[i + j] != pos[j]:
        break
  return 'Not found'
# Test cases
print(time.time()-start)
print(find_Index("Python Exercises", "Ex"))
# print(find_Index("Python Exercises", "yt"))
# print(find_Index("Python Exercises", "PY"))
