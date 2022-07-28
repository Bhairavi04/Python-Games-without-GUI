# n=18
# no. of guesses 3
# print no. of guesses left
#no. of guesses he took to win
# game over
# you won

n= 20
guess=1

while(True):
    print("Guess:", guess)
    guess += 1

    num = int(input("Enter the number : "))
    if guess<=3 or num==20:
        if num<20:
            print("Increase the number")
            print(guess,"attempt left\n")

        elif num>20:
            print("Decrease the number")
            print(guess, "attempt left\n")
            continue
        else:
            if num == 20:
                print("You won in",guess-1,"attempt")
            break


    else:
        print("You lost!!\nattempts over")
        break

