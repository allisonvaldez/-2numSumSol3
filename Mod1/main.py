# time: O(n log(n)) | space: O(n)

def two_num_sum(array, targetSum):
    # start by sorting the array
    array.sort()

    # initialize the left and right side of the array
    left = 0
    right = len(array) - 1

    """
    set the condition for the program to run while the leftside of array is
    less then the rightside
    """
    while left < right:
        # initialize a value that is the sum of the left and right index
        currentSum = array[left] + array[right]

        """
        create an if statement that satisfys the condition when:
        1. condition that meets the criteria
        2. when currentSum is less than the targetSum move to left in index by +=1
        3. when currentSum is more than targetSum move to right in index by -=1
        """
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
        return []


print(two_num_sum([4, 6, 1, -3], 3))
