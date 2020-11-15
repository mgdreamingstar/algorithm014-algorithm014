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


if __name__ == "__main__":
    nums = [1, 3, 4, 5, 2]
    # print("bubble sort:", bubble_sort(nums))
    # print("selection sort:", selection_sort(nums))
    # print("insertion sort:", insertion_sort(nums))
    # print("shell sort:", shell_sort(nums))
    # print("quick sort:", quick_sort(nums, 0, len(nums) - 1))
    print("merge sort:", merge_sort(nums, 0, len(nums) - 1))

