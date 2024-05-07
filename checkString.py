def test(str1:str):
  dic={"Not_Upper":"You must add ltters of upper case",
      "Not_Lower":"You must add ltters of lower case",
       "Not_digit":"You must add numbers",
       "Not_Long":"You must make it longer than 8" 
      }
  if not any((l.islower() for l in str1)):
    return dic["Not_Lower"]
  if not any((l.isupper() for l in str1)):
    return dic["Not_Upper"]
  if not any((l.isdigit() for l in str1)):
    return dic["Not_digit"]
  if len(str1)<8:
    return dic["Not_Long"]
  return "'Valid string.'"
print(test("KARAMALRASAM2"))
