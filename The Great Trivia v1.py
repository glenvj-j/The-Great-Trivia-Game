import random
import time
import os
from colorama import Fore, Style

data_base_0 = [
    {"question" : "What is the capital city of Italy?", "option" : [("1","Venice"),("2","Florence"),("3","Rome"),("4","Milan")], "answer" : "3", "hint" : "It's known for its ancient history and the Colosseum."},
    {"question" : "What is the official currency of Japan?", "option" : [("1","Yuan"),("2","Yen"),("3","Won"),("4","Ringgit")], "answer" : "2", "hint" : "It's represented by the symbol ¥."},
    {"question" : "Which city is known as the 'Big Apple'?", "option" : [("1","Chicago"),("2","Los Angeles"),("3","New York City"),("4","Miami")], "answer" : "3", "hint" : "Think of Times Square and Broadway."},
    {"question" : "What type of travel is primarily focused on experiencing nature?", "option" : [("1","Cultural tourism"),("2","Ecotourism"),("3","Business travel"),("4","Adventure tourism")], "answer" : "2", "hint" : "It often includes wildlife conservation and sustainable practices."},
    {"question" : "Which country is home to the Great Barrier Reef?", "option" : [("1","Australia"),("2","Mexico"),("3","Indonesia"),("4","Philippines")], "answer" : "1", "hint" : "It's the largest coral reef system in the world."},
    
    {"question" : "Which city is famous for its canals and gondolas?", "option" : [("1","Amsterdam"),("2","Venice"),("3","Bangkok"),("4","Stockholm")], "answer" : "2", "hint" : "It's known as 'The Floating City.'"},
    {"question" : "What is the primary language spoken in Egypt?", "option" : [("1","Arabic"),("2","English"),("3","French"),("4","Spanish")], "answer" : "1", "hint" : "It's the most widely spoken language in the country."},
    {"question" : "Which continent is the Sahara Desert located on?", "option" : [("1","Asia"),("2","Africa"),("3","Australia"),("4","South America")], "answer" : "2", "hint" : "It's the largest hot desert in the world."},
    {"question" : "What is the currency used in the United Kingdom?", "option" : [("1","Euro"),("2","Pound Sterling"),("3","Dollar"),("4","Yen")], "answer" : "2", "hint" : "It's represented by the symbol £."},
 
    {"question" : "Which city is known for its historic Colosseum?", "option" : [("1","Athens"),("2","Rome"),("3","Istanbul"),("4","Barcelona")], "answer" : "2", "hint" : "It's an ancient amphitheater."},
    {"question" : "What is the main mode of transportation in Tokyo?", "option" : [("1","Train"),("2","Bicycle"),("3","Rickshaw"),("4","Tram")], "answer" : "1", "hint" : "It's one of the busiest rail systems in the world."},
    {"question" : "Which country is famous for tulips and windmills?", "option" : [("1","Belgium"),("2","Netherlands"),("3","Denmark"),("4","Switzerland")], "answer" : "2", "hint" : "Think of Keukenhof gardens."},
    {"question" : "What is the official language of Brazil?", "option" : [("1","Spanish"),("2","English"),("3","Portuguese"),("4","French")], "answer" : "3", "hint" : "It's the only Portuguese-speaking country in South America."},
 
 
    {"question" : "Which landmark is an ancient Incan city located in Peru?", "option" : [("1","Chichen Itza"),("2","Petra"),("3","Machu Picchu"),("4","Angkor Wat")], "answer" : "3", "hint" : "It's situated high in the Andes mountains."},
    {"question" : "What is the largest country by land area?", "option" : [("1","China"),("2","Canada"),("3","Russia"),("4","Brazil")], "answer" : "3", "hint" : "It spans over 17 million square kilometers."},
    {"question" : "Which ocean is the smallest in the world?", "option" : [("1","Atlantic"),("2","Indian"),("3","Arctic"),("4","Southern")], "answer" : "3", "hint" : "It covers an area of about 15 million square kilometers."},
    {"question" : "What type of food is paella?", "option" : [("1","Italian"),("2","Spanish"),("3","French"),("4","Greek")], "answer" : "2", "hint" : "It originates from Valencia, Spain."},

    {"question" : "Which continent is home to the Amazon Rainforest?", "option" : [("1","Africa"),("2","Asia"),("3","South America"),("4","North America")], "answer" : "3", "hint" : "It's the largest rainforest in the world."},
    {"question" : "What is the capital city of Canada?", "option" : [("1","Toronto"),("2","Ottawa"),("3","Vancouver"),("4","Montreal")], "answer" : "2", "hint" : "It's name sound like japanese"},
    {"question" : "What is the capital city of Australia?", "option" : [("1","Sydney"),("2","Canberra"),("3","Melbourne"),("4","Brisbane")], "answer" : "2", "hint" : "It's located in the Australian Capital Territory."},
    {"question" : "Which city is known as the 'City of Light'?", "option" : [("1","New York City"),("2","Paris"),("3","Tokyo"),("4","London")], "answer" : "2", "hint" : "Famous for its art, fashion, and culture."},
    {"question" : "Which mountain is considered the highest peak in the world?", "option" : [("1","Kilimanjaro"),("2","Mount Everest"),("3","Puncak Jaya"),("4","Lhotse")], "answer" : "2", "hint" : "It stands at 8,848 meters."},

    {"question" : "Which country is known for its pyramids?", "option" : [("1","Greece"),("2","Mexico"),("3","Egypt"),("4","China")], "answer" : "3", "hint" : "The Great Pyramid of Giza is one of the Seven Wonders."},
    {"question" : "What is the capital of Thailand?", "option" : [("1","Bangkok"),("2","Hanoi"),("3","Kuala Lumpur"),("4","Jakarta")], "answer" : "1", "hint" : "It's famous for its vibrant street life."},
    {"question" : "What type of food is sushi?", "option" : [("1","Italian"),("2","Mexican"),("3","Japanese"),("4","Chinese")], "answer" : "3", "hint" : "It often includes rice and raw fish."},
    {"question" : "Which country is known for the Great Wall?", "option" : [("1","China"),("2","Japan"),("3","India"),("4","Mongolia")], "answer" : "1", "hint" : "It was built to protect against invasions."},
    {"question" : "What is the official currency of Canada?", "option" : [("1","Dollar"),("2","Euro"),("3","Pound"),("4","Yen")], "answer" : "1", "hint" : "It's similar to the US dollar."},

    {"question" : "Which country is known for the Statue of Liberty?", "option" : [("1","Canada"),("2","United States"),("3","France"),("4","Australia")], "answer" : "2", "hint" : "It was a gift from France to the US."},
    {"question" : "What is the capital city of Greece?", "option" : [("1","Athens"),("2","Rome"),("3","Istanbul"),("4","Cairo")], "answer" : "1", "hint" : "It's known for ancient ruins like the Acropolis."},
    {"question" : "What is the main language spoken in South Africa?", "option" : [("1","English"),("2","Zulu"),("3","Afrikaans"),("4","All of the above")], "answer" : "4", "hint" : "South Africa has 11 official languages."},
    {"question" : "Which river is the longest in the world?", "option" : [("1","Amazon"),("2","Nile"),("3","Yangtze"),("4","Mississippi")], "answer" : "2", "hint" : "It runs through northeastern Africa."},
    {"question" : "Which country is famous for its chocolate?", "option" : [("1","Belgium"),("2","Switzerland"),("3","Germany"),("4","France")], "answer" : "2", "hint" : "It's known for its high-quality chocolate."},

    {"question" : "Which desert is the largest hot desert in the world?", "option" : [("1","Arabian"),("2","Gobi"),("3","Sahara"),("4","Kalahari")], "answer" : "3", "hint" : "It spans several countries in North Africa."},
    {"question" : "What is the capital city of South Korea?", "option" : [("1","Seoul"),("2","Busan"),("3","Incheon"),("4","Gwangju")], "answer" : "1", "hint" : "Known for its modern skyline"},
    {"question" : "Which traditional Korean dish is made from fermented vegetables?", "option" : [("1","Kimchi"),("2","Sushi"),("3","Pho"),("4","Pad Thai")], "answer" : "1", "hint" : "Known for it's red color and sour taste"},
    {"question" : "What is the name of the traditional Korean dress?", "option" : [("1","Hanbok"),("2","Kimono"),("3","Cheongsam"),("4","Sari")], "answer" : "1", "hint" : "Worn during holidays and celebrations"},
    {"question" : "What is the popular Korean pop music genre called?", "option" : [("1","J-Pop"),("2","K-Pop"),("3","C-Pop"),("4","M-Pop")], "answer" : "2", "hint" : "Known for its catchy tunes"}
]

