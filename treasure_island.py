def Treasure() :
    import time

    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    ******************************************************************************* ''')

    print('Welcome to Treasure Island.\n')
    time.sleep(1)
    print('Your mission is to find the treasure.')
    time.sleep(0.6)

    print("You're at a cross road.Where do you want to go?")
    time.sleep(0.6)
    print('            Type "left" or "right"      '       )
    time.sleep(0.6)
    direction=input()

    if direction == 'right':
        print('Game Over')

    if direction == 'left':
        print("You've come to a lake.There is an island in the middle of the lake.")
        time.sleep(0.3)
        print('   Type "wait" for a boat.Type "swim" to swim across.  ')
        type_=input()
        if  type_ == 'swim' :
            print('Game Over')
        if type_ == 'wait':
            print('Which door?')
            print('   Choose between "Red" ,"Blue" and "Yellow" Door')
            choose=input().capitalize()
            if choose== 'Red':
                print('Game Over')
            if choose == 'Blue':
                print('Game Over')
            if choose == 'Yellow':

                print('You win!!!!')

Treasue()


