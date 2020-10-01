# zZ= Mad Libs =Zz
# 1. Create a Mad Libs program that reads in text files
# 2. and lets the user add their own text anywhere
# 3. the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# 4. For example, a text file may look like this:
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
# unaffected by these events.
# 5. The program would find these occurrences and
# 6. prompt the user to replace them.
#Enter an adjective:
# silly
# Enter a noun:
# chandelier
# Enter a verb:
# screamed
# Enter a noun:
# pickup truck

# 7. The following text file would then be created:
# 8. The silly panda walked to the chandelier and then screamed. A nearby pickup
# truck was unaffected by these events.
# 9. The results should be printed to the screen
# 10. and saved to a new text file.

# i could use replace() method on strings, but since it's not in the book i won't

import shelve, sys, re

mad_libs_txt = open('mad_libs.txt', 'w') # this creates file with the following text
mad_libs_txt.write('The ADJECTIVE panda walked to the NOUN and then VERB.\nA nearby NOUN was unaffected by these events.')
mad_libs_txt.close()
# to access text file content one must open the file with read() method
mad_libs_txt = open('mad_libs.txt')
text = mad_libs_txt.read()
mad_libs_txt.close()

# regex for speech parts search
speech_parts = re.compile(r'[A-Z]{2,}')

# make a list with split() function, to let the program search through words, not letters
text_list = text.split()

for word in text_list:

    fin = speech_parts.search(word) # apply regex
    if fin:
        user_input = input('Please eneter ' +  str(fin.group()) + ' ')
        text_list.insert(text_list.index(word), user_input.lower())
        text_list.remove(word)

text_update = ' '.join(text_list)
mad_libs_new = open('mad_libs_new.txt', 'w')
mad_libs_new.write(text_update)
print(text_update)
mad_libs_new.close()
