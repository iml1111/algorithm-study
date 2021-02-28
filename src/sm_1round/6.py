def search(arr, left, right):
    if right - left == 1:
        return max(arr[left], arr[right])
    mid = (right + left) // 2
    left_max =  max(arr[left: mid + 1]) + search(arr, mid + 1, right)
    right_max = max(arr[mid + 1: right]) + search(arr, left, mid)
    return max(left_max, right_max)

def solution(arr):
    return search(arr, 0, len(arr)-1)

if __name__ == '__main__':
    print(solution([1,3,10,9,6,2,3,2]))