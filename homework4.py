import csv
import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(10000)

# Note: No AI used in any part of this homework

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

    def measurePerformance(self):
            sizes = [10**4, 10**5, 5 * 10**5, 10**6]
    
            def generate_input(n, itype):
                if itype == "random":
                    return [random.uniform(-1e6, 1e6) for _ in range(n)]
                elif itype == "sorted":
                    return [float(i) for i in range(n)]
                elif itype == "reverse":
                    return [float(n - i) for i in range(n)]
                elif itype == "repeated":
                    vals = [random.uniform(-100, 100) for _ in range(10)]
                    return [random.choice(vals) for _ in range(n)]
    
            input_types = ["random", "sorted", "reverse", "repeated"]
    
            print("\nPROBLEM 3: PERFORMANCE ANALYSIS")
            for itype in input_types:
                print(f"\nInput type: {itype.upper()}")
                print(f"{'N':<12} {'QS Time(s)':<15} {'QS Mem(MB)':<15} {'HS Time(s)':<15} {'HS Mem(MB)':<15}")
                print("-" * 70)
    
                for n in sizes:
                    data = generate_input(n, itype)
    
                    qs_time = qs_mem = hs_time = hs_mem = None
    
                    try:
                        tracemalloc.start()
                        t0 = time.perf_counter()
                        self.randomQuickSort(data[:])
                        t1 = time.perf_counter()
                        _, peak = tracemalloc.get_traced_memory()
                        tracemalloc.stop()
                        qs_time = round(t1 - t0, 4)
                        qs_mem = round(peak / 1024 / 1024, 2)
                    except RecursionError:
                        tracemalloc.stop()
                        qs_time = "RecursionError"
                        qs_mem = "N/A"
                        print(f"  [QuickSort] RecursionError encountered at N={n}")
                    except Exception as e:
                        tracemalloc.stop()
                        qs_time = f"Error: {e}"
                        qs_mem = "N/A"
    
                    try:
                        tracemalloc.start()
                        t0 = time.perf_counter()
                        self.heapSort(data[:])
                        t1 = time.perf_counter()
                        _, peak = tracemalloc.get_traced_memory()
                        tracemalloc.stop()
                        hs_time = round(t1 - t0, 4)
                        hs_mem = round(peak / 1024 / 1024, 2)
                    except RecursionError:
                        tracemalloc.stop()
                        hs_time = "RecursionError"
                        hs_mem = "N/A"
                        print(f"  [HeapSort] RecursionError encountered at N={n}")
                    except Exception as e:
                        tracemalloc.stop()
                        hs_time = f"Error: {e}"
                        hs_mem = "N/A"
    
                    print(f"{n:<12} {str(qs_time):<15} {str(qs_mem):<15} {str(hs_time):<15} {str(hs_mem):<15}")

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
    
    homework4.measurePerformance()
