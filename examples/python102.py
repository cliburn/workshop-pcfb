# get input and store in variable word
word = raw_input("Enter a word: ")
# check if word is the same when reversed
if word == word[::-1]:
    print "%s is a palindrome!" % word
else:
    print "%s is a regular old word" % word
