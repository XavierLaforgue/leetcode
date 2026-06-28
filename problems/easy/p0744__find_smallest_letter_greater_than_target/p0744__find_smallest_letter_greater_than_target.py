from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        for idx in range(length):
            if letters[idx] <= target:
                continue
            else:
                return letters[idx]
        return letters[0]
