#to check whether a word conatins a vowel

while True:
    try:
       x = input("Enter the word:").strip().lower()
       break
    except Exception:
        print("something is wrong!")

novowel = True

for ch in x:
    if ch in "aeiou":
        novowel = False
        
if novowel:
    print("there is not any vowel present in the word.")

else:
    print("there is vowel present in the word.")
