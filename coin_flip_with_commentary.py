# zZ= Coin Flip Streaks =Zz

# this is a task from Automate the Boring Staff, chapter 4 'Lists'
import random

print('Coin Flip Streaks \n This is a task from Automate the Boring Staff, chapter 3 "Lists", '
      'For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and \n'
      'write down an “H” for each heads and “T” for each tails, you’ll create a list that \n'
      'looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips,\n'
      ' you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” \n'
      'which looks random (to humans), but isn’t mathematically random. A human will almost \n'
      'never write down a streak of six heads or six tails in a row, even though it is highly \n'
      'likely to happen in truly random coin flips. Humans are predictably bad at being \n'
      'random.')

# 1. Write a program to find out how often a streak of six heads
# or a streak of six tails comes up
# 2. in a randomly generated list of heads and tails.
# 3. Your program breaks up the experiment into two parts:
# 4. the first part generates a list of randomly selected 'heads' and 'tails' values,
# 5. and the second part checks if there is a streak in it.
# 6. Put all of this code in a loop
# 7. that repeats the experiment 10,000 times
# 8. so we can find out what percentage of the coin flips contains a streak of six heads
# or tails in a row.
# 9. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time
# 10. and a 1 value the other 50% of the time.

# You can start with the following template:

# import random
# numberOfStreaks = 0
# for experimentNumber in range(10000):
# Code that creates a list of 100 'heads' or 'tails' values.
# Code that checks if there is a streak of 6 heads or tails in a row.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# zZ= Coin Flip Streaks Counter =Zz
print('\n\n zZ= Coin Flip Streaks Counter =Zz.')

streaks = 0

for experimentNumber in range(10000):
    heads_and_tails = ['H', 'T']  # this is a list of 1 heads and 1 tails to randomly choose from
    random_heads_and_tails = []  # this is an empty list, which later random.choice() function will fill

    # this is how i fill an empty list with 100 random values of heads and tails
    for j in range(100):
        random_heads_and_tails.append(random.choice(heads_and_tails))

    # next i create 2 counters
    row = 1  # this counts the amount of heads or tails in a row, we start with one, because each time we compare 2 values
    streaks = 0  # this counts the amount of streaks of 6 heads or 6 tails

    # to avoid 'list index out of range' error, i subtract one from the list length
    for i in range(len(random_heads_and_tails) - 1):
        # this time i compare values by using their index i
        if random_heads_and_tails[i] == random_heads_and_tails[i + 1]:
            row += 1  # every time the next value equals current value row counter is increased by 1
            if row == 6:
                streaks += 1
                row = 1
            else:
                pass
        else:
            row = 1
    # here coin flip counter ends, but in order to verify the result i used brute force below.

    # zZ= Brute Force Coin Flip Streak Counter =Zz
    heads = 0  # heads counter, starts with 0 because we compare values one by one
    tails = 0  # tails counter
    number_of_streaks = 0
    # this time i compare by values
    for v in random_heads_and_tails:
        if v == 'H':
            heads += 1
            tails = 0
            if heads == 6:
                number_of_streaks += 1
                heads = 0
            else:
                pass
        else:
            tails += 1
            heads = 0
            if tails == 6:
                number_of_streaks += 1
                tails = 0
            else:
                pass

print('The amount of heads and tails in a list is ', len(random_heads_and_tails))
print('The number of experiments is ', experimentNumber + 1)
print('Total amount of streaks', streaks)
print('Chance of streak: %s%%' % (streaks / 100))


print('\n\nzZ= Brute Force Coin Flip Streak Counter =Zz')
print('Amount of streaks', number_of_streaks)
print('Chance of streak: %s%%' % (number_of_streaks / 100))
