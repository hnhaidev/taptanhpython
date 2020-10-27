from random import randint

print("Nhap (Dam, La, Keo): ")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "Dam"
elif computer == 1:
    computer = "La"
elif computer == 2:
    computer = "Keo"

print("-------")
print("You choose: "+player)
print("Computer choose: "+computer)
print("-------")

if player == computer:
    print("Draw")
else:
    if player == "Dam":
        if computer == "La":
            print("Lose")
        else: 
            print("Win")

    elif player == "La":
        if computer == "Dam":
            print("Lose")
        else: 
            print("Win")

    elif player == "Keo":
        if computer == "Dam":
            print("Lose")
        else: 
            print("Win")
    
    else:
        print("Bạn Nhập Sai!")