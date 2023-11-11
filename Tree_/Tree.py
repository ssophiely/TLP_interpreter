from Tree_.NodeListener import current_node


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

        if self.term:
            self.parent.add_children([Tree(False, "доп")])

        for node in self.children:
            if node is None:
                return
            node.print_tree()
            print(node.value)

    def check_root_left_right(self):
        if self is None:
            return

        print(self.value)
        current_node(self)
        for child in self.children:
            child.check_root_left_right()
