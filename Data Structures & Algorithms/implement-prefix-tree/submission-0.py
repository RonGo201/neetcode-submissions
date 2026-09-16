class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        i, wordLen = 0, len(word)
        cur = self.root

        while i < wordLen:
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            
            cur = cur.children[word[i]]
            i += 1

        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        i, wordLen = 0, len(word)
        cur = self.root

        while i < wordLen:
            if word[i] not in cur.children:
                return False
            
            cur = cur.children[word[i]]
            i += 1
        
        return cur.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        i, wordLen = 0, len(prefix)
        cur = self.root

        while i < wordLen:
            if prefix[i] not in cur.children:
                return False
            
            cur = cur.children[prefix[i]]
            i += 1
        
        return True
        