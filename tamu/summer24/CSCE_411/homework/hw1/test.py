def max_sum_contiguous_subsequence_dp(S):
    n = len(S)
    if n == 0:
        return []
    
    # Initialize DP array
    dp = [0] * n
    dp[0] = S[0]
    
    # Variables to keep track of the maximum sum and its indices
    max_sum = dp[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, n):
        # If including the current element increases the sum, extend the subsequence
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + S[i]
        # Otherwise, start a new subsequence from the current element
        else:
            dp[i] = S[i]
            temp_start = i
        
        # Update max_sum and indices if necessary
        if dp[i] > max_sum:
            max_sum = dp[i]
            start = temp_start
            end = i
    
    return S[start:end+1]

# Example usage
# S = [6, 16, -29, 11, -4, 41, 11]
S = [-2, 3, 4, -5]
result = max_sum_contiguous_subsequence_dp(S)
print(f"Maximum sum contiguous subsequence: {result}")
print(f"Sum: {sum(result)}")
