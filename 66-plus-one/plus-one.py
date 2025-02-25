class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            number = int("".join(map(str, digits)))
            number += 1
            lst = list(map(int, str(number)))
        return lst