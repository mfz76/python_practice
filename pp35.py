# to check whether the string are anagrams of each other or not

x = input("Enter the string:").strip()
y = input("Enter the string:").strip()



if sorted(x) == sorted(y):
     print("its a anagram")
else:
     print("its not a anagram.")
        
