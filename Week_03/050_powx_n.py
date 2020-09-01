class Solution:
    def pow(x, n):
        def quickMul(N):
            if N == 0:
                return 1

            ans = 1
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute
                
                x_contribute *= x_contribute
                N //= 2

            return ans

        return quickMul(n) if n >= 0 else 1 / quickMul(-n)
            