data_base = data_base_0.copy()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def randomizer():
    question_choice = random.choice(range(0,len(data_base)))
    return question_choice

#------------------------All Setting

choosen_number = randomizer()

point_counter = 0 # default 0
win_condition = 10 # default 10

player_health = 10 # default 10
max_health = 10 # default 10

user_name = ""
gender_choosen = []


helper = 3 # default 3
max_helper = 3 # default 3

story_pace = 0.02 # default 0.02
speed = 2.3 #default 2.3

def setting():
    global player_health
    global helper
    global win_condition

    while True:
        print('''
            Level:
              
            ╔═════════════╗ 
            ║  1. Easy    ║
            ║  2. Medium  ║
            ║  3. Hard    ║
            ╚═════════════╝

              ''')
        selection = input("What Mode you want to play? : ") #1 is easy, 2 medium, 3 hard
        if selection == "1":
            player_health = 10
            helper = 3
            win_condition = 5
            break
        elif selection == "2":
            player_health = 5
            helper = 2
            win_condition = 10
            break
        elif selection == "3":
            player_health = 2
            helper = 2
            win_condition = 20
            break
        else:
            continue


def user_detail():
    global user_name
    global gender_choosen
    user_name = input("Type Your name : ")
    gender = input("Input your gender (M/F): ") #to determine what to use in dialogue
    while True:
        if gender.upper() == "M":
            gender_choosen.append(("he","his"))
            break
        elif gender.upper() == "F":
            gender_choosen.append(("she","her"))
            break
        else:
            print("Please choose between M or F")
            gender = input("Input your gender (M/F): ")
    
