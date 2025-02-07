    def postorderTraversal2(self, root):
        if not root:
            return []
        
        res = []
        it_stack = [] # Top of the stack is the end

        curr = root
        it_stack.append(root)

        while it_stack:

            if curr.right:
                it_stack.append(curr.right)

            if curr.left:
                it_stack.append(curr.left)
        
        print(it_stack)