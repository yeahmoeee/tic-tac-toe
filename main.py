from tictactoe import *

def main():
    board = tictactoe([0,0,0,0,0,0,0,0,0])
    print("Computer: X VS. You: O")
    first = input("Play first (Y/N) : ")
    if first.lower() == "y":
        player = 1
    else:
        player = 0
    for i in range(9):
        if board.check_game() != 2:
            break
        if (i + player) % 2 == 0:
            count = 0
            board.ai_turn()
            print("Count:", count)
        else:
            board.drawboard()
            board.human_turn()
    result = board.check_game()
    if result == 0:
        board.drawboard()
        print("Draw!")
    elif result == 1:
        board.drawboard()
        print("AI(X) Wins! Human(O) Loses!")
    elif result == -1:
        board.drawboard()
        print("Human(O) Wins! AI(X) Loses!")

main()