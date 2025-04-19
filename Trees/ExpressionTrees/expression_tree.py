from Trees.ExpressionTrees.expression_node import ExpressionNode


class ExpressionTree:

    def __init__(self):
        self.root = None
        self.operators = {"*": 2, "/": 2, "+": 1, "-": 1}
        self.infix = None
        self.postfix = None

    def to_postfix(self, expression):
        output = []
        stack = []

        for item in expression:
            if item.isdigit():
                output.append(item)
            elif item in self.operators:
                while stack and stack[-1] in self.operators and self.operators[stack[-1]] >= self.operators[item]:
                    output.append(stack.pop())
                stack.append(item)
            elif item == "(":
                stack.append(item)
            elif item == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()
        while stack:
            output.append(stack.pop())
        self.postfix = output
        return output

    def to_infix(self, postfix= None):
        if postfix is None:
            postfix = self.postfix
        stack = []
        for item in postfix:
            if item.isdigit():
                stack.append(item)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(f"({left} {item} {right})")
        return stack.pop()

    def evaluate(self):
        return self._evaluate(self.root)

    def _evaluate(self, node):
        if node.left is None and node.right is None:
            if node.val.isdigit():
                return float(node.val)
        left = self._evaluate(node.left)
        right = self._evaluate(node.right)
        if node.val == "*":
            return left * right
        elif node.val == "/":
            return left / right
        elif node.val == "+":
            return left + right
        elif node.val == "-":
            return left - right

    @staticmethod
    def parse(expression):
        output = []
        digits = []
        for char in expression:
            if char.isdigit():
                digits.append(char)
            else:
                if digits:
                    output.append(''.join(digits))
                    digits = []
                if char != ' ':
                    output.append(char)
        if digits:
            output.append(''.join(digits))

        return output

    def build_from_postfix(self, postfix):
        stack = []
        for item in postfix:
            if item.isdigit():
                stack.append(item)
            elif item in self.operators:
                right = ExpressionNode(stack.pop())
                left = ExpressionNode(stack.pop())
                stack.append(ExpressionNode(item, left, right))
        self.root = stack.pop()

def main():
    expression = ExpressionTree()
    infix = expression.parse("((4 * 2) - 5) + 9")
    print(f"\nINFIX: {infix}")
    postfix = expression.to_postfix(infix)
    print(f"\nPOSTFIX: {postfix}")
    print(f"\nPostfix: {postfix} --> Infix: {expression.to_infix(postfix)}")
    expression.build_from_postfix(postfix)
    result = expression.evaluate()
    print(f'\nRESULT: {result}')

if __name__ == '__main__':
    main()
