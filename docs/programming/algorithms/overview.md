# Algorithms

Algorithm is the soul of programming, and the only way to learn it well is to practice it well. The chart below shows my [LeetCode](https://leetcode.com/lucienzhang/) Contest Rating History. Fine me on [LeetCode](https://leetcode.com/lucienzhang/) and [LeetCode-CN](https://leetcode-cn.com/u/lucien_z/)!

<LeetCode />

[comment]: # "# todo: 分三、四块，基础算法，启发式算法，np-hard问题，数学，右下角copy不float"
[comment]: # "# todo: merge sort, longest common subsequence, longest palindromic subsequence, longest palindromic substring, 正序对，逆序对，树状数组(bit)，st表，可持久化线段树，单调队列，单调栈，回溯，dp， rmq, fenwich tree，SegmentTree, 环检测， 霍夫曼树， 斐波那契堆，卡塔兰数,floyd, 洗牌算法, 马拉车，KMP，关联数组 多重关连数组，双端队列，双端优先队列，多重集，环形缓冲器，哈希数组树，稀疏矩阵，关联表，跳跃列表（跳表），松散链表异或链表，AA树，伸展树，左偏树，二项堆，R树 R*树R+树Hilbert R树，哈希树（墨克树），二元决策图，确定性非循环有限自动机，ac自动机，二分图的最大匹配、完美匹配和匈牙利算法，morris遍历, 最近公共祖先（LCA）问题(Tarjan's off-line lowest common ancestors algorithm )、双连通分量 问题, Tarjan 算法, Splay, Toptree, 欧拉通路，哈密顿回路，网络流，树分治，kd树，树链剖分，动态树，树套树, 原来repo中的算法，lcs等。https://blog.csdn.net/u012161726/article/details/100716483，数字进制转换。string四则运算，快速幂，除法逆元：拓展欧几里得、费马小定理、线性递推,同余定理；欧拉定理；孙子定理"
[comment]: # "# todo: https://oi-wiki.org/"
[comment]: # "# todo: https://www.geeksforgeeks.org/"

<!-- ## Array Representation of Binary Tree starting from 0

For a binary tree with `n` nodes, it can be represented by an array `T`.

1. The index of `T` is from 0 to n-1
1. The root of the tree is located at `T[0]`
1. The parent nodes are located at `T[:n//2]`
1. The leaf nodes are located at `T[n//2:]`
1. for `i < n//2`, its children are located at `T[2*i+1]` and `T[2*i+2]` (may not exist)
1. for `0 < i < n`, its parent node is located at `T[(i-1)//2]` -->

## Fundamental Algorithms

This section includes an introduction to some commonly used data structures. Algorithms such as sorting and searching are presented in the form of the best practices.

## NP-Hard Problems and Advanced Algorithms

This part contains an introduction to the NP-hard problems and some advanced algorithms, including approximation algorithms, online algorithms and other heuristic algorithms. Part of the content here is derived from the courses given by [Dr. Vorapong Suppakitpaisarn](http://www.vorapong-sup.net/)

### Linear Programming

Linear programming (LP, also called linear optimization) is a method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships.

- Input: Matrix $\mathbf{A}$, vectors $\vec{b}$, $\vec{c}$

- Output: vector $\vec{x}$

- Constraint: $\mathbf{A}\vec{x} \ge \vec{b}$

- Objective Function: Minimize $\vec{c}^\intercal\vec{x}$

For a certain problem, assume we already have an algorithm for it. If we can use this algorithm to solve a Hard Problem in a polynomial calls, we can say the original problem is not easier than the Hard Problem. Thus, it is NP-Hard.

### Hard Problem

In computational complexity theory, NP-hardness (non-deterministic polynomial-time hardness) is the defining property of a class of problems that are informally "at least as hard as the hardest problems in NP".

1. Satisfiability Problem

   - Input: A logic circuit that has two levels. First level is OR gate, and second level is AND gate. One input can enter more than one different OR gates. There might be NOT gate in front of OR gate.

   - Output: Yes or No
   - Constraint: Yes if it's possible to make the whole circuit output "true". Otherwise, No.

2. K-clique problem

   To find a full-connected subgraph with n nodes in a graph.

   - Input: Set $V$, set $E\subseteq\{\{u,v\} \mid u,v \in V\}$, integer $k$
   - Output: Yes or No
   - Constraint: Yes, if there is a set $S\subseteq V$, such that $|S|=k$, and $\{v_1, v_2\} \in E$ for all $v_1,v_2 \in S$. Otherwise, No.

3. K-most representative skyline operator problem

### Approximation Algorithms

Approximation algorithms are efficient algorithms that find approximate solutions to optimization problems (in particular NP-hard problems) with provable guarantees on the distance of the returned solution to the optimal one. [^approximation] There are two commonly used schemas for approximation algorithms, greedy based algorithm ([Knapsack Problem](./knapsack.md)) and deterministic rounding ([Vertex Cover Problem](./vertex-cover.md)).

[^approximation]: Williamson, D. P., & Shmoys, D. B. (2011). The design of approximation algorithms. Cambridge university press.

[comment]: # "# todo: inapproximability, online algorithm, dominating set problem, net optimization"
[comment]: # "# todo: Heuristic Algorithms, simple Heuristic Algorithms, meta-Heuristic Algorithms, hyper-Heuristic Algorithms"
