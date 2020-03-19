__author__ = 'Ken Tan'
"""
this program is counting
the number of 
words for you
"""
user_input = input("Please enter the path and the name of the text file you want to anaylze."   
                   "\n (Eg. c:/users/monty/desktop/file.txt):" 
                   "\n")

# sending user's input back to them, for now
print(user_input)

common_word = input("would you like to strip common words from the results (y/n)")
print(common_word)

user_output = input("\nwould you like to output these results to a file(y/n) ")
print(user_output)

if (common_word == "y"):
    print("You have chosen yes")
else:
    print("You have chosen no")


