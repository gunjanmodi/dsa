import unittest
from solution import MinStack


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
        values = [[], [-2], [0], [-3], [], [], [], []]
        expected = [None, None, None, None, -3, None, 0, -2]

        min_stack = None
        result = []
        for i, operation in enumerate(operations):
            if operation == "MinStack":
                min_stack = MinStack()
                result.append(None)
            elif operation == "push":
                min_stack.push(values[i][0])
                result.append(None)
            elif operation == "getMin":
                result.append(min_stack.getMin())
            elif operation == "pop":
                min_stack.pop()
                result.append(None)
            elif operation == "top":
                result.append(min_stack.top())
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
