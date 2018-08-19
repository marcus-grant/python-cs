def fibonacci(n):
    """ Computes the nth fibonacci number using dynamic programming """
    # Take care of edge cases i.e. less than 0 & return the 0 case
    if n <= 0:
        return 0
    
    # Prepare memoization array to store sub-results to fibonacci sequence
    memo = [0] * (n + 1)

    # Initialize the memo list so it fits with the
    # ...initial conditions for a fibonacci sequence
    memo[1] = 1

    # Iterate through the initialized memo list,
    # ...updating each element with the sum of the previous two
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    # Return last element to get fibonacci number
    return memo[n]

    
    