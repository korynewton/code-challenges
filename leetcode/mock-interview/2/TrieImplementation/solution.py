class Node:
    def __init__(self, val, isWord=False):
        self.val = val
        self.next = {}
        self.isWord = isWord

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            if char not in current.next:
                current.next[char] = Node(char)
            current = current.next.get(char)
        
        #indicate at last node that it is the end of a word
        current.isWord = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            if char in current.next:
                current = current.next[char]
            else:
                return False
        return current.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char in current.next:
                current = current.next[char]
            else:
                return False
        return True
        
