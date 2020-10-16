from typing import List


def insert_array(array: List) -> None:
    for i in range(1, len(array)):
        value = array[i]
        left = i - 1
        while left >= 0 and value < array[left]:
            array[left + 1] = array[left]
            array[left] = value
            left -= 1


if __name__ == '__main__':
    arrays = [
        [1, 6, 7, 6, 1],
        [6, 7, 6, 1],
        [],
        [1],
    ]
    for array in arrays:
        print()
        print(array)
        insert_array(array)
        print(array)
