# Minimum Spanning Tree

Example

![Graph](@assets/img/algorithms/graph/weighted-graph.png)

Adjacency Matrix

|                                         |                0                 |                1                 |                2                 |                3                 |                4                 |                5                 |                6                 |
| :-------------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: |
| <span style="font-weight:bold">0</span> |                0                 | <span style="color:red">1</span> | <span style="color:red">3</span> |                0                 |                0                 |                0                 |                0                 |
| <span style="font-weight:bold">1</span> | <span style="color:red">1</span> |                0                 | <span style="color:red">1</span> | <span style="color:red">5</span> |                0                 |                0                 |                0                 |
| <span style="font-weight:bold">2</span> | <span style="color:red">3</span> | <span style="color:red">1</span> |                0                 |                0                 | <span style="color:red">1</span> |                0                 |                0                 |
| <span style="font-weight:bold">3</span> |                0                 | <span style="color:red">5</span> |                0                 |                0                 | <span style="color:red">2</span> |                0                 |                0                 |
| <span style="font-weight:bold">4</span> |                0                 |                0                 | <span style="color:red">1</span> | <span style="color:red">2</span> |                0                 | <span style="color:red">4</span> |                0                 |
| <span style="font-weight:bold">5</span> |                0                 |                0                 |                0                 |                0                 | <span style="color:red">4</span> |                0                 | <span style="color:red">2</span> |
| <span style="font-weight:bold">6</span> |                0                 |                0                 |                0                 |                0                 |                0                 | <span style="color:red">2</span> |                0                 |

## Prim's Algorithm

Works fine even with negative weights

```py
from heapq import heappop, heappush
from typing import List

def prim(matrix) -> List[List[int]]:
    # optimized by heap
    n = len(matrix)
    ans = [[0] * n for _ in range(n)]

    h = [(0, 0, 0)]  # weight, node, pre
    visited = set()
    while h:
        weight, cur, pre = heappop(h)
        if cur in visited:
            continue
        visited.add(cur)
        ans[cur][pre] = weight
        ans[pre][cur] = weight
        for i, w in enumerate(matrix[cur]):
            if w > 0 and i not in visited:
                heappush(h, (w, i, cur))
    return ans
```

[comment]: # "# todo: 加改进版heap"
[comment]: # "# todo: 加复杂度分析"

## Kruskal's Algorithm

## Tests

<iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/mst?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
