def Treasure():

    import time


    print(f'Welcome to Treasure Island.\n*{10}')
    time.sleep(1)
    print('You must wonder where you are well friend you are in Tugela River and  your mission is to find the treasure of Umbhutho.')
    time.sleep(0.6)

    print("You're on your journey to the River .Where do you want to go?")
    time.sleep(0.6)
    print('            Type "left" or "right"      '       )
    time.sleep(0.6)
    direction=input()

    if direction == 'right':
        print('\n'* 20)

        print('You were chased by a wild boer!')
        print('''
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
    
''')
        print('Game Over')

    if direction == 'left':
        print('\n'*20)
        print(
            "You were able to walk safely and go through a short cut that allows you to enter You've come to a River.There is an island in the middle of the River\n.")
        print('''
                  _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
                  --------/     '     '   ''')
        print('\n'*10)
        print("You were able to walk safely and go through a short cut that allows you to enter You've come to a River.There is an island in the middle of the River\n.")
        print('What do you want to do?\n')
        print('Wait for the boat or swim across the river')
        time.sleep(0.3)
        print(' Type "wait" for a boat.Type "swim" to swim across the river.  ')
        type_=input()
        if  type_ == 'swim' :
            print('\n' * 10 )
            print(""" 
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
""")
            print('A nasty crocodile ate you while you were swimming!')
            print('Game Over')

        if type_ == 'wait':
            print('\n' *20)
            print('While you were still waiting for the boat ,you found an abandoned building ,as you enter you see 3 doors .You need one to enter.')
            print(""" ______________
                    |\ ___________ /|
                    | |  _ _ _ _  | |
                    | | | | | | | | |
                    | | |-+-+-+-| | |
                    | | |-+-+=+%| | |
                    | | |_|_|_|_| | |
                    | |    ___    | |
                    | |   [___] ()| |
                    
                    | |         ||| |
                    | |         ()| |
                    | |           | |
                    | |           | |
                    | |           | |
                |_|___________|_| ejm        ______________
                                            |\ ___________ /|
                                            | |  _ _ _ _  | |
                                            | | | | | | | | |
                                            | | |-+-+-+-| | |
                                            | | |-+-+=+%| | |
                                            | | |_|_|_|_| | |
                                            | |    ___    | |
                                            | |   [___] ()| |
                                            
                                            | |         ||| |
                                            | |         ()| |
                                            | |           | |
                                            | |           | |
                                            | |           | |
                                            |_|___________|_| ejm
                                             ______________
                                            |\ ___________ /|
                                            | |  _ _ _ _  | |
                                            | | | | | | | | |
                                            | | |-+-+-+-| | |
                                            | | |-+-+=+%| | |
                                            | | |_|_|_|_| | |
                                            | |    ___    | |
                                            | |   [___] ()| |
                                            
                                            | |         ||| |
                                            | |         ()| |
                                            | |           | |
                                            | |           | |
                                            | |           | |
                                            |_|___________|_| ejm """,end='         ')
            print('Which door do you choose?')
            print('Choose between "Red" ,"Blue" and "Yellow" Door')
            choose=input().capitalize()
            if choose== 'Red':
                print("As you entered you got trap for eternity ,tried screaming? well it didn't help")
                print('Game Over')
            if choose == 'Blue':
                print('Got into an empty room')
                print('Game Over')
            if choose == 'Yellow':
                    print('As you entered the room ,you started wondering around the room ')
                    print('Wait what is that?','\n'*10)
                    print("IT'S A TUNNEL!!!!",'\n'*10)
                    print("""
                                            .......
                                      .-'''L   |   J'''-.
                                   .'\     |   |   |     /'.
                                 .'   \    J   |   F    /   '.
                               .'.     \    L  |  J    /     .'.
                              /   '.    \   |  |  |   /    .'   \
                             +-.    '.   \  J  |  F  /   .'    .-+
                            J   '-.   '.  \ .L.|.J. /  .'   .-'   L
                            L__    '-.  '.JHHHHHHHHHh.'  .-'    __J
                           J   ""-__  '-.HHHHHHHHHHHHH.-'  __-""   L
                           |        ""--|HHHHHHHHHHHHH|--""        |
                           |------------HHHHHHHHHHHHHHH------------|
                           |        __--|HHHHHHHHHHHHH|--__        |
                           J   __-""  .-'HHHHHHHHHHHHH'-.  ""-__   F
                            L""    .-'  .TYHHHHHHHHHP'.  '-.    ""J
                            J   .-'   .'  / 'L'T'J' \  '.   '-.   F
                             +-'    .'   /  J  |  L  \   '.    '-+
                              \   .'    /   |  |  |   \    '.   /
                               '.'     /    L  |  J    \     '.'
                                 '.   /    J   |   L    \   .'
                                   './     |   |   |     \.'
                                      '-...L   |   J...-'
                                            '''''''
                hs
""")

                    print( 'Do you crawl or do you just keep on wondering the room?')
                    print('Crawl or Wonder?:')
                    crawl=input().capitalize()
                    if crawl=='Crawl':
                        print("\n"*10)
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

                        print('You win!!!!')
                    if crawl == 'Wonder':
                        print('A group of bandits found you!!')
                        print('You lose !!!\n ')
                        print("Sorry :(")



Treasure()




