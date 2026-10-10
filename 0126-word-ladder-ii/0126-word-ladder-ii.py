from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}
        found = False

        while queue and not found:
            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]

                        if new_word in wordSet and new_word not in visited:
                            parents[new_word].append(word)

                            if new_word not in level_visited:
                                level_visited.add(new_word)
                                queue.append(new_word)

                            if new_word == endWord:
                                found = True

            visited.update(level_visited)

        if not found:
            return []

        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)
        return result