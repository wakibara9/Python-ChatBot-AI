# Jason Vo
# 1/20/2023
# Project 1: Conversation with an Educational Chat Bot


# ask for guest's name
def get_name():
    name = input("Please type your first name: ")
    print("Hello",name,)
    print()
    print("==========") #start of chat sequence
    return name


# title of program -- provide AICB details, purpose, and short overview.
def display_title():
    print("Welcome to Etherhallow.")
    print()
    print("I am Sebastian, the owner of Etherhallow. At Etherhallow, our goal is to spread knowledge about a particular video game. \nIt is my life purpose to inform others about the video game Sid Meier's Civilization VI (often referred to as CivVI or Civ6).")
    print()
    print("Sid Meier's Civilization VI (2016) is the newest installment in the award winning Civilization Franchise.")
    print()
    print("It is a turn-based, strategy, 4X video game developed by Firaxis Games, published by 2K Games, and distributed by Take-Two Interactive.")
    print()
    print("I've been playing Civ6 since its release and am the one and only first owner of a copy.")
    print()


# primary logic for information dispersal
def talking():
    while True:  # confirm user agreement to proceed
        learn_more = input("Would you like to learn more about Sid Meier's Civilization VI? (y/n): ")
        print()
        if learn_more == "y":  #information will proceed/end based on user choice.
            print("Great to hear! What would you like to learn about? I can tell you about the following game aspects...")
            print()
            print("A: Gameplay details \nB: Character details \nC: Platforms and Controls details  \n ")

            genre = input("Select a letter to continue learning: ")  #information routes based on user choice
            if genre == "A":
                print("So you would like to learn about gameplay details...")
                print()
                print("In Civilization VI, you are playing as a leader of a certain nation (Civilization) and must guide its growth over the course of several eras of time.\n You must manage aspects of life such as population, loyalty, and food. Keeping your people sounds simple, but can quickly become out of hand as the game progresses. If you don't keep them happy, they could stage a rebellion against you!")
                print()
                print("There are also ways to interact with the computer-controlled AI -- each with their own unique tendencies, which creates unique and memorable interactions. The AI has unique agendas and personalities, leading to a myriad of possibilities for how you can interact with them.")
                print()
                print("To achieve victory, there is a  variety of methods such as Domination, Culture, Religious, and more. My favorite is Domination because it's the most simple victory; all you have to do is conquer all of your enemies through military might!")
                print()
                continue

            elif genre == "B":
                print("So you would like to learn about Character details...")
                print()
                print("In Civilization VI, you are able to choose a wide variety of historical figures from varying periods of time. A few examples of this would be: Gilgamesh of the Sumeria (2500 BC), Julius Caesar of Rome (100 BC), and Abraham Lincoln of the United States of America (1800 AD).") 
                print()
                print("My personal reccomendation would be Trajan of Rome. His leader bonus provides a free building in each of your cities and his Civilization ability is to automatically generate roads between your cities and its capital, leading to increased income and faster travel time. For newcomers, it can make your learning experience a bit easier.")
                print()
                print("There are many available leaders and civilizations to choose from, each with their own unique abilities and perks. If you take time to explore the many options, I am sure that you'll find a good fit somewhere.")
                print()
                continue

            elif genre == "C":
                print("So you would like to learn about Platforms and Controls details...")
                print()
                print("Currently, Sid Meier's Civilization VI is available on Microsoft Windows, macOS, Linux, iOS, Nintendo Switch, Playstation 4, Xbox One, and Android.")
                print()
                print("Thanks to the variety of platform availability, you can play using a mouse and keyboard, various console controllers, or even your phone and/or tablet. I prefer mouse and keyboard because I play on PC via Steam.")
                print()
                print("Feel free to experiment and find whatever is most comfortable for you!")
                print()
                continue

            else: 
                print("I'm sorry, I didn't quite get that.")
                continue

        elif learn_more == "n": #exit loop
            print("Understood. I will escort you to the exit.")
            print()
            break
        else:
            print("I'm sorry, I didn't quite get that.")
            continue

# parting messages, email request
def farewell():
    bye = input("Before leaving - would you like to stay in touch? [y/n]: ")
    print()
    while True:
        if bye == "y": #email request 
            email = input("Please write your email address down here: ")
            print()
            print("Your email address is:", email)
            print()
            print("I have your email down as", email)
            print()
            print("I will be in touch soon.")
            print()
            break
        if bye == "n":
            print("No worries. I will always be here if you would like to talk again.")
            print()
            break
        else:
            print("I'm sorry, I didn't quite get that.")
            continue

def main():
    name = get_name()
    display_title()
    talking()
    farewell()
    print("Goodbye", name, "!", "Thank you for visiting Etherhallow and taking the time to talk with me.")
    print("==========") #end of chat sequence


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
