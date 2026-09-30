class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def backtrack(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            if board[row][col] != word[index]:
                return False

            # Mark this cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Check up, down, left, right
            found = (
                backtrack(row - 1, col, index + 1) or
                backtrack(row + 1, col, index + 1) or
                backtrack(row, col - 1, index + 1) or
                backtrack(row, col + 1, index + 1)
            )

            # Restore the cell
            board[row][col] = temp

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False