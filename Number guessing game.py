import random
import math

def even_or_odd(b):
    print(' My number is even.') if b%2==0 else print(' My number is odd.')
def is_prime(b):
    while b!=1:
        if b in [i for i in range(2,b) if 0 not in [i%j for j in range(2,i)]]:
            return 1
        else:
            return 0
def is_square(b):
    if abs(math.sqrt(b)-math.floor(math.sqrt(b)))==0:
        return 1
    else :
        return 0
def is_mul9(b):
    if b%3==0 or b%9==0:
        return 1
    else :
        return 0


if __name__=='__main__':
    g=3 #Number of guesses
    cl=3
    n=random.randrange(101) #
    ch=0
    ch1=0
    U_name= input("Hello player, what's your name ?")
    print("\n Hi {}, Let's get on with the game!\n In this game you will have three chances to guess the number that I have in mind.\n It lies between 1-50.\n Lets see if can guess it !!\n Here's your first clue:".format(U_name))
    even_or_odd(n)
    cl-=1
    ip=int(input(" Enter your guess:"))
    g-=1
    if ip==n:
        print(" Wow you got it right.\n Yes my number is {}. ".format(n))
        exit()
    else :
        i=random.randrange(1,11)
        if n+i<=100 and n-i>=0:
            print(" Nope.That's not it!\n It lies in the range {}-{}. You have {} more guesses left.".format(n-i,n+i,g))

    ip = int(input("Enter your next guess:"))
    g -= 1
    if ip == n:
        print(" Your guess is correct,it is {}".format(n))
        exit()
    ch= int(is_prime(n))
    ch1=int(is_prime(ip))

    if ch^ch1==1:
        print(" Your guess is wrong,\n Here's my next clue,my number is a prime number!") if ch else print(" No your guess is wrong,\n Here's my next clue,my number is a prime number!")
        cl-=1
    else:
        print(" Yes you are right,my number is a prime ") if ch else print(" Yes you are right,my number is a not a prime.")
        print(" But its not my number.\n Now for the next clue: ")
        ch=is_square(n)
        if ch:
            print(" My number is a perfect square")
        else:
            print(" My number is not a perfect square")

    #print(" Here is you last clue:My number is divisible by 3") if ch else print(" My number is not divisible by 3")
    #cl -= 1
    ip=int(input(" Enter your last guess:"))
    if ip==n:
        print(" That was a close one, but you guessed it right. My number is {}".format(n))
    else:
        print(" You lost the game,My number was {}".format(n))




























