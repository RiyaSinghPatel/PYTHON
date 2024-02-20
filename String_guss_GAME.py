# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string

option = input("Do you want to code or decode? ")  # code or decode
s = input("Enter the word: ")
words = s.split(" ")


if option == "code":
    nwords = []
    for word in words:
        if len(word) >= 3:
            first_three = word[:1]
            lst_three = word[1:]
            code = lst_three + first_three
            random_word = ''.join(random.choices(string.ascii_lowercase, k=3))
            code1 = random_word + code + random_word 
            nwords.append(code1)
        else:
            reversed_string = word[::-1]
            nwords.append(reversed_string)
    print("Code of your entered word is:", ' '.join(nwords))
elif option == "decode":
    nwords = []
    for word in words:
        if len(word) >= 3:
            trimmed_word = word[2:-3]
            new=trimmed_word[-1]+trimmed_word[1:-1]
            nwords.append(new)
        else:
            reversed_string = word[::-1]
            nwords.append(reversed_string)
    print("Code of your entered word is:", ' '.join(nwords))

else:
    pass