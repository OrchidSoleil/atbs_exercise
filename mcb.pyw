# This is a task from Chapter 9, called 'Extending the Multi-Clipboard'
# below is the original code, it's under comments, because it was in a book
  # mcb.pyw - Saves and loads pieces of text to the clipboard. 
  
   # Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        python mcb.pyw <keyword> - Loads keyword to clipboard.
   #        python mcb.pyw list - Loads all keywords to clipboard.
   # this should be typed in IDEs terminal or command prompt if the bat file is created

# import shelve, pyperclip, sys
#
# mcbShelf = shelve.open('mcb')
#
# if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
#         # Save clipboard to keyword.
#         mcbShelf[sys.argv[2]] = pyperclip.paste()
# elif len(sys.argv) == 2:
#     if sys.argv[1].lower() == 'list':
#         # Copy list of keywords to clipboard.
#         pyperclip.copy(str(list(mcbShelf.keys())))
#     elif sys.argv[1] in mcbShelf:
#         # Load the keyword to the clipboard.
#         pyperclip.copy(mcbShelf[sys.argv[1]])
#
# mcbShelf.close()


# Extending the Multi-Clipboard
# Extend the multi-clipboard program in this chapter
  # so that it has a delete <keyword> command line argument
  # that will delete a keyword from the shelf.
  # Then add a delete command line argument that will delete all keywords.
  
  import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        # Save clipboard to keyword.
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'del':
        # delete keyword from the clipboard
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        # Copy list of keywords to clipboard.
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # Load the keyword to the clipboard.
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delall':
    # delete all keywords
        mcbShelf.clear()

mcbShelf.close()
