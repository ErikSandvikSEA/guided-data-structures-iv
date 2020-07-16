class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Call the function `fn` on the value of each node

    # def for_each(self, fn):
    #     fn(self.value)
    #     if self.left is None and self.right is None:
    #         return
    #     else:
    #         if self.left is None:
    #             self.right.for_each(fn)
    #         elif self.right is None:
    #             self.left.for_each(fn)
    #         else:
    #             self.left.for_each(fn)
    #             self.right.for_each(fn)

    # DEPTH FIRST=======================================================
    # lecture alt (recursive)
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # lecture alt (iterative)
    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it there are more nodes to travers
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()

            # add the current node's right child first
            if current.right:
                stack.append(current.right)

            # add the current node's left
            if current.left:
                stack.append(current.left)

            # then call the function
            fn(current.value)


# BREADTH FIRST=======================================================
    def iterative_breadth_first_for_each(self, fn):
        from collections import deque
        # BFT: FIFO
        # we'll use a queue to facilitate the ordering 
        queue = deque()
        queue.append(self)

        # continue to travers so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                fn(current.value)
