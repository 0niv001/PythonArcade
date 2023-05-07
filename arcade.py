import HangMan
import RPS
import TreasureIsland

games = {
    1: ["Rock, Paper, Scissors", RPS.rps_round],
    2: ["Treasure Island", TreasureIsland.treasure],
    3: ["Hangman", HangMan.hangman],
    4: ["BlackJack", ],
    5: ["Number Guess", ],
    6: ["Higher Lower", ],
    7: ["Quiz"],
}
on = True

while on:
    print('''  _____       _   _                                              _      
 |  __ \     | | | |                     /\                     | |     
 | |__) |   _| |_| |__   ___  _ __      /  \   _ __ ___ __ _  __| | ___ 
 |  ___/ | | | __| '_ \ / _ \| '_ \    / /\ \ | '__/ __/ _` |/ _` |/ _ \
 | |   | |_| | |_| | | | (_) | | | |  / ____ \| | | (_| (_| | (_| |  __/
 |_|    \__, |\__|_| |_|\___/|_| |_| /_/    \_\_|  \___\__,_|\__,_|\___|
         __/ |                                                          
        |___/                                                           ''')
    print("<< Welcome to the Python Arcade >>\nTo start playing, type the number of the game you want to play")
    for key, value in games.items():
        print(f"{key}: {games[key][0]}")
    choice = int(input("Game: "))
    print(f"<< {games[choice][0]} >>")
    games[choice][1]()
    again = input("Do you want to play a different game? Type 'yes' to go back to the menu, or press any other key to "
                  "quit \n").lower()
    if again != "yes":
        on = False