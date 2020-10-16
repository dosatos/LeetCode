from typing import List


def insert_array(array: List) -> None:
    """
    Complexity

    Worst case time complexity: O(n^2)
    Average case time complexity: O(n^2)
    Best case time complexity: O(n)
    Space complexity: O(1)

    :param array:
    :return:
    """
    for i in range(1, len(array)):
        value = array[i]

        left_pointer = i - 1

        while left_pointer >= 0 and value < array[left_pointer]:
            array[left_pointer + 1] = array[left_pointer]
            array[left_pointer] = value
            left_pointer -= 1


if __name__ == '__main__':
    array = [1, 6, 7, 6, 1]
    print(array)
    insert_array(array)
    print(array)
