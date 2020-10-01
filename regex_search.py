# Regex Search among computer files
# 1. Write a program that opens all .txt files in a folder 
# (I changed it to .py files for my own use)
# 2. and searches for any line
# 3. that matches a user-supplied regular expression.
# 4. The results should be printed to the screen.

import re
from pathlib import Path

# a path to a current working directory, that's where the program will look
p = Path.cwd()

search_word = re.compile(input('SEARCH: '), re.IGNORECASE) # my regex

for a_file in p.glob('*.py'):
    content = a_file.read_text()
    mo = search_word.search(content)
    if mo:
        print(mo.group(), 'found in ', a_file)
    else:
        pass
