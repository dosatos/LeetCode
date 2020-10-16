from typing import List


def split_by_pivot(array, left, right):

    pivot = array[right]
    border_index = left - 1
    print("\n", array, f"from: {left}, to: {right}", "->", array[left: right], "[ pivot", pivot, "] [border_index is", border_index, "]")

    print(range(left, right))
    for i in range(left, right):
        print(f"Comparing {array[i]} < {pivot}: {array[i] <= pivot}")
        if array[i] < pivot:
            border_index += 1
            print(f"Borders goes up {border_index - 1} to {border_index}")
            print(f"Swapping array[broder_index]:{array[border_index]} <-> array[i]:{array[i]}")
            array[border_index], array[i] = array[i], array[border_index]
            print("After swap: ", array)
        print("----")

    print(f"changing pivot:{array[right]} and what's right to the border_index:{array[border_index + 1]}")
    print("before", array)
    (array[border_index + 1], array[right]) = (array[right], array[border_index + 1])
    print("after", array)

    return border_index + 1


def _quick_sort(array: List, left: int, right: int):
    if right - left > 0:
        pivot = split_by_pivot(array, left, right)
        _quick_sort(array, left, pivot - 1)
        _quick_sort(array, pivot + 1, right)
    return array


def quick_sort(array: List):
    """
    === TIME COMPLEXITY ===

    On average, this algorithm will perform at O(n* log n).
    This happens when the pivot element is not the greatest or smallest element
    and when the pivot element is not near the middle element.

    The quicksort has a worst case complexity of O(n2).
    This occurs when the element selected as a pivot is either the greatest or
    a smallest element. If this is the case, the pivot element will always be at
     the end of a sorted array. This will create a number of unnecessary subarrays.

    The best case complexity for this algorithm is O(n* log n).
    This happens when the pivot element is either equal to the middle element or near the middle element.


    === SPACE ===
    https://www.youtube.com/watch?v=kFeXwkgnQ9U
    https://www.youtube.com/watch?v=CB_NCoxzQnk

    :param array:
    :return:
    """
    return _quick_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    # array = [6, 4, 2, 3, 7, 8]
    array = [7, 6, 3, 4, 2]
    print("Start", array)
    print("Resullts", quick_sort(array))
