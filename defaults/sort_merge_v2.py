def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(array, left, right)


def merge(array, left, right):
    lp, rp, pos = 0, 0, 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            array[pos] = left[lp]
            lp += 1
        else:
            array[pos] = right[rp]
            rp += 1
        pos += 1
    while lp < len(left):
        array[pos] = left[lp]
        lp += 1
        pos += 1
    while rp < len(right):
        array[pos] = right[rp]
        rp += 1
        pos += 1


if __name__ == '__main__':
    array = [6, 3, 1, 1, 7]
    merge_sort(array)
    print(array)