def storytime():
    global gender_choosen
    global user_name
    story = f'''
        Once upon a time, a human named {user_name.capitalize()} was an avid traveler and trivia enthusiast, walking through a forest.


        At one point, {user_name.capitalize()} noticed a strange tree that held a mysterious door.
        When {user_name.capitalize()} approached, the door suddenly opened, pulling {user_name.capitalize()} inside the tree.


        {user_name.capitalize()} woke up in a village inhabited by owls as big as humans.
        Panicked, {user_name.capitalize()} ran to the village entrance, but one of the owls, named {Fore.BLUE+"Quote"+Style.RESET_ALL}, stopped {user_name.capitalize()}.


        Quote explained that if {user_name.capitalize()} wanted to go back to {gender_choosen[0][1]} world,
        {gender_choosen[0][0]} would need to fight a monster outside the village until reaching the door {gender_choosen[0][0]} had come through.
        The monsters could only be defeated by {Fore.RED+"answering questions"+Style.RESET_ALL}.


        As an avid trivia enthusiast who also wanted to go home, {user_name.capitalize()} accepted the challenge.
        Quote offered {user_name.capitalize()} help by giving hints and part of the answers, but only for a limited time.


        “If you can defeat {Fore.GREEN+str(win_condition)+Style.RESET_ALL} monsters, you can go back to your world! So let's start!”'''
    print()
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("|                                           The Great TRIVIA ODYSSEY                                                     |\n")
    for i in story:
        print(i,end='', flush=True)
        time.sleep(story_pace)
    print("\n\n\n")
    wait = input("Click Enter to start the game")

def health_bar():
    bar = ""
    if max_health >= player_health >=3:
        for i in range(1):
            for j in range(player_health):
                bar += Fore.GREEN+"■■"+Style.RESET_ALL
            for k in range(max_health-player_health):
                bar += "□□"
    elif player_health <= 2:
        for i in range(1):
            for j in range(player_health):
                bar += Fore.RED+"■■"+Style.RESET_ALL
            for k in range(max_health-player_health):
                bar += "□□"
    else:
        bar += Fore.RED+"□□"*6+Style.RESET_ALL
    return bar

def quo_bar():
    quo_bar = ""
    if helper >1:
        for i in range(1):
            for j in range(helper):
                quo_bar += Fore.GREEN+"■■"+Style.RESET_ALL
            for k in range(max_helper-helper):
                quo_bar += "□□"
    elif helper == 1:
        for i in range(1):
            for j in range(helper):
                quo_bar += Fore.RED+"■■"+Style.RESET_ALL
            for k in range(max_helper-helper):
                quo_bar += "□□"
    elif helper == -1:
        quo_bar += Fore.RED+"last power"+Style.RESET_ALL
    else:
        quo_bar += Fore.RED+"□"*6+Style.RESET_ALL
    return quo_bar

#------------------------GUI


menu_cover = r'''|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|
│═══════════════════════════════════════════════════════════════════════│
│                                                                       │
│                    ╔╦╗╦ ╦╔═╗  ╔═╗╦═╗╔═╗╔═╗╔╦╗                         │  
│                     ║ ╠═╣║╣   ║ ╦╠╦╝║╣ ╠═╣ ║                          │
│     ___________ ____╩ ╩ ╩╚═╝__╚═╝╩╚═╚═╝╩ ╩ ╩__ _______      _         │
│     |  _   _  ||_   __ \   |_   _||_  _| |_  _||_   _|     / \        │
│     |_/ | | \_|  | |__) |    | |    \ \   / /    | |      / _ \       │
│         | |      |  __ /     | |     \ \ / /     | |     / ___ \      │
│        _| |_    _| |  \ \_  _| |_     \ ' /     _| |_  _/ /   \ \_    │
│       |_____|  |____| |___||_____|     \_/     |_____||____| |____|   │ 
│                                                                       │
│                       ╔═╗╔╦╗╦ ╦╔═╗╔═╗╔═╗╦ ╦                           │
│                       ║ ║ ║║╚╦╝╚═╗╚═╗║╣ ╚╦╝                           │
│                       ╚═╝═╩╝ ╩ ╚═╝╚═╝╚═╝ ╩                            │
│                                                                       │'''


