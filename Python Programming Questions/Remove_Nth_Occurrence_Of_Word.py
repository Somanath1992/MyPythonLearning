# Remove the Nth occurrence of word from list
myList = ["geeks", "for", "geeks"]
word = "geeks"
n = 2
count = 0
for i in range(0, len(myList)):
    if myList[i] == word:
        count = count + 1
        if count == n:
            del myList[i]

print("Updated List:", myList)
