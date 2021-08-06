#! /Users/user/.pyenv/versions/3.7.5/bin/python3
# passwordGenerator.py - an insecure password locker program.
import sys
import random
import array
import pyperclip

# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = input('specify you randomly generated password length ')


if MAX_LEN.isalpha():
    print('enter a digit length for random password')
elif MAX_LEN.isdigit():
    MAX_LEN = int(MAX_LEN)
    if MAX_LEN > 100:
        print('proposed password too long...')
        print('try again')
    else:

        specialChars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                        '*', '(', ')', '<']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lowerChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                      'z']
        upperChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                      'Z']

        passwordElements = specialChars + nums + lowerChars + upperChars

        # pick a random element from each list
        rand_special = random.choice(specialChars)
        rand_num = random.choice(nums)
        rand_lower = random.choice(lowerChars)
        rand_upper = random.choice(upperChars)

        temp_pass = rand_special + rand_lower + rand_upper + rand_num

        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(passwordElements)

            # convert temporary password into array and shuffle to
            # prevent it from having a consistent pattern
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        genPassword = ""
        for x in temp_pass_list:

            genPassword = genPassword + x


        pyperclip.copy(genPassword)

        print('generated password added to clipboard')
