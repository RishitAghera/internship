from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def path_from_root(self, to_node):
        paths = [[self]]
        while paths:
            current = paths.pop()
            if current[-1].label == to_node:
                return current

            for child in current[-1].children:
                paths.append(current + [child])

        raise ValueError("Missing node.")

    def from_pov(self, from_node):
        path = self.path_from_root(from_node)
        tree = path.pop()
        current = tree

        while path:
            node = path.pop()
            node.children.remove(current)
            current.children.append(node)
            current = node

        return tree

    def path_to(self, from_node, to_node):
        return [node.label for node
                in self.from_pov(from_node).path_from_root(to_node)]