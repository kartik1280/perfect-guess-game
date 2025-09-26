import random
n = random.randint(1,100)
a = -1
guesses = 1
while (a != n):
    a = int(input("guess the number: "))

    if (a>n):
        print("enter lower number please")
        guesses += 1
    elif (a<n):
        print("enter higher number please")
        guesses += 1


print(f"you have guess the correct number {n} in {guesses} attempts")
