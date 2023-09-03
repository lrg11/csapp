class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            row.sort()
        for z in zip(*grid):
            ans += max(z)
        return ans

# 2399
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        pos = [0] * 26
        for i,d in enumerate(s):
            p = ord(d) - ord('a')
            if pos[p] and i - pos[p] != distance[p]:
                return False
            if not pos[p]:
                pos[p] = i + 1
        return True

# 2400
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if abs(endPos - startPos) > k or abs(endPos - startPos) % 2 != k % 2:
            return 0

        Mod = 10 ** 9 + 7
        # return comb(k, (d+k)//2) % Mod
        @cache
        def f(x: int, left: int) -> int:
            if abs(x - endPos) > left:
                return 0
            if left == 0:
                return 1
            return (f(x + 1, left - 1) + f(x - 1, left - 1)) % Mod
        return f(startPos, k)


# H index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = reversed(sorted(citations))
        h = 0
        for sc in sorted_citations:
            if sc > h:
                h +=1
        return h