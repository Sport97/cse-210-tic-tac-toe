'Tic-Tac-Toe'
'Stephen Port'

options = ["1|", "2|", "3\n", "4|", "5|", "6\n", "7|", "8|", "9\n"]
response_x = []
response_o = []

def main():
    create_board()
    
    while check_win() != True:
        create_choice_x()

        if check_win() == True:
            clear_board()
            break

        create_choice_o()

def create_board():
    board = print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")

def create_choice_x():
    option_x = None

    while option_x == None:
        option_x = int(input("\nYou Are X's. Choose option 1 through 9: "))
        if option_x == 1:
            options[0] = "X|"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 2:
            options[1] = "X|"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 3:
            options[2] = "X\n"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 4:
            options[3] = "X|"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 5:
            options[4] = "X|"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 6:
            options[5] = "X\n"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 7:
            options[6] = "X|"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 8:
            options[7] = "X|"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        elif option_x == 9:
            options[8] = "X\n"
            response_x.append(option_x)
            for selection in options:
                print(selection, end="")
            break
        else:
            print("Wrong Input")

def create_choice_o():
    option_o = None

    while option_o == None:
        option_o = int(input("\nYou Are O's. Choose option 1 through 9: "))
        if option_o == 1:
            options[0] = "O|"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 2:
            options[1] = "O|"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 3:
            options[2] = "O\n"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 4:
            options[3] = "O|"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 5:
            options[4] = "O|"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 6:
            options[5] = "O\n"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 7:
            options[6] = "O|"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 8:
            options[7] = "O|"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        elif option_o == 9:
            options[8] = "O\n"
            response_o.append(option_o)
            for selection in options:
                print(selection, end="")
            break
        else:
            print("Wrong Input")

def check_win():
    solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    if response_x in solutions:
        print("X Won.\n")
        return True
    elif response_o in solutions:
        print("O Won.\n")
        return True
    
    return False

def clear_board():
    options[0] = "1|"
    options[1] = "2|"
    options[2] = "3\n"
    options[3] = "4|"
    options[4] = "5|"
    options[5] = "6\n"
    options[6] = "7|"
    options[7] = "8|"
    options[8] = "9\n"

if __name__ == "__main__":
    main()