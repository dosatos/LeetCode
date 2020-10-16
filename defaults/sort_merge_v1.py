from typing import List


def merge_sort(array: List):
    """
    Properties

    Time complexity is O(n.logn)
    Space complexity is O(n)

    https://stackoverflow.com/questions/10342890/merge-sort-time-and-space-complexity

    :param array:
    :return:
    """
    if len(array) > 1:
        # Splitting
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursively
        merge_sort(left)
        merge_sort(right)

        # two iterators for traversing the two halves
        i, j = 0, 0

        # an iterator for main array
        k = 0

        while j < len(right) and i < len(left):
            if left[i] < right[j]:
                # The value from the left half has been used
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # for the remaining
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    array = [7, 3, 5, 4, 1]
    print("Before printing:", array)
    merge_sort(array)
    print("After printing:", array)
