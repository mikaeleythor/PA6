class NoneValueException(Exception):
    pass

class WordTree():

    class Node():

        def __init__(self, word=None, parent=None, left=None, right=None):
            self.word = word
            self.parent = parent
            self.left = left
            self.right = right

        def __lt__(self, word):
            """This function compares a Node to a given word"""
            if self.word == None or word == None:
                raise NoneValueException
            else:
                return self.word < word

        def __gt__(self, word):
            """This function compares a Node to a given word"""
            if self.word == None or word == None:
                raise NoneValueException()
            else:
                return self.word > word

        def __eq__(self, word):
            return self.word == word


    def __init__(self):
        self.root = Node('N') # Root node is between values of 'M' and 'N'

    # def insert(self, word):
        # node = self.root
        # if word < node:
            # node = node.left
