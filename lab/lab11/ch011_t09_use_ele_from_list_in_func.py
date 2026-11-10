from typing import List


def list_function(x: List[int]) -> List[int]:
    print x[1]


n = [3, 5, 7]
print(list_function(n))
