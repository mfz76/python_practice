#check whether string contains any uppercase letter or not


while True:
    try:
        x = input("Enter the word:").strip()
        break
    except Exception:
        print("something is wrong!")

Noupper = True

for ch in x:
    if   "A" <= ch  <= "Z":
        Noupper = False
        break

if Noupper:
    print("there is no any uppercase letter.")
else:
    print("there is an uppercase letter.")
    




