"""
The goal is to find the number of consecutive 1's in a given array.
"""

def naive(array):
    """ 
    Complexity: Naive solution, O(n**2) time, and O(n) space
    """
    maxConsecutive = 0

    for pivotIndex in range(len(array)):
        
        if array[pivotIndex]==1:

            count, innerIndex = 0, pivotIndex
            
            while innerIndex<len(array) and array[innerIndex]==1:
                count += 1    
                innerIndex += 1
            
            maxConsecutive = max(maxConsecutive, count)
    
    return maxConsecutive 


def improved(array):
    """
    Complexity: O(n) time, and O(1) space
    """
    runningMaximum, runningCount = 0, 0

    for pivotIndex in range(len(array)):

        if array[pivotIndex]==1:
            runningCount += 1
        else:
            runningCount = 0

        runningMaximum = max(runningMaximum, runningCount)    

    return runningMaximum


def test(function):
    testCases = [[0, 1, 1, 0, 1, 0], 
                 [1, 1, 1, 1], 
                 [0, 0, 0], 
                 [1, 0, 1, 1, 1, 1, 0, 1, 1]]
    for test in testCases:
        print(function(test))
        
        
test(naive)
print("--")
test(improved)