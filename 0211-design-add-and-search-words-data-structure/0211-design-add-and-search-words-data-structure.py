class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, index):
            # Base case: if we have reached the end of the search word
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]
            
            if char == '.':
                # If the character is '.', try searching all possible children nodes
                for child_node in node.children.values():
                    if dfs(child_node, index + 1):
                        return True
                return False
            else:
                # Regular character search
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)