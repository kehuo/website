# Segment Tree

## Array Representation of Binary Tree

For a binary tree with `n` nodes, it can be represented by an array `T`.

1. The index of `T` is from 1 to n, `T[0]` is empty
1. The root of the tree is located at `T[1]`
1. The parent nodes are located at `T[:n//2+1]`
1. The leaf nodes are located at `T[n//2+1:]`
1. for `1 <= i <= n//2`, its children are located at `T[2*i]` and `T[2*i+1]` (may not exist)
1. for `2 <= i <= n`, its parent node is located at `T[i//2]`

## Implementation

for an array of length n, we need 2n space to store the segment tree, which contains 2n-1 values.

| Algorithm | Complexity  |
| :-------: | :---------: |
|   Space   |   $O(n)$    |
| Construct |   $O(n)$    |
|  Update   | $O(\log n)$ |
|   Query   | $O(\log n)$ |

:::: tabs

::: tab python

```py
from typing import List


class SegmentTree(object):
    def __init__(self, arr: List[int]) -> None:
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        for i in range(self.n - 1, 0, -1):
            # The merging may be different for different problems
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, pos: int, value: int) -> None:
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            self.tree[pos >> 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def query(self, l: int, r: int) -> int:
        # get sum on interval [l, r]
        res = 0
        l += self.n
        r += self.n

        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1

        return res
```

:::

::: tab java

```java
class SegmentTree {
    int n;
    int[] tree;

    SegmentTree(int[] arr) {
        n = arr.length;
        tree = new int[2 * n];
        for (int i = 0; i < n; i++) {
            tree[i + n] = arr[i];
        }
        for (int i = n - 1; i > 0; i--) {
            // The merging may be different for different problems
            tree[i] = tree[i << 1] + tree[i << 1 | 1];
        }
    }

    void update(int pos, int value) {
        pos += n;
        tree[pos] = value;
        while (pos > 1) {
            tree[pos >> 1] = tree[pos] + tree[pos ^ 1];
            pos >>= 1;
        }
    }

    int query(int l, int r) {
        int res = 0;
        l += n;
        r += n;
        while (l <= r) {
            if (l % 2 == 1) {
                res += tree[l];
                l++;
            }
            if (r % 2 == 0) {
                res += tree[r];
                r--;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
}
```

:::

::::

## Tests

:::: tabs

::: tab python

<iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/segment-tree?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

:::

::: tab java

<iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/segment-tree-java?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

:::

::::
