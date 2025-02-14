"""
The goal is to find the maximum sum of a subarray in this array
"""
def naive(array):
    """
    Complexity: O(n**2) time and O(1) space
    """
    maxSubSum = float("-Inf")
    for pivotIndex in range(len(array)):
        runSubSum = 0

        for innerIndex in range(pivotIndex, len(array)):
            runSubSum += array[innerIndex] 
            maxSubSum = max(maxSubSum, runSubSum)

    return maxSubSum             

def improved(array):
    """
    Complexity: O(n) time and O(1) space
    """

    

def test(function):
    testCases = [[2, 3, -8, 7, -1, 2, 3], 
                 [5, 8, 3],
                 [-6, -1, -8]]

    for test in testCases:
        print(function(test))

test(naive)