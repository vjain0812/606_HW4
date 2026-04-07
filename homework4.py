import csv
import random

class Homework4:

    # QUESTION 1
    # Implement randomized quicksort and heapsort in the below function
    # Input for the function - an array of floating point numbers ex: [3.0,9.0,1.0]
    # Output - sorted list of numbers ex: [1.0,3.0,9.0]
    # Numbers can be negative, repeated, and floating point numbers
    # DO NOT USE THE INBUILT HEAPQ MODULE TO SOLVE THE PROBLEMS
    def randomQuickSort(self, nums: list) -> list:
        # Todo: Implement randomized quicksort
        if len(nums) <= 1:
            return nums
        pivot_index = random.randint(0, len(nums) - 1)
        pivot = nums[pivot_index]
        less = [x for i, x in enumerate(nums) if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for i, x in enumerate(nums) if x > pivot]
        return self.randomQuickSort(less) + equal + self.randomQuickSort(greater)

    def heapSort(self, nums: list) -> list:
        # Todo: Implement heapsort
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        arr = nums[:]
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)
        return arr

# Main Function
# Do not edit the code below
if __name__ == "__main__":
    homework4 = Homework4()
    testCasesforSorting = []
    try:
        with open('testcases.csv', 'r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testCasesforSorting.append(row)
    except FileNotFoundError:
        print("File Not Found")

    # Running Test Cases for Question 1
    print("RUNNING TEST CASES FOR QUICKSORT: ")
    for row, (inputValue, expectedOutput) in enumerate(testCasesforSorting, start=1):
        if inputValue == "" and expectedOutput == "":
            inputValue = []
            expectedOutput = []
        else:
            inputValue = inputValue.split(" ")
            inputValue = [float(i) for i in inputValue]
            expectedOutput = expectedOutput.split(" ")
            expectedOutput = [float(i) for i in expectedOutput]
        actualOutput = homework4.randomQuickSort(inputValue)
        are_equal = all(x == y for x, y in zip(actualOutput, expectedOutput))
        if are_equal:
            print(f"Test Case {row} : PASSED")
        else:
            print(f"Test Case {row}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")

    print("\nRUNNING TEST CASES FOR HEAPSORT: ")
    for row, (inputValue, expectedOutput) in enumerate(testCasesforSorting, start=1):
        if inputValue == "" and expectedOutput == "":
            inputValue = []
            expectedOutput = []
        else:
            inputValue = inputValue.split(" ")
            inputValue = [float(i) for i in inputValue]
            expectedOutput = expectedOutput.split(" ")
            expectedOutput = [float(i) for i in expectedOutput]
        actualOutput = homework4.heapSort(inputValue)
        are_equal = all(x == y for x, y in zip(actualOutput, expectedOutput))
        if are_equal:
            print(f"Test Case {row} : PASSED")
        else:
            print(f"Test Case {row}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")