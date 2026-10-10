class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the actual word at the end node to avoid rebuilding it

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Step 1: Build the Trie from the given list of words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, parent_node):
            char = board[r][c]
            current_node = parent_node.children[char]
            
            # If we found a complete word, add it to our results and clear it to prevent duplicates
            if current_node.word:
                result.append(current_node.word)
                current_node.word = None 
                
            # Temporarily mark the current cell as visited by modifying it
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    if board[nr][nc] in current_node.children:
                        dfs(nr, nc, current_node)
                        
            # Restore the cell's original character after backtracking
            board[r][c] = char
            
            # Optimization (Pruning): Remove leaf nodes from the Trie to avoid redundant traversals
            if not current_node.children:
                del parent_node.children[char]

        # Step 2: Kick off DFS from every cell on the board that matches a root trie character
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return result