class tictactoe:
    def __init__(self,board):
        self.board = board
        self.winning_pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def draw_board(self):
        print("Current state: \n\n")
        for i in range(0,9):
            if self.board[i] == 0:
                print("- ", end = " ")
            elif self.board[i] == 1:
                print("X ", end =  " ")
            elif self.board[i] == -1:
                print("O ", end = " ")
            if (i+1) % 3 == 0:
                print("\n")
        print("\n")
    
    def check_game(self):
        for i in range(8):
            if self.board[self.winning_pos[i][0]] != 0 and\
               self.board[self.winning_pos[i][0]] == self.board[self.winning_pos[i][1]] and\
               self.board[self.winning_pos[i][0]] == self.board[self.winning_pos[i][2]]:
               return self.board[self.winning_pos[i][2]]

        if any(element == 0 for element in self.board): return 2
        return 0 
    
    def human_turn(self):
        pos = int(input("Enter O's position [1 to 9]: "))
        if self.board[pos-1] != 0:
            print("Illegal Move!")
            exit(0)
        self.board[pos-1] = -1
    
    def minimax_search(self,player):
        result = self.check_game()
        if result != 2:
            return result 
        scores = []
        for i in range(0,9):
            if self.board[i] == 0:
                self.board[i] = player
                scores.append(self.minimax_search(player * -1))
                self.board[i] = 0
        return max(scores) if player == 1 else min(scores)
    
    def ai_turn(self):
        pos = -1
        max_value = -2
        for i in range(0,9):
            if self.board[i] == 0:
                self.board[i] = 1
                score = self.minimax_search(-1)
                self.board[i] = 0
                if score > max_value:
                    max_value = score
                    pos = i 
        self.board[pos] = 1







        
        
            
