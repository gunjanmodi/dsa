class Solution:
    def simplifyPath(self, path: str) -> str: # noqa
        path_array = path.split("/")
        stack = []
        for i in range(len(path_array)):
            sub_path = path_array[i]
            if sub_path == '.' or sub_path == '':
                continue
            elif sub_path == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(sub_path)
        return '/'+'/'.join(stack)
