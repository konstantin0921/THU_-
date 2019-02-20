"""
Python class definition for creation and
evaluation of arithmetic expressions
"""

# import Tree class definition
import poc_tree

# Use dictionary of lambdas to abstract function definitions

OPERATORS = {
    "+" : (lambda x, y : x + y),
    "-" : (lambda x, y : x - y),
    "*" : (lambda x, y : x * y),
    "/" : (lambda x, y : x / y),
    "//" : (lambda x, y : x // y),
    "%" : (lambda x, y : x % y)
}

class ArithmeticExpression(poc_tree.Tree):
    """
    Basic operations on arithmetic expressions
    """
    def __init__(self, value, children, parent=None):
        """
        Create an arithmetic expression as a tree
        """
        poc_tree.Tree.__init__(self, value, children)

    def __str__(self):
        """
        Generate a string representation for an arithmetic expression
        """
        if len(self.children) == 0:
            return str(self.value)

        ans = "("
        ans += str(self.children[0])
        ans += str(self.value)
        ans += str(self.children[1])
        ans += ")"
        return ans

    def evaluate(self):
        """
        Evaluate the arithmetic expression
        """
        if len(self.children) == 0:
            if "." in self.value:
                return float(self.value)
            else:
                return int(self.value)
        else:
            return OPERATORS[self.value](self.children[0].evaluate(), self.children[1].evaluate())


def run_examples():
    """
    Create and evaluate some examples of arithmetic expressions
    """

    one = ArithmeticExpression("1", [])
    two = ArithmeticExpression("2", [])
    three = ArithmeticExpression("3", [])
    print(one)
    print(one.evaluate())

    one_plus_two = ArithmeticExpression("+", [one, two])
    print(one_plus_two)
    print(one_plus_two.evaluate())

    one_plus_two_times_three = ArithmeticExpression("*", [one_plus_two, three])
    print(one_plus_two_times_three)

    # import poc_draw_tree
    # poc_draw_tree.TreeDisplay(one_plus_two_times_three)
    print(one_plus_two_times_three.evaluate())

if __name__ == "__main__":
    run_examples()