def main_menu():
    clear_console()
    print(f'''
┌───────────────────────────────────────────────────────────────────────┐
{menu_cover}      
│═══════════════════════════════════════════════════════════════════════│
│░░                                                                   ░░│
│░░░                       →  1. New Game                            ░░░│
│░░░░                                                               ░░░░│
│░░░░░                                                             ░░░░░│
│░░░░░░                 → 2. Change Difficulty                    ░░░░░░│
│░░░░░                                                             ░░░░░│
│░░░░                                                               ░░░░│
│░░░                         →  3. Exit                              ░░░│
│░░                                                                   ░░│
│───────────────────────────────────────────────────────────────────────│
│ Trivia Game created by Glen                                           │
└───────────────────────────────────────────────────────────────────────┘''')
    global menu_input
    menu_input = input("        Choose what you want to do : ")
    

def bar_bawah():
    print(f'''│───────────────────────────────────────────────────────────────────────│
│      {point_counter}pt\t│ Health : {health_bar()}\t│\tQuo :{quo_bar()}\t│
└───────────────────────────────────────────────────────────────────────┘''')
    
def bar_atas():
    print(f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│''')
    
def winning_screen():
    clear_console()
    print(Fore.GREEN+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
.-=~=-.-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-
(__  _)           __   __            _    _ _       _             (__  _)
( _ __)           \ \ / /           | |  | (_)     | |            (__  _)
(__  _)            \ V /___  _   _  | |  | |_ _ __ | |            (__  _)
(_ ___)             \ // _ \| | | | | |/\| | | '_ \| |            (_ ___)
(__  _)             | | (_) | |_| | \  /\  / | | | |_|            (__  _)
(_ ___)             \_/\___/ \__,_|  \/  \/|_|_| |_(_)            (__  _)
(__  _)                                                           ( _ __)
.-=~=-.-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-
  
│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
    print(f'''
                       You defeat all the monster!
          
│───────────────────────────────────────────────────────────────────────│

          
                         
                          You reach the door!
                          You can go home now!
                 


                                                                        ''')
    bar_bawah()
    time.sleep(speed)

def losing_ilus():
    print(Fore.RED+r'''│                            ,-=-.       ______                         │
│                           /  +  \     />----->                        │
│                           | ~~~ |    // -/- /                         │
│                           |R.I.P|   //  /  /                          │
│              ___  __ \vV,,|_____|V,//_____/VvV,v,/  _                 │
│              \ \ / /__  _   _  | |    ___  ___  ___| |                │
│               \ V / _ \| | | | | |   / _ \/ __|/ _ \ |                │     
│                | | (_) | |_| | | |__| (_) \__ \  __/_|                │
│                |_|\___/ \__,_| |_____\___/|___/\___(_)                │                
│                                                                       │'''+Style.RESET_ALL)
    

def losing_screen():
    clear_console()
    print(Fore.RED+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│'''+Style.RESET_ALL)
    losing_ilus()
    print(Fore.RED+f'''│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
    
    print('''
                        You lose all your health!
              
│───────────────────────────────────────────────────────────────────────│''')
    print('''
          
                         
                        You failed to reach home!
                    Quote take you back to the village
                 


                                                                        ''')
    bar_bawah()
    time.sleep(speed)



def loading():
    clear_console()
    print(f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│ ~            ~                ___,---,_.,-'=_.-'-._,. ~        ~      │
│         ~         .__.-':_.-'                      '-._    ~       ~  │
│        ) () ()  -,'       _.-'-.-'~,     /\             '-._,         │
│       ) " ( " (   '-.__.  '-.~-'._.-'  /\   /\    𓉙𓉝     _.-'   ~   ~ │
│      )  "  ("  (    '-._              /  \ /  \      _.-'   ~         │
│ -._-│--│--│--│--/  ~   .-'               )       '-._.,.           ~  │
│    \_o__o__o__o/      '-._               (            '-._  ~         │
│                  ~        '.-'._    .-`-._;'-._.='._     _.-'    ~    │
│----------------│      ~          '-_."      ~    ~   '-._:  ~_        │
│ Map of Trivian │             ~                  ~                  ~  │
│═══════════════════════════════════════════════════════════════════════│''')
    print(f'''
                         Welcome to Trivian World
          
│───────────────────────────────────────────────────────────────────────│

          
                         
                          
                              Loading.....
                                


                                                                        ''')
    bar_bawah()
    time.sleep(speed)


