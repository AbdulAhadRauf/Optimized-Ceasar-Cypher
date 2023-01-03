from replit import clear
import string
l=list(string.ascii_lowercase)

def Cypher(w,s,d):
  code=''
  if d=="decode":
    s *= -1
  for i in w:
    if i in l:
      newpos=(l.index(i)+s)%26
      code+= l[newpos]
    else:
      code+=i
  print(f"the {d}d code is {code}")

go='Y'
while "Y" in go:
  clear()
  word = input("Enter The Word ").lower()
  shift = int(input("Enter the shift "))
  Typeofenc = input("Encode or Decode ").lower()
  if Typeofenc=="encode" or Typeofenc=="decode":
    Cypher(w=word, s=shift,d= Typeofenc)
  else:
    print("Please enter encrypt or decrypt ")
  go = input('Do you want to go again?').upper()
print("\nBye. Have a Great Time")