class NoneValueException(Exception):
    pass


class WordTree():

    # The WordTree class is a dictionary

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
                return self.word > word

        def __gt__(self, word):
            """This function compares a Node to a given word"""
            if self.word == None or word == None:
                raise NoneValueException()
            else:
                return self.word > word

        def __eq__(self, word):
            return self.word == word


    def __init__(self):
        self.root = self.Node('N') # Root node is between values of 'M' and 'N'

    def insert_recursive(self, node, word):
        """This function takes in a Word() object and adds it to the BST"""
        if node == None:
            return self.Node(word)
        else:
            if node == word:
                return node
            elif node < word:
                node.right = self.insert_recursive(node.right, word)
            else:
                node.left = self.insert_recursive(node.left, word)

    def insert(self, word):
        self.insert_recursive(self.root, word)

    def contains(self, word):
        