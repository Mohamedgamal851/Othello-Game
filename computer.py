import copy

class ComputerPlayer:
    def __init__(self, gridObject):
        self.grid = gridObject
    def make_move(self,grid,move, player):
        newGrid = copy.deepcopy(grid)
        swappableDisks = newGrid.getAlloutFlanksDisks(move)
        newGrid.board[move[0]][move[1]] = player
        for disk in swappableDisks:
            newGrid.board[disk[0]][disk[1]] = player
        return newGrid
    def computerHard(self, grid, depth, alpha, beta, player):
        availableMoves = grid.get_valid_moves()
        if depth == 0 or not availableMoves:
            bestMove, bestScore = None, grid.evaluate_board(player - 1)
            return bestMove, bestScore
        if player == 2:  # maximizing player
            bestScore = -float('inf')
            bestMove = None
            for move in availableMoves:
                newGrid = self.make_move(grid, move, player)
                _, value = self.computerHard(newGrid, depth-1, alpha, beta, 1)
                if value > bestScore:
                    bestScore = value
                    bestMove = move
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
            return bestMove, bestScore

        else:  # minimizing player
            bestScore = float('inf')
            bestMove = None
            for move in availableMoves:
                newGrid = self.make_move(grid, move, player)
                _, value = self.computerHard(newGrid, depth-1, alpha, beta, 2)
                if value < bestScore:
                    bestScore = value
                    bestMove = move
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
            return bestMove, bestScore