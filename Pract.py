"""
Count permutations of [1, 2, ..., m] that have exactly n inversions.
Answer modulo 10^9 + 7.
"""

MOD = 10**9 + 7


def solution(m: int, n: int) -> int:
    # Can't have more inversions than all pairs (reverse sorted)
    max_inv = m * (m - 1) // 2
    if n > max_inv:
        return 0

    # dp[j] = number of permutations of {1, ..., i} with exactly j inversions
    # We only need the current row; build it from the previous one each time
    dp = [0] * (n + 1)
    dp[0] = 1  # one permutation of 0 elements, 0 inversions

    for i in range(1, m + 1):
        new_dp = [0] * (n + 1)
        # When we add the number i, we can stick it in any of i positions.
        # Putting it so that k elements are to its right adds k inversions.
        # So new_dp[j] = sum of old dp[j], dp[j-1], ..., dp[j - (i-1)] (with 0 for negative indices).
        # That's a sliding window of length i over the previous row.
        window_sum = 0
        for j in range(n + 1):
            window_sum += dp[j]
            if j >= i:
                window_sum -= dp[j - i]
            new_dp[j] = window_sum % MOD
        dp = new_dp

    return dp[n] % MOD


if __name__ == "__main__":
    print(solution(3, 0))  # 1
    print(solution(3, 1))  # 2