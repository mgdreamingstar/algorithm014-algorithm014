from typing import List


def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        digits[i] %= 10
        if digits[i] != 0:
            return digits

    digits.insert(0, 1)
    return digits