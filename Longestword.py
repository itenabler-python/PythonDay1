#read a file find longest word in text file
sentence = "The quick brown fox jumps over the laziest dog"

list1 = sentence.split(" ")
maxwordlength = 0

for word in list1:
    print(word)
    if len(word)>= maxwordlength:
        longestword = word
        maxwordlength = len(word)

print("Longest word is {} with word length {}".format(longestword, maxwordlength))

