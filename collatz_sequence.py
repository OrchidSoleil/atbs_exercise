print('This is Collatz Sequence Function. The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.')

### Task: 
# 1. Write a function named collatz() 
# 2. that has one parameter named number. 
# 3. If number is even, then collatz() should print number // 2 and return this value. 
# 4. If number is odd, then collatz() should print and return 3 * number + 1.
#
# 5. Then write a program that lets the user type in an integer 
# 6. and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
# 7. Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
#Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.


### Collatz Sequence

def collatz(number):

    if number % 2 == 0: #checks if number is even
        return number//2
    else:
        return 3*number+1 #checks if number is odd


n = int(input('Enter any integer greater than 1: ')) # n variable here contains an integer

while n != 1: #until integer doesn't equal 1.
    n = collatz(n) #then variable n equals collatz function of n.
    print(n) #print variable n after it was run through collatz function and continue while loop again.

    
  ### Collatz sequence WITH input Validation  
