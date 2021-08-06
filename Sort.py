from typing import List
from Heap import MinHeap, MaxHeap

def quickSort(nums: List[int]) -> List[int]:
    return 1

def mergeSort(nums: List[int]) -> List[int]:
    def mergeLists(listOne, listTwo):
        if(not listOne and not listTwo):
            return []
        elif(not listOne):
            return listTwo
        elif(not listTwo):
            return listOne
        mergedList = []
        pointerOne = 0
        pointerTwo = 0
        while pointerOne < len(listOne) and pointerTwo < len(listTwo):
            if(listOne[pointerOne] <= listTwo[pointerTwo]):
                mergedList.append(listOne[pointerOne])
                pointerOne += 1
            else:
                mergedList.append(listTwo[pointerTwo])
                pointerTwo += 1
        while pointerOne < len(listOne):
            mergedList.append(listOne[pointerOne])
            pointerOne += 1
        while pointerTwo < len(listTwo):
            mergedList.append(listTwo[pointerTwo])
            pointerTwo += 1
        return mergedList

    if(len(nums) == 1):
        return nums
    elif(len(nums) == 0):
        return []
    mid = int(len(nums) / 2)
    left = mergeSort(nums[0:mid])
    right = mergeSort(nums[mid:])
    mergedList = mergeLists(left, right)
    return mergedList

def heapSortMin(nums: List[int]) -> List[int]:
    if(not nums):
        return []
    heapUtil = MinHeap()
    for num in nums:
        heapUtil.heappush(num)
    returnList = []
    while(heapUtil.size() > 0):
        returnList.append(heapUtil.heappop())
    return returnList

def heapSortMax(nums: List[int]) -> List[int]:
    if(not nums):
        return []
    heapUtil = MaxHeap()
    for num in nums:
        heapUtil.heappush(num)
    returnList = []
    while(heapUtil.size() > 0):
        returnList.append(heapUtil.heappop())
    return returnList

# iterate over the array and find where to place the element
def insertionSort(nums: List[int]) -> List[int]:
    if(not nums):
        return []
    for right in range(1, len(nums)):
        curr = nums[right]
        left = right - 1
        while(curr < nums[left] and left >= 0):
            nums[left + 1] = nums[left]
            left -= 1
        nums[left + 1] = curr
    return nums

            
# iterate over the array and find the min each time, build from the left
def selectionSort(nums: List[int]) -> List[int]:
    if(not nums):
        return []
    for left in range(len(nums)):
        minElement = min(nums[left:])
        indexOfMin = nums.index(minElement, left)
        temp = nums[indexOfMin]
        nums[indexOfMin] = nums[left]
        nums[left] = temp
    return nums

def bubbleSort(nums:List[int]) -> List[int]:
    if(not nums):
        return []
    swapped = True
    while swapped:
        swapCount = 0
        for i in range(0, len(nums) - 1):
            if(nums[i] > nums[i+1]):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                swapCount += 1
        if(swapCount == 0):
            swapped = False
    return nums