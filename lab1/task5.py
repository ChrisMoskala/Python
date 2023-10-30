import re

print("please enter the text")
text = input()
print("please enter the word to look for")
lookout = input()
print("Delete or replace?")
choice = input()
if choice == "delete":
    print(re.sub(lookout, "", text))
elif choice == "replace":
    print("Type the word to replace into")
    uganda = input()
    print(re.sub(lookout, uganda, text))
