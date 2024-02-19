word = input("Please enter your name: ")
first =word[0]
rest = word[1:len(word)]
print(f"you word is:{rest}")
if first in {"a","e","i","o","u"}:
     w=rest + first + "way"
     print(w.lower())
else: 
     w1=rest+ first + "ay"
     print(w1.lower())