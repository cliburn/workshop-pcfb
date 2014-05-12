"""Count the number of vowels in a name."""

# input data and store in variable name
name = raw_input("What's your name? ")
# store count of vowels in variable num_vowels
num_vowels = 0
# repeat updating of vowel count
for vowel in 'aeiou':
    # simple calculation (count occurences of vowel in string)
    num_vowels += name.count(vowel)
# output result
print "Hello %s, there are %d vowels in your name." % (name, num_vowels)
