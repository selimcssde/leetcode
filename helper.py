from queue import deque

null = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def deserialize(arr):
        if not arr:
            return None
        nodes = [TreeNode(x) if x is not None else None for x in arr]
        root = nodes[0]
        q = deque([root])
        n = len(arr)
        i = 1
        while q:
            node = q.popleft()
            if i < n and nodes[i]:
                q.append(nodes[i])
                node.left = nodes[i]
            i += 1
            if i < n and nodes[i]:
                q.append(nodes[i])
                node.right = nodes[i]
            i += 1
        return root
    
    @staticmethod
    def serialize(root):
        if not root:
            return []
        q = deque([root])
        arr = [root.val]
        while q:
            node = q.popleft()
            if node.left:
                arr.append(node.left.val)
                q.append(node.left)
            else:
                arr.append(None)
            if node.right:
                arr.append(node.right.val)
                q.append(node.right)
            else:
                arr.append(None)
        while arr[-1] is None:
            arr.pop()
        return arr




