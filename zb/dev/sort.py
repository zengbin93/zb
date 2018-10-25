

def quick_sort(array, left, right):
    """快速排序"""
    if left >= right:
        return

    low = left
    high = right
    key = array[low]

    while left < right:

        # 将大于key的值放到右边
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]

        # 将小于key的值放到左边
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]

    # 把key放到对应的位置
    array[right] = key

    # 递归执行（左右同时排序）
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)



