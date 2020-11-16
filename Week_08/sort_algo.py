def bubble_sort(nums):
    for i in range(len(nums) - 1):
        # i 用来记录已排序好的元素数量
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selection_sort(nums):
    N = len(nums)
    for i in range(N):
        minimum = i
        for j in range(i + 1, N):
            if nums[minimum] > nums[j]:
                minimum = j
        nums[i], nums[minimum] = nums[minimum], nums[i]
    return nums


def insertion_sort(nums):
    # 简单插入排序
    for i in range(1, len(nums)):
        current = nums[i]
        pre_ind = i - 1
        while pre_ind >= 0 and nums[pre_ind] > current:
            nums[pre_ind + 1] = nums[pre_ind]
            pre_ind -= 1
        nums[pre_ind + 1] = current
    return nums


def shell_sort(nums):
    # 希尔排序（复杂插入排序）
    gap = len(nums) // 2
    while gap >= 1:
        for i in range(gap, len(nums)):
            j = i  # 切换分组
            current = nums[i]
            while j >= gap and current < nums[j - gap]:
                # 分组内比较
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = current
        gap //= 2
    return nums


def quick_sort(nums, begin, end):
    def partition(arr, begin, end):
        # left_nums 是小于 pivot 数字的个数
        pivot, left_nums = end, begin
        for i in range(begin, end):
            # 只要找到比 pivot 小的元素，left_nums 就 +1
            if arr[i] < arr[pivot]:
                arr[left_nums], arr[i] = arr[i], arr[left_nums]
                left_nums += 1
        # 最终，left_nums 就是 pivot 要被移动到的位置
        arr[pivot], arr[left_nums] = arr[left_nums], arr[pivot]
        return left_nums

    if begin >= end:
        return
    pivot = partition(nums, begin, end)
    quick_sort(nums, begin, pivot - 1)
    quick_sort(nums, pivot + 1, end)
    return nums


def merge_sort(nums, left, right):
    def merge(nums, left, mid, right):
        temp = []
        # 两部分的开始分别为 i, j
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left : right + 1] = temp

    if right <= left:
        return
    mid = (left + right) >> 1
    # 不断深入到下一层
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    # 返回上一层后合并
    merge(nums, left, mid, right)
    return nums


def heap_sort(nums):
    def heapify(parent_index, length, nums):
        temp = nums[parent_index]  # 保存父节点的值
        child_index = 2 * parent_index + 1
        while child_index < length:
            if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:
                child_index = child_index + 1
            if temp > nums[child_index]:  # 大顶堆，已满足条件（父 > 子）
                break
            # 继续向下
            nums[parent_index] = nums[child_index]
            parent_index = child_index
            child_index = 2 * parent_index + 1
        # 最终将初始父节点值放下
        nums[parent_index] = temp

    """
    遍历所有子节点的父节点，最终获取到了最大值，放在 index = 0 位置
    不从最后遍历，是因为会重复遍历
    """
    for i in range((len(nums) - 2) // 2, -1, -1):
        heapify(i, len(nums), nums)
    
    """
    将最大的元素放在最后（j 的位置）
    j 不断前移，表明其之后的位置已排序完成
    """
    for j in range(len(nums) - 1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
    return nums


if __name__ == "__main__":
    nums = [1, 3, 4, 5, 2]
    # print("bubble sort:", bubble_sort(nums))
    # print("selection sort:", selection_sort(nums))
    # print("insertion sort:", insertion_sort(nums))
    # print("shell sort:", shell_sort(nums))
    # print("quick sort:", quick_sort(nums, 0, len(nums) - 1))
    # print("merge sort:", merge_sort(nums, 0, len(nums) - 1))
    print("heap sort:", heap_sort([2, 3, 4, 5, 1, 6, 7, 9, 8, 10, 11]))

