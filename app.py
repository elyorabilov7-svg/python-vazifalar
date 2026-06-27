import random
while True:
    emojis = { 'r': '🪨',
            's': '✂️',
            'p': '📄'}

    choices = ('r', 's', 'p')
    choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if choice not in choices:
        print("Invalid Choice!")
        continue
        
    computer_choice = random.choice(choices)

    print(f"You chose {emojis[choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if choice == computer_choice:
        print("Tie")
    elif choice == 'r' and computer_choice == 's':
        print("You win!")
    elif choice == 's' and computer_choice == 'p':
        print("You win!")
    elif choice == 'p' and computer_choice == 'r':
        print("You win!")
    else:
        print("You lose!")
        
    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing")
        break


