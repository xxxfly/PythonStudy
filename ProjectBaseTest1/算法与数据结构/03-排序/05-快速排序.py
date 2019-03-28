# coding:utf-8


def quickSort(orgList, start, last):
    """快速排序"""
    if start >= last:
        return
    mid_vlaue = orgList[start]
    low = start
    high = last
    while low < high:
        # high 左移
        while low < high and orgList[high] >= mid_vlaue:
            high -= 1
        orgList[low] = orgList[high]
        # low 右移
        while low < high and orgList[low] < mid_vlaue:
            low += 1
        orgList[high] = orgList[low]
    # 循环退出时，low==high
    orgList[low] = mid_vlaue

    # 递归
    # 对low左边的列表进行快速排序
    quickSort(orgList, start, low-1)
    # 对low右边的列表进行快速排序
    quickSort(orgList, low+1, last)


if __name__ == "__main__":
    a = [33, 2, 34, 123, 56, 47, 87, 38, 26, 88, 52, 9, 17, 28, 243]
    print(a)
    quickSort(a, 0, len(a)-1)
    print(a)
