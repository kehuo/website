# NP-Hard Problem

## Linear Programming

- Input: Matrix $\mathbf{A}$, vectors $\vec{b}$, $\vec{c}$

- Output: vector $\vec{x}$

- Constraint: $\mathbf{A}\vec{x} \ge \vec{b}$

- Objective Function: Minimize $\vec{c}^\intercal\vec{x}$

For a certain problem, assume we already have an algorithm for it. If we can use this algorithm to solve a Hard Problem in a polynomial calls, we can say the original problem is not easier than the Hard Problem. Thus, it is NP-Hard.

## Hard Problem

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
