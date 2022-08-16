import random

class Grattacieli:

    keys: list[int]
    complete_board: list[list[int]]

    @staticmethod
    def create_board():

        complete_board = [[None for c in range(5)] for i in range(5)]

        for row in range(5):
            # First row
            if row == 0:
                numbers = [1,2,3,4,5]
                for i in range(5):
                    random_index = random.randrange(len(numbers))
                    complete_board[0][i] = numbers[random_index]
                    numbers.pop(random_index)
                continue

            # Check available numbers for each column
            available = []
            for c in range(5):
                numbers = [1,2,3,4,5]
                for r in range(5):
                    if complete_board[r][c] != None:
                        numbers.remove(complete_board[r][c])
                if len(numbers) != 0:
                    available.append(numbers)

            # Position each number
            numbers = [1,2,3,4,5]
            for numb in numbers:

                # Find every occurence of number in available
                index = []
                columns_length = max([len(arr) for arr in available])
                for r in range(5):
                    if len(available[r]) != 0:
                        for c in range(columns_length):
                            if available[r][c] == numb:
                                index.append((r,c))

                
                # Find min row occurence
                min = 6 
                for ind in index:
                    if ind[1] < min:
                        min = ind[1]

                # Group up occurences in min row
                available_rows = []
                for r in range(5):
                    if len(available[r]) != 0:
                        if available[r][min] == numb:
                            available_rows.append(r)

                # Min rows

                r_saved = []
                min = 15
                for r in available_rows:
                    if sum(available[r]) == min:
                        r_saved.append(r)
                    elif sum(available[r]) < min:
                        r_saved = []
                        r_saved.append(r)
                        min = sum(available[r]) 

                    

                selection = r_saved[random.randrange(len(r_saved))]

                complete_board[row][selection] = numb

                available[selection] = []

        return complete_board,Grattacieli.calculate_keys(complete_board)

    @staticmethod
    def calculate_keys(complete_board: list[list[int]]) -> list[int]:

        keys = [None for c in range(20)]

        current_key_index = 0
        # TOP
        for board_col_index in range(5):
            max = 0
            num = 0
            for board_row_index in range(5):
                value = complete_board[board_row_index][board_col_index]
                if value > max:
                    max = value
                    num += 1
            keys[current_key_index] = num
            current_key_index += 1

        # RIGHT
        for board_row_index in range(5):
            max = 0
            num = 0
            for board_col_index in range(4,-1,-1):
                value = complete_board[board_row_index][board_col_index]
                if value > max:
                    max = value
                    num += 1
            keys[current_key_index] = num
            current_key_index += 1

        # BOTTOM
        for board_col_index in range(4,-1,-1):
            max = 0
            num = 0
            for board_row_index in range(4,-1,-1):
                value = complete_board[board_row_index][board_col_index]
                if value > max:
                    max = value
                    num += 1
            keys[current_key_index] = num
            current_key_index += 1

        # LEFT
        for board_row_index in range(4,-1,-1):
            max = 0
            num = 0
            for board_col_index in range(5):
                value = complete_board[board_row_index][board_col_index]
                if value > max:
                    max = value
                    num += 1
            keys[current_key_index] = num
            current_key_index += 1

        return keys

    @staticmethod
    def print_empty_grid(keys) -> str:
        print(f"""
         {keys[0]}   {keys[1]}   {keys[2]}   {keys[3]}   {keys[4]}          
       ┌───┬───┬───┬───┬───┐
     {keys[19]} │   │   │   │   │   │ {keys[5]} 
       ├───┼───┼───┼───┼───┤
     {keys[18]} │   │   │   │   │   │ {keys[6]}
       ├───┼───┼───┼───┼───┤
     {keys[17]} │   │   │   │   │   │ {keys[7]}
       ├───┼───┼───┼───┼───┤
     {keys[16]} │   │   │   │   │   │ {keys[8]}
       ├───┼───┼───┼───┼───┤
     {keys[15]} │   │   │   │   │   │ {keys[9]}
       └───┴───┴───┴───┴───┘
         {keys[14]}   {keys[13]}   {keys[12]}   {keys[11]}   {keys[10]}
        """)

    @staticmethod
    def print_solution(keys,complete_board) -> str:
        print(f"""
         {keys[0]}   {keys[1]}   {keys[2]}   {keys[3]}   {keys[4]}          
       ┌───┬───┬───┬───┬───┐
     {keys[19]} │ {complete_board[0][0]} │ {complete_board[0][1]} │ {complete_board[0][2]} │ {complete_board[0][3]} │ {complete_board[0][4]} │ {keys[5]} 
       ├───┼───┼───┼───┼───┤
     {keys[18]} │ {complete_board[1][0]} │ {complete_board[1][1]} │ {complete_board[1][2]} │ {complete_board[1][3]} │ {complete_board[1][4]} │ {keys[6]}
       ├───┼───┼───┼───┼───┤
     {keys[17]} │ {complete_board[2][0]} │ {complete_board[2][1]} │ {complete_board[2][2]} │ {complete_board[2][3]} │ {complete_board[2][4]} │ {keys[7]}
       ├───┼───┼───┼───┼───┤
     {keys[16]} │ {complete_board[3][0]} │ {complete_board[3][1]} │ {complete_board[3][2]} │ {complete_board[3][3]} │ {complete_board[3][4]} │ {keys[8]}
       ├───┼───┼───┼───┼───┤
     {keys[15]} │ {complete_board[4][0]} │ {complete_board[4][1]} │ {complete_board[4][2]} │ {complete_board[4][3]} │ {complete_board[4][4]} │ {keys[9]}
       └───┴───┴───┴───┴───┘
         {keys[14]}   {keys[13]}   {keys[12]}   {keys[11]}   {keys[10]}
        """)

'''
        ┌───┬───┬───┬───┬───┐
      3 │   │   │   │   │   │
        ├───┼───┼───┼───┼───┤
        │   │   │   │   │   │
        ├───┼───┼───┼───┼───┤
        │   │   │   │   │   │
        ├───┼───┼───┼───┼───┤
        │   │   │   │   │   │
        ├───┼───┼───┼───┼───┤
        │   │   │   │   │   │
        └───┴───┴───┴───┴───┘
'''