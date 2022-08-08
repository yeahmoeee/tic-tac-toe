# Tic-Tac-Toe Using Minimax

Tic-Tac-Toe (also known as Noughts and Crosses) is a paper-and-pencil game for two players, who take turns marking the spaces in a 3 x 3 grid. The player who succeds in placing three of their marks in a diagonal, horizontal, or vertical line is the winner. 


## A Naïve Approach to the Game

First, if there is a move that will win the game, play it.\
If not, check if there is a move that will block a win from the opposing player. If so, place your marker in the blocking spot.\
Otherwise, just place your marker in a random empty cell.\
The AI may not play optimally in this case.\

## Algorithmic Game Theory Approach to the Game

Minimax is a recursive algorithm which is used to choose an optimal move for a player assuming that the other player is also playing optimally. In minimax, the two players are called maximizer (the AI player of the game) and minimizer (the Human player of the game)
, and define a scoring method from the view of the maximizer. The maximizer tries to maximize the score while the minimizer tries to minimize the score of the AI player.

![Tic_tac_toe svg](https://user-images.githubusercontent.com/76827587/183385171-41c689db-c97a-4ae8-aac6-46495ab98717.png)


This algorithm only works on game that has perfect information, is zero-sum and deterministic. 

Steps of the minimax algorithm:
1. Construct the complete game tree
2. Apply the utility function to each terminal state. In our case, our utility function is defined in the perspective of AI; win = +1, loss = - 1 and draw = 0.
3. Beginning with the terminal states, determine the utility of the predecessor nodes as follows; if Node is a minimizer, value is the minimum of the children nodes, but if Node is a maximizer, value is the maximum of the children nodes.
4. From the initial state (i.e., root of the game tree), maximizer chooses the move that leads to the highest value.

![1_BQVKAxmorPGfwAjVz1bI7A](https://user-images.githubusercontent.com/76827587/183385265-310dd32c-a21f-4f64-ba2a-4f7ed8cfbdff.png)

    






