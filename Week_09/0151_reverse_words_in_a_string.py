class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.strip().split(" ")
        ans = []
        for i in range(len(li) - 1, -1, -1):
            if li[i] != "":
                ans.append(li[i])
        return " ".join(ans)

