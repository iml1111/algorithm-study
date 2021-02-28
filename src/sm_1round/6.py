def search(tree, a, b):
    if a >= len(tree) // 2:
        return tree[a] + tree[b]
    left_max = tree[a] + search(tree, b * 2, b * 2 + 1)
    right_max = tree[b] + search(tree, a * 2, b * 2 + 1)
    return max(left_max, right_max)

def solution(arr):
    tree = []
    while len(arr) > 2:
        arr = [max(arr[idx], arr[idx + 1]) for idx in range(0, len(arr) - 1, 2)]
        tree = arr + tree
    return search([0,0] + tree, 2, 3)

if __name__ == '__main__':
    print(solution([1,3,10,9,6,2,3,2]))