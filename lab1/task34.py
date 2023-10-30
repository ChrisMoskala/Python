import os


def deleteWords(words):
    with open(os.path.abspath("text.txt"), "r") as file:
        for line in file:
            print("old line:\n" + line)
            for i in words:
                line = line.replace(i, "")
            print("new line:\n" + line)
    file.close()


def replaceWords(words, words2):
    with open(os.path.abspath("text.txt"), "r") as file:
        for line in file:
            print("old line:\n" + line)
            j = 0
            for i in words:
                line = line.replace(i, words2[j])
                j = j + 1
            print("new line:\n" + line)
    file.close()


words = ["lama"]
words2 = ["bruh"]

print("delete or replace ?")
user = input()
if user == "delete":
    deleteWords(words)
elif user == "replace":
    replaceWords(words, words2)
