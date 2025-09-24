import random
while True:
   number_to_guess = random.randint(1,100)


   while True:
    try:
     user_input = int(input("Guess the number 😁 between 1 to 100: "))
     if user_input < number_to_guess:
      print("Too low 🥲")

     elif user_input > number_to_guess:
      print("Too High 🥲")
     else:
      print("congratulations 🥳u have guessed correct number🥳!")
      break 
    except ValueError:
     print("Invalid input please enter a number")
   play_again=input("do u want to play again(yes/No)").lower()
   if play_again!="yes":
     print("Thanks for playing😁")
     break
