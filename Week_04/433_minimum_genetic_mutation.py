from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank, v, path = set(bank), {start}, [(start, 0)]
        for w, step in path:
            for s in (w[:i] + cc + w[i + 1 :] for i, _ in enumerate(w) for cc in "ACGT"):
                if s in bank and s not in v:
                    if s == end:
                        return step + 1
                    path.append([s, step + 1])
                    v.add(s)
        return -1