def monster_approaching():
    print(f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│                __  __                 _                               │      
│               │  \/  │ ___  _ __  ___│ │_ ___ _ __                    │      
│               │ │\/│ │/ _ \│ '_ \/ __│ __/ _ \ '__│                   │      
│               │ │  │ │ (_) │ │ │ \__ \ ││  __/ │                      │     
│               │_│  │_│\___/│_│ │_│___/\__\___│_│                      │
│       / \   _ __  _ __  _ __ ___   __ _  ___│ │__ (_)_ __   __ _      │
│      / _ \ | '_ \| '_ \| '__/ _ \ / _` |/ __| '_ \| | '_ \ / _` |     │
│     / ___ \| |_) | |_) | | | (_) | (_| | (__| | | | | | | | (_| |     │
│    /_/   \_\ .__/| .__/|_|  \___/ \__,_|\___|_| |_|_|_| |_|\__, |     │
│            |_|   |_|                                       |___/      │
│═══════════════════════════════════════════════════════════════════════│''')
    print(f'''
                          
          
│───────────────────────────────────────────────────────────────────────│

          
                         
                          Prepare yourself!!!!
                     
                      Choose only the right answer!       


                                                                        ''')
    bar_bawah()
    time.sleep(speed)
    clear_console()



def jawaban_benar():
        clear_console()
        print(Fore.GREEN+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│                 __  __                 _                              │
│                |  \/  | ___  _ __  ___| |_ ___ _ __                   │
│                | |\/| |/ _ \| '_ \/ __| __/ _ | '__|                  │
│                | |  | | (_) | | | \__ | ||  __| |                     │
│              __|____|_|\___/__| |_|___/\______|_|  __                 │
│             |  _ \  ___ / _| ___  __ _| |_ ___  __| |                 │
│             | | | |/ _ | |_ / _ \/ _` | __/ _ \/ _` |                 │
│             | |_| |  __|  _|  __| (_| | ||  __| (_| |                 │
│             |____/ \___|_|  \___|\__,_|\__\___|\__,_|                 │
│                                                                       │
│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
        print(f'''


│───────────────────────────────────────────────────────────────────────│



                          Right Answer!!!!
                            
                             Point +1

              
''')
        bar_bawah()
        time.sleep(speed)

def jawaban_salah():
    clear_console()
    print(Fore.RED+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│                                                                       │
│                                                                       │
│         __   __             ____       _     _   _ _ _   _            │
│         \ \ / /__  _   _   / ___| ___ | |_  | | | (_) |_| |           │
│          \ V / _ \| | | | | |  _ / _ \| __| | |_| | | __| |           │
│           | | (_) | |_| | | |_| | (_) | |_  |  _  | | |_|_|           │
│           |_|\___/ \__,_|  \____|\___/ \__| |_| |_|_|\__(_)           │
│                                                                       │      
│                                                                       │ 
│                                                                       │
│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
    print('''

          
│───────────────────────────────────────────────────────────────────────│

          

                           Wrong Answer!!!!
                         
                             Health -1


                                                                        ''')
    bar_bawah()
    time.sleep(speed)


def calling_help_half():
    clear_console()
    
    print(Fore.BLUE+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│     __________-------____                 ____-------__________       │
│     \------____-------___--__---------__--___-------____------/       │
│      \//////// / / / / / \   _-------_   / \ \ \ \ \ /////////        │
│       \////-/-/------/_/_| /_^^    ^^\ |_\_\------\-\-/////           │
│         --//// / /  /  //|| (O)\ /(O) ||//  \  \ \ ////--             │
│              ---__/  // /| \_ (/V\) _/ |\ //  \__---                  │
│                   -//  / /\_ ---v---- _/\ \  //-                      │
│                     \_/_/ /\---------/\ \_\_/                         │
│----------------│        ----\   │   /----                             │
│      Quote     │             │ -│- │                                  │
│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
    print(f'''
                 Behold! I am here to help you {user_name}!
          
│───────────────────────────────────────────────────────────────────────│

          
                         Quote is Helping You!
                          
                          ERASE HALF UNLOCKED
                                

                                Quo -1
                                                                        ''')
    bar_bawah()
    time.sleep(speed)




def calling_help_hint():
    clear_console()
    print(Fore.BLUE+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│     __________-------____                 ____-------__________       │
│     \------____-------___--__---------__--___-------____------/       │
│      \//////// / / / / / \   _-------_   / \ \ \ \ \ /////////        │
│       \////-/-/------/_/_│ /_^^    ^^\ │_\_\------\-\-/////           │
│         --//// / /  /  //││ (O)\ /(O) ││//  \  \ \ ////--             │
│              ---__/  // /│ \_ (/V\) _/ │\ //  \__---                  │
│                   -//  / /\_ ---v---- _/\ \  //-                      │
│                     \_/_/ /\---------/\ \_\_/                         │
│----------------│        ----\   │   /----                             │
│      Quote     │             │ -│- │                                  │
│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
    print(f'''
                 Behold! I am here to help you {user_name}!
          
│───────────────────────────────────────────────────────────────────────│

          
                         Quote is Helping You!
                          
                             HINT UNLOCKED
                                

                                Quo -1
                                                                        ''')
    bar_bawah()
    time.sleep(speed)


def help_zero():
    clear_console()
    
    print(Fore.YELLOW+f'''
╔═══════════════════════════════════════════════════════════════════════╗
│  The Great TRIVIA ODYSSEY \t\t\t\t\t{user_name[0:7]}\t│
│───────────────────────────────────────────────────────────────────────│
│        .-. ,-.                 '                                      |
│       '   (%%'`.                ,_,                                   |
│       `-(%|%)% )               (x,x),               .-. ,-.           |
│         (%/K /,               '(   )               '   (%%'`.         |
│         %./V/%.)               -"-"--             `-(%|%)% )          |
│         (%/%`(',              '------                (%/K /,          |
│           %| ,)                     '               (%/%`(',          |
│            | |                   '                   %| ,)            |
│            | |                '                       | |             |
│            | |                   '                    | |             |
│═══════════════════════════════════════════════════════════════════════│'''+Style.RESET_ALL)
    print(f'''
                          Quote is Exhausted
          
│───────────────────────────────────────────────────────────────────────│

          
                      Quote can't help you anymore!
                                    
                       
                          You must go alone!  
                           
                               
                                                                        ''')
    bar_bawah()
    time.sleep(speed)


giant_ant =r'''│                                                                       │
│                                                                       │
│                              _.---._    /\                            │
│                           ./'       "--`\ //                          │
│                         ./              o \'                          │
│                       /./\  )______   \__ \'                          │
│                      ./  / /\ \  vk│ \ \  \ \'                        │
│                          / /  \ \  │ │\ \  \ 7                        │
│----------------│        "     "    "  "                               │       
│ Giant Anteater │                                                      │
│═══════/\══════════════════════════════════════════════════════════════│''' #pakai r untuk jadi raw string

giant_bat = r'''│                                                                       │
│                                                                       │
│                        =/\                 /\=                        │
│                        / \'._   (\_/)   _.'/ \                        │
│                       / .''._'--(o.o)--'_.''. \                       │
│                      /.' _/ │`'=/ " \='`│ \_ `.\                      │
│                     /` .' `\;-,'\___/',-;/` '. '\                     │
│                    /.-' jgs   `\(-V-)/`       `-.\                    │
│----------------│                                                      │
│    Giant Bat   │                                                      │
│═══════/\══════════════════════════════════════════════════════════════│''' #pakai r untuk jadi raw string

beaverton = r'''│                                                                       │
│                                    ___                                │
│                                 .="   "=._.---.                       │
│                               ."         c ' Y'`p                     │
│                            _ /   ,       `.  w_/                      │
│                        jgs │   '-.   /     /                          │
│                      _,..._│      )_-\ \_=.\                          │
│                      `-....-'`------)))`=-'"`'"                       │
│----------------│                                                      │
│    Beaverton   │                                                      │
│═══════/\══════════════════════════════════════════════════════════════│''' #pakai r untuk jadi raw string

camelus = r'''│                                                                       │
│                                       ,,__                            │
│                             ..  ..   / o._)                           │
│                            /--'/--\  \-'/│                            │
│                           /        \_/ / │                            │
│                          .'\  \__\  __.'.'                            │
│                            )\ │  )\ │                                 │
│                           // \\ // \\                                 │
│----------------│         ││_  \\│_  \\_                               │
│    Camelus     │     mrf '--' '--'' '--'                              │
│═══════/\══════════════════════════════════════════════════════════════│''' #pakai r untuk jadi raw string

meowing = r'''│                                                                       │
│                                                                       │
│                   ("`-''-/").___..--''"`-._                           │
│                    `6_ 6  )   `-.  (     ).`-.__.`)                   │
│                   (_Y_.)'  ._   )  `._ `. ``-..-'                     │
│                     _..`--'_..-_/  /--'_.'/                           │
│                    ((((.-''  ((((.'  (((.-' hjw                       │
│                 - - ' ' '     ' ' '   '' - -                          │
│----------------│                                                      │
│     Meowing    │                                                      │
│═══════/\══════════════════════════════════════════════════════════════│''' #pakai r untuk jadi raw string

duo_froggy = r'''│                                                                       │
│                    _  _                     _  _                      │
│                   (.)(.)                   (.)(.)                     │
│               ,-.(.____.),-.           ,-.(.____.),-.                 │
│              ( \ \ '--' / / )         ( \ \ '--' / / )                │
│               \ \ / ,. \ / /           \ \ / ,. \ / /                 │
│                 ) '│ ││ │' ( mrf        ) '│ ││ │' (                  │
│              ()()()'- ()()()'          ()()()'- ()()()'               │
│----------------│                                                      │
│   Duo Froggy   │                                                      │
│═══════/\══════════════════════════════════════════════════════════════│''' #pakai r untuk jadi raw string



data_base_image= [giant_ant,giant_bat,beaverton,camelus,meowing,duo_froggy]

#------------------------ENGINE

def randomizer_image():
    image_choice = random.choice(range(0,len(data_base_image)))
    return image_choice


def format_pertanyaan():
    clear_console()
    monster_approaching()
    bar_atas()
    print(f'''{data_base_image[randomizer_image()]}
      
    {data_base[choosen_number].get("question").center(24)}

|-----------------------------------------------------------------------|

     1.  {data_base[choosen_number].get("option")[0][1] : <10} \t\t\t| 2. {data_base[choosen_number].get("option")[1][1] : <10}

     3.  {data_base[choosen_number].get("option")[2][1] : <10} \t\t\t| 4. {data_base[choosen_number].get("option")[3][1]  : <10}

     ( Q. Call Quo )       

     ( E. Erase Half )
''')
    bar_bawah()



def format_pertanyaan_halfed():
    clear_console()
    halfer()
    bar_atas()
    print(f'''{data_base_image[randomizer_image()]}
      
    {data_base[choosen_number].get("question").center(24)}

|-----------------------------------------------------------------------|

     1.  {data_base[choosen_number].get("option")[0][1] : <10} \t\t\t| 2. {data_base[choosen_number].get("option")[1][1] : <10}

     3.  {data_base[choosen_number].get("option")[2][1] : <10} \t\t\t| 4. {data_base[choosen_number].get("option")[3][1]  : <10}

     ( Q. Call Quo )       
                     

''')
    bar_bawah()



def format_pertanyaan_with_hint_half():
    clear_console()
    halfer()
    bar_atas()
    print(f'''{data_base_image[randomizer_image()]}
      
    {data_base[choosen_number].get("question").center(24)}

|-----------------------------------------------------------------------|

     1.  {data_base[choosen_number].get("option")[0][1] : <10} \t\t\t| 2. {data_base[choosen_number].get("option")[1][1] : <10}

     3.  {data_base[choosen_number].get("option")[2][1] : <10} \t\t\t| 4. {data_base[choosen_number].get("option")[3][1]  : <10}

     ( Q: {data_base[choosen_number].get("hint")} )       
                     
  
 ''')
    bar_bawah()

    

def format_pertanyaan_with_hint():
    clear_console()
    bar_atas()
    print(f'''{data_base_image[randomizer_image()]}
      
    {data_base[choosen_number].get("question").center(24)}

|-----------------------------------------------------------------------|

     1.  {data_base[choosen_number].get("option")[0][1] : <10} \t\t\t| 2. {data_base[choosen_number].get("option")[1][1] : <10}

     3.  {data_base[choosen_number].get("option")[2][1] : <10} \t\t\t| 4. {data_base[choosen_number].get("option")[3][1]  : <10}

     ( Q: {data_base[choosen_number].get("hint")} )      

     ( E. Erase Half )
 
|-----------------------------------------------------------------------|
|      {point_counter}pt\t| Health : {health_bar()}\t|\tQuo :{quo_bar()}\t|
|-----------------------------------------------------------------------|''')
    


def halfer():
    if data_base[choosen_number].get("answer") != "4":
        for i in range(3):
            if data_base[choosen_number].get("option")[i][0] != data_base[choosen_number].get("answer"):
                data_base[choosen_number].get("option")[i] = ("____","____")
            else:
                data_base[choosen_number].get("option")[i] = data_base[choosen_number].get("option")[i]
    elif data_base[choosen_number].get("answer") == "4":
        for i in range(2):
            if data_base[choosen_number].get("option")[i][0] != data_base[choosen_number].get("answer"):
                data_base[choosen_number].get("option")[i-3] = ("____","____")
            else:
                continue

def gameplay():
    global player_health
    
    global point_counter
    global max_health
    global user_name

    global helper
    global max_helper

    global choosen_number
    global win_condition
    global data_base_0
    global data_base

    while True:
        try:
            choosen_number = randomizer()
            if player_health <= 0:
                losing_screen()
                point_counter = 0
                player_health = 10
                win_condition = 10
                helper = 3
                break
            elif point_counter == win_condition:
                winning_screen()
                point_counter = 0
                player_health = 10
                win_condition = 10
                helper = 3
                break
            elif player_health > 0 and helper > 0:
                format_pertanyaan()
                jawaban = input("        What will be your answer? : ").upper()
                if jawaban == "Q":
                    helper -= 1
                    calling_help_hint()
                    format_pertanyaan_with_hint()
                    jawaban = input("        What will be your answer? : ").upper()
                    print("\n\n\n\n\n\n\n")
                    if jawaban == data_base[choosen_number].get("answer"):
                        jawaban_benar()
                        clear_console()
                        data_base.pop(choosen_number)
                        point_counter += 1
                    elif jawaban == "E":
                        helper -= 1
                        calling_help_half()
                        clear_console()
                        format_pertanyaan_with_hint_half()
                        
                        jawaban = input("        What will be your answer? : ").upper()
                        clear_console()
                        if jawaban == data_base[choosen_number].get("answer"):
                            jawaban_benar()
                            clear_console()
                            data_base.pop(choosen_number)
                            point_counter += 1
                        else :
                            jawaban_salah()
                            clear_console()
                            player_health -= 1
                            data_base.pop(choosen_number)
                    else:
                        jawaban_salah()
                        clear_console()
                        player_health -= 1
                        data_base.pop(choosen_number)
                elif jawaban == "E":
                    helper -= 1
                    calling_help_half()
                    clear_console()
                    format_pertanyaan_halfed() 
                    
                    jawaban = input("        What will be your answer? : ").upper()
                    clear_console()
                    if jawaban == data_base[choosen_number].get("answer"):
                        jawaban_benar()
                        clear_console()
                        data_base.pop(choosen_number)
                        point_counter += 1
                    elif jawaban == "Q":
                        helper -= 1
                        calling_help_hint()
                        clear_console()
                        format_pertanyaan_with_hint_half()
                        
                        jawaban = input("        What will be your answer? : ").upper()
                        clear_console()
                        if jawaban == data_base[choosen_number].get("answer"):
                            jawaban_benar()
                            clear_console()
                            data_base.pop(choosen_number)
                            point_counter += 1
                        else :
                            jawaban_salah()
                            clear_console()
                            player_health -= 1
                            data_base.pop(choosen_number)
                    else:
                        jawaban_salah()
                        clear_console()
                        player_health -= 1
                        data_base.pop(choosen_number)
                elif jawaban == data_base[choosen_number].get("answer"):
                    jawaban_benar()
                    clear_console()
                    data_base.pop(choosen_number)
                    point_counter += 1
                else:
                    jawaban_salah()
                    clear_console()
                    player_health -= 1
                    data_base.pop(choosen_number)

            elif player_health > 0 and helper == 0 or helper == -1:
                if helper == -1:
                    helper = 0
                format_pertanyaan()
                jawaban = input("What will be your answer? : ").upper()
                clear_console()
                while True:
                    if jawaban in ("1","2","3","4"):
                        if jawaban == data_base[choosen_number].get("answer"):
                            jawaban_benar()
                            clear_console()
                            data_base.pop(choosen_number)
                            point_counter += 1
                        else :
                            jawaban_salah()
                            clear_console()
                            player_health -= 1
                            data_base.pop(choosen_number)
                        break
                    elif jawaban == "Q" or jawaban == "E":
                        help_zero()
                        format_pertanyaan()
                        jawaban = input("What will be your answer? : ").upper()
                        clear_console()
                    else:
                        print("Pilihan tidak valid")
                        format_pertanyaan()
                        jawaban = input("What will be your answer? : ").upper()
                        clear_console()
        except IndexError:
            print("Pertanyaan Habis")
            break


def game ():
    while True :
        clear_console()
        main_menu()
        clear_console()
        if menu_input == "1":
            clear_console()
            user_detail()
            clear_console()
            storytime()
            loading()
            gameplay()
        elif menu_input == "2":
            setting()
        elif menu_input == "3":
            break
        else:
            print("Your selection is not exist")

game()
