"""
You probably played Snakes and Ladders when you were a kid. Since it's been a while, let's review the rules:

Each player puts their counter on the start position.
Roll the dice. Move your counter forward the number of spaces shown on the dice.
If your counter lands at the bottom of a ladder, you must move up to the top of the ladder.
If your counter lands on the head of a snake, you must slide down to the bottom of the snake.
The first player to get to the finish position is the winner.
We will use a standard six-sided dice.

You are given the length of the gameboard boardSize, a list of all the snakes, where snakes[i] = [a, b] means the snake with its head on position a and its tail on position b, and a list of all the ladders, where ladders[i] = [a, b] means the ladder with its bottom on position a and its top on position b. Return the length of the shortest possible path between the start (cell 1) and finish (cell boardSize) positions of the game.

Example

For boardSize = 30, snakes = [[27, 1], [21, 9], [17, 4], [19, 7]], and ladders = [[11, 26], [3, 22], [5, 8], [20, 29]], the output should be
shortestSnakesAndLadders(boardSize, snakes, ladders) = 3.
"""
from collections import deque

def shortestSnakesAndLadders(boardSize, snakes, ladders):
    board = [-1] * boardSize
    
    for ladder in ladders:
        board[ladder[0] - 1] = ladder[1]
    
    for snake in snakes:
        board[snake[0] - 1] = snake[1] 
    
    n = len(board)
    target = len(board) - 1
    q = deque([(0, 0)])
    seen = set()

    while q:
        ind, steps = q.popleft()
        
        if ind == target:
            return steps

        for move in [1, 2, 3, 4, 5, 6]:
            n_ind = ind + move

            if n_ind < n and n_ind not in seen:
                seen.add(n_ind)

                if board[n_ind] == -1:
                    q.append((n_ind, steps+1))
                    
                else:
                    q.append((board[n_ind]-1, steps+1))
        
    return -1
    