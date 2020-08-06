# Quicksort

## Quick Sort

```py
from typing import List
import random


def partition(nums: List[int], left: int, right: int) -> int:
    pivot = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    i = j = left
    while i < right:
        if nums[i] <= nums[right]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
        i += 1
    nums[i], nums[j] = nums[j], nums[i]
    return j


def randomized_quicksort(nums: List[int], left: int, right: int) -> None:
    if left >= right:
        return
    mid = partition(nums, left, right)
    randomized_quicksort(nums, left, mid - 1)
    randomized_quicksort(nums, mid + 1, right)


def quicksort(nums: List[int]) -> None:
    randomized_quicksort(nums, 0, len(nums) - 1)
```

## Quick Select

```py
from typing import List
import random


def partition(nums: List[int], left: int, right: int) -> int:
    pivot = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    i = j = left
    while i < right:
        if nums[i] <= nums[right]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
        i += 1
    nums[i], nums[j] = nums[j], nums[i]
    return j


def randomized_quickselect(nums: List[int], left: int, right: int,
                           index: int) -> int:
    mid = partition(nums, left, right)
    if mid == index:
        return nums[mid]
    elif mid < index:
        return randomized_quickselect(nums, mid + 1, right, index)
    else:
        return randomized_quickselect(nums, left, mid - 1, index)


def quickselect(nums: List[int], index: int) -> int:
    if index >= len(nums):
        raise IndexError
    return randomized_quickselect(nums, 0, len(nums) - 1, index)
```

## Tests

<iframe height="400px" width="100%" src="https://repl.it/@LucienZhang/quicksort?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
