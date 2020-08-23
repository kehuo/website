# Algorithms

Algorithm is the soul of programming, and the only way to learn it well is to practice it well. The chart below shows my [LeetCode](https://leetcode.com/lucienzhang/) Contest Rating History. Fine me on [LeetCode](https://leetcode.com/lucienzhang/) and [LeetCode-CN](https://leetcode-cn.com/u/lucien_z/)!

<LeetCode />

[comment]: # "# todo: 分三、四块，基础算法，启发式算法，np-hard问题，数学，右下角copy不float"
[comment]: # "# todo: merge sort, longest common subsequence, longest palindromic subsequence, longest palindromic substring, 正序对，逆序对，树状数组(bit)，单调队列，单调栈，回溯，dp， rmq, fenwich tree，SegmentTree, 环检测， 霍夫曼树， 斐波那契堆，卡塔兰数,floyd, 洗牌算法, 马拉车，KMP"

<!-- ## Array Representation of Binary Tree starting from 0

For a binary tree with `n` nodes, it can be represented by an array `T`.

1. The index of `T` is from 0 to n-1
1. The root of the tree is located at `T[0]`
1. The parent nodes are located at `T[:n//2]`
1. The leaf nodes are located at `T[n//2:]`
1. for `i < n//2`, its children are located at `T[2*i+1]` and `T[2*i+2]` (may not exist)
1. for `0 < i < n`, its parent node is located at `T[(i-1)//2]` -->

## Fundamental Algorithms

This section includes an introduction to some commonly used data structures. Algorithms such as sorting and searching are presented in the form of Python best practices.

## NP-Hard Problems and Advanced Algorithms

This part contains an introduction to the NP-hard problems and some advanced algorithms, including approximation algorithms, online algorithms and other heuristic algorithms.

[comment]: # "# todo: thanks to vorapong"

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
