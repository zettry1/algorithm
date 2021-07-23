 def preorderTraversal(self, root):
        if root is None:
            return []
        stack, output = [root],[]

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

        return output