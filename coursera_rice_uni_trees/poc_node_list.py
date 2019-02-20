"""
Recursive class definition for a non-empty list of nodes
"""
class NodeList:
    """
    Basic class definition for non-empty lists using recursion
    """
    def __init__(self, value):
        """
        Create a list with one node
        """
        self.value = value
        self.next = None

    def append(self, value):
        """
        Append a node to an existing list of nodes
        """
        if self.next == None:
            new_node = NodeList(value)
            self.next = new_node
        else:
            self.next.append(value)

    def __str__(self):
        """
        Build standard string representation for list
        """
        if self.next == None:
            return "[" + str(self.value) + "]"
        else:
            rest_str = str(self.next)
            rest_str = rest_str[1:]
            return "[" + str(self.value) + ", " + rest_str

def run_example():
    """
    Create some examples
    """
    node_list = NodeList(2)
    node_list.append(3)
    node_list.append(4)
    print(node_list)

    sub_list = NodeList(5)
    sub_list.append(6)

    node_list.append(sub_list)
    print(node_list)

run_example()
