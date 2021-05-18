

def quick_sort(lists,i,j):
    if i>= j:
        return lists
    
    m = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= m:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= m:
            i += 1
        lists[j] = lists[i]
    lists[j] = m
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists


if __name__ == '__main__':
    lists = [4,1,7,12,3,5,57,2]
    print("排序前")
    print(lists)
    print("排序后")
    print(quick_sort(lists,0,len(lists)-1))
    
