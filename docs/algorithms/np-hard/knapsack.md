# Knapsack Problem

The **knapsack problem** is a problem in [combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization): Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size [knapsack](https://en.wikipedia.org/wiki/Knapsack) and must fill it with the most valuable items. The problem often arises in [resource allocation](https://en.wikipedia.org/wiki/Resource_allocation) where the decision makers have to choose from a set of non-divisible projects or tasks under a fixed budget or time constraint, respectively.[^knapsack]

[^knapsack]: https://en.wikipedia.org/wiki/Knapsack_problem

## Simplified Version

Suppose that you are in an all-you-can-eat strawberry farm, where you can have an unlimited amount of strawberry, but when you decide to eat a strawberry, you have to each a whole of it. We have the following optimization model, because we want to eat the maximum amount of strawberry.

- Input:
  - Positive integer $n$ (number of strawberries)
  - Positive real numbers $w_1,...,w_n$ (weight of each strawberry)
  - Positive real number $W$ (maximum weight of strawberry that we can eat)
  - Assumption: $w_1 \le w_2 \le ... \le w_n$
- Output: Set $S \subseteq \{1,...,n\}$ (set of strawberries we eat)
- Constraint: $\sum\limits_{i\in S} w_i \le W$
- Objective Function: Maximize $\sum\limits_{i\in S} w_i$

### Algorithm

---

<Pseudo>
    \begin{algorithm}
    \begin{algorithmic}
      \STATE $S \gets \varnothing$
      \FOR{$j = 1$ \TO $n$}
        \IF{$\sum\limits_{i\in S} w_i + w_j\le W$}
          \STATE $S \gets S \cup \{j\}$
        \ELSE
          \IF{$w_j \ge \sum\limits_{i\in S} w_i$}
            \STATE $S \gets \{j\}$
          \ENDIF
          \STATE \textbf{break}
        \ENDIF
      \ENDFOR
      \RETURN $S$
    \end{algorithmic}
    \end{algorithm}
</Pseudo>

---

Here we assume that for all $i$, $w_i \le W$

If this assumption doesn't hold, we can just pick those over-weight out beforehand.

This is a 0.5-approximation algorithm, i.e., $SOL \ge 0.5 \ OPT$ for any input.

### proof

---

1. $OPT \le W$

2. if $\sum\limits_{i=1}^{n} w_i \le W$, i.e., the loop never break, then

   $$SOL = OPT$$

   Otherwise,

   $$\text{weight sum of previously chosen strawberries} + \text{weight of last one} \ge W$$

   Thus, either $\text{weight sum of previously chosen strawberries} \ge 0.5W$ or $\text{weight of last one} \ge 0.5W$, we pick the larger one of them, so $SOL \ge 0.5W$

3. $SOL \ge 0.5W \ge 0.5 \ OPT$

---
