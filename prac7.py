while True:
    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        continue

    if name[0].isdigit():
        print("Name cannot start with a number.")
        continue

    break


while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Enter valid age!!")
        else:
          break
    except ValueError:
        print("Invalid input.")


if age >=18:
     print(f"Hey, {name}, you are eligible to vote!")
else:
     print(f"Hey, {name}, you are not eligible to vote!")


