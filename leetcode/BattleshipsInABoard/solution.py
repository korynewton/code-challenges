class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        '''Using a BFS, find Xs on board'''
        count = 0
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                # if element at index is '.', move on to next index
                if board[i][j] == ".":
                    continue

                # set current element that is currently 'X' to '.'
                # so that we do not traverse over it again
                board[i][j] = '.'

                # BFS using a queue to append adjacent X's
                queue = [(i, j)]
                while queue:
                    l, m = queue.pop(0)

                    for x, y in (l+1, m), (l, m+1):
                        if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'X':
                            queue.append((x, y))
                            board[x][y] = '.'
                count += 1
        return count
