class Tree:
    def __init__(self, term, value):
        self.term = term
        self.value = value
        self.children = []
        self.parent = None

    def add_children(self, list):
        self.children += list
        for child in list:
            child.parent = self

    def print_tree(self):
        if self is None:
            return

        if self.term == True:
            self.parent.children += [Tree(False, "доп", self.parent)]

        for node in self.children:
            if node == None:
                return
            node.print_tree()
            print(node.value)
