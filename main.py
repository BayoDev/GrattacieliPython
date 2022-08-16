from modules.grattacieli import Grattacieli
import os

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    while True:
        cls()
        print('''
          .oooooo.                           .       .                        o8o            oooo   o8o  
         d8P'  `Y8b                        .o8     .o8                        `"'            `888   `"'  
        888           oooo d8b  .oooo.   .o888oo .o888oo  .oooo.    .ooooo.  oooo   .ooooo.   888  oooo  
        888           `888""8P `P  )88b    888     888   `P  )88b  d88' `"Y8 `888  d88' `88b  888  `888  
        888     ooooo  888      .oP"888    888     888    .oP"888  888        888  888ooo888  888   888  
        `88.    .88'   888     d8(  888    888 .   888 . d8(  888  888   .o8  888  888    .o  888   888  
         `Y8bood8P'   d888b    `Y888""8o   "888"   "888" `Y888""8o `Y8bod8P' o888o `Y8bod8P' o888o o888o

                                        Created by Giulio Venturini                                                                                       
        ''')
        print('\n 1) Generate schema \n 2) Exit')
        try:
            choice = int(input('\n Option >> '))
        except:
            choice == -1
        if choice == 1:
            phrase = ''
            schema, keys = Grattacieli.create_board()
            while phrase!='solution' and phrase!='exit':
                cls()
                Grattacieli.print_empty_grid(keys)
                phrase = input("Write 'solution' to show solution or 'exit' to quit: ")
            if phrase == 'exit':
                continue
            cls()
            Grattacieli.print_solution(keys,schema)
            input('\n Press any key to continue...')
        if choice == 2:
            return
            

if __name__ == '__main__':
    main()