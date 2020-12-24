from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_num = len(numbers)
    for i in range(len_num):
        for j in range(len_num - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return  numbers

def selection_sort(numbers: List[int]) -> List[int]:
    len_num = len(numbers)
    for i in range(len_num):
        min_index = i
        for j in range(i+1, len_num):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

if __name__ == '__main__':
    import  random
    nums = [random.randint(0,1000) for _ in range(10)]
    result = selection_sort(nums)
    print(result)