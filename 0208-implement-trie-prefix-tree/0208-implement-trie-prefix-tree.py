class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
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
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True