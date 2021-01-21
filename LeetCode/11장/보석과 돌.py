import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = collections.Counter(stones)
        cnt = 0
        for stone in stone_dict:
            if stone in jewels:
                cnt += stone_dict[stone]
        return cnt
