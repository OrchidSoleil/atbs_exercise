# zZ= Comma Code =Zz

This is a task from Automate the Boring Staff, chapter 4 'Lists'.

# 1. Say you have a list value like this: spam = ['apples', 'bananas', 'tofu', 'cats']
# 2. Write a function that takes a list value as an argument
# 3. and returns a string with all the items separated by a comma and a space,
# 4. with "and" inserted before the last item.
# 5. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# 6. But your function should be able to work with any list value passed to it.
# 7. Be sure to test the case where an empty list [] is passed to your function.

def coma (li):
    try:
        for i in range(len(li[:-1])):
            print(li[i], end=', ')
        print('and ' + li[-1])

    except IndexError:
        print('The list is empty')


spam = ['apples', 'bananas', 'tofu', 'cats']
spam1 = ['neroli', 'verbena', 'patchouli', 'vetiver', 'ylang-ylang']
empty_list = []


coma(spam) # apples, bananas, tofu, and cats
coma(spam1) # neroli, verbena, patchouli, vetiver, and ylang-ylang
coma(empty_list) # without try-except this shows IndexError: the list is out of range
