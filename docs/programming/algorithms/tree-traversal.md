# Tree Traversal

|            Item             |     DFS      |      BFS      |
| :-------------------------: | :----------: | :-----------: |
|       Data Structure        |    Stack     |     Queue     |
|        Vertex Order         | one sequence | two sequences |
|       Time Complexity       |    $O(n)$    |    $O(n)$     |
|      Space Complexity       | $O(height)$  |  $O(width)$   |
| Worst-case Space Complexity |    $O(n)$    |    $O(n)$     |

Example

![Binary Tree](@assets/img/algorithms/tree/binary_tree.png)

Tree Node definition

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## DFS

```py
def dfs(root: TreeNode):
    # stack
    stack = [root]
    while stack:
        node = stack.pop()
        # do something
        print(node.val)
        if node.left:
            # do something
            stack.append(node.left)
        if node.right:
            # do something
            stack.append(node.right)
```

## BFS

```py
from collections import deque

def bfs(root: TreeNode):
    # queue
    q = deque([root])
    while q:
        node = q.popleft()
        # do something
        print(node.val)
        if node.left:
            # do something
            q.append(node.left)
        if node.right:
            # do something
            q.append(node.right)
```

## Level Order Traversal

```py
from collections import deque

def lot(root: TreeNode) -> int:
    # queue
    q = deque([root])
    lv = 0
    while q:
        lv += 1
        print(f'level {lv}')
        for _ in range(len(q)):
            node = q.popleft()
            # do something
            print(node.val)
            if node.left:
                # do something
                q.append(node.left)
            if node.right:
                # do something
                q.append(node.right)
    return lv
```

## Preorder Traversal

```py
def preorder(root: TreeNode):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
```

```py
from typing import List

def preorder_without_recursion(root: TreeNode) -> List[int]:
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        ans.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return ans
```

## Inorder Traversal

```py
def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

```py
from typing import List

def inorder_without_recursion(root: TreeNode) -> List[int]:
    ans = []
    stack = []
    now = root

    while stack or now:
        if now:
            stack.append(now)
            now = now.left
            continue
        else:
            node = stack.pop()
            ans.append(node.val)
            now = node.right
    return ans
```

## Postorder Traversal

```py
def postorder(root: TreeNode):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

```py
from typing import List

def postorder_without_recursion(root: TreeNode) -> List[int]:
    if not root:
        return []

    ans = []
    stack = []
    now = root

    while True:
        while now:
            if now.right:
                stack.append(now.right)
            stack.append(now)
            now = now.left
        now = stack.pop()
        if stack and stack[-1] is now.right:
            stack.pop()
            stack.append(now)
            now = now.right
        else:
            ans.append(now.val)
            now = None
        if not stack:
            break
    return ans
```

## Tests

<iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/binary-tree-traversal?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
