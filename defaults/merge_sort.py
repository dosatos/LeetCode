def merge(array, arr1, arr2):
	lp, rp, pos = 0, 0, 0

	while lp < len(arr1) and rp < len(arr2):
		if arr1[lp] < arr2[rp]:
			array[pos] = arr1[lp]
			lp += 1
		else:
			array[pos] = arr2[rp]
			rp += 1
		pos += 1
	return array


def merge_sort(array):
	if len(array) <= 1:
		return array
	mid = len(array) // 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	return merge(array, left, right)


print(merge_sort(lst))