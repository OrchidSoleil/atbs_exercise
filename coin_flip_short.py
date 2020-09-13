# zZ= Coin Flip Streaks =Zz

# this is a task from Automate the Boring Staff, chapter 4 'Lists'


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

import random
print('\n\n zZ= Coin Flip Streaks Counter =Zz.')

streaks = 0

for experimentNumber in range(10000):
    heads_and_tails = ['H', 'T']  
    random_heads_and_tails = []  

    
    for j in range(100):
        random_heads_and_tails.append(random.choice(heads_and_tails))

    
    row = 1  
    streaks = 0  

    
    for i in range(len(random_heads_and_tails) - 1):
        
        if random_heads_and_tails[i] == random_heads_and_tails[i + 1]:
            row += 1  
            if row == 6:
                streaks += 1
                row = 1
            else:
                pass
        else:
            row = 1
    
print('Chance of streak: %s%%' % (streaks / 100))


