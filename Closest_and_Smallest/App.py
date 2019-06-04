def closest(strng):
    if (not strng):
        return []
    numbers = list(map(int,strng.split()))
    weights = []
    
    # Get weights
    for n_str in strng.split():
        # Get the digits in int type
        n_dig = map(int, list(n_str))
        # Get the weight and append it to the list
        weights.append(sum(n_dig))
    
    # Calculate weight differences and decide what to do

    diff = weights[0]
    result1 = []
    result2 = []
    # This type of iteration already satisfied the third requirement of the solution (the smallest index...) because the first ocurrence it what will be in the results
    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
            # If it's the two closest at the moment of the iteration...
            if diff > abs(weights[i] - weights[j]):
                # Update the closest weight value and save the results
                diff = abs(weights[i] - weights[j])
                if (weights[i] <= weights[j]):
                    result1 = [weights[i], i, numbers[i]]
                    result2 = [weights[j], j, numbers[j]]
                else:
                    result1 = [weights[j], j, numbers[j]]
                    result2 = [weights[i], i, numbers[i]]
            elif diff == abs(weights[i] - weights[j]):
                # To satisfy the second requirement (if the difference is the same, the numbers with the smallest weight)
                if (weights[i] <= weights[j]):
                    # With the second condition I make sure that, if the difference of weights is 0, both numbers need to have smaller weight, or they won't change the results (to preserver the smaller index)
                    if (weights[j] <= result1[0] and weights[i] < result1[0]):
                        result1 = [weights[i], i, numbers[i]]
                        result2 = [weights[j], j, numbers[j]]
                if (weights[i] > weights[j]):
                    if (weights[i] <= result1[0] and weights[j] < result1[0]):
                        result1 = [weights[j], j, numbers[j]]
                        result2 = [weights[i], i, numbers[i]]

    return [result1, result2]