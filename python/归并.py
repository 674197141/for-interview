

def merge(left,right):
    res = []
    while len(left) > 0 and len(right) >0:
        if (left[0] < right[0]):
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    middle = n//2
    left = arr[:middle]
    right = arr[middle:]
    left_sort = mergeSort(left)
    right_sort = mergeSort(right)
    return merge(left_sort,right_sort)


if __name__ == '__main__':
    lists = [4,1,7,12,3,5,57,2]
    print("排序前")
    print(lists)
    print("排序后")
    print(mergeSort(lists))
    

    