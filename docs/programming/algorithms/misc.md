# Misc

## Trie

:::: tabs

::: tab python

```py
from collections import defaultdict

Trie = lambda: defaultdict(Trie)
trie = Trie()
for row in ['abc', 'ab', 'abcd']:
    now = trie
    for ch in row:
        now = now[ch]
```

:::

::: tab java

```java

```

:::

::::

## i2b & b2i

:::: tabs

::: tab python

```py
print('{:0>10b}'.format(37))
print(int('0000100101', 2))
```

:::

::: tab java

```java

```

:::

::::

## Tensor

:::: tabs

::: tab python

```py
def tensor(shape, fill=0):
    if len(shape) == 1:
        return [fill for _ in range(shape[0])]
    else:
        return [tensor(shape[1:], fill) for _ in range(shape[0])]
```

:::

::: tab java

```java

```

:::

::::

## Tests

:::: tabs

::: tab python

<iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/misc?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

:::

::: tab java

<!-- <iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/misc-java?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> -->

:::

::::
