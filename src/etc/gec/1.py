
def convert(array):
    new_array = []
    for x,y in array:
        if x == 0:
            new_array.append(
                (-2, float('inf')) if y > 0 else
                (-2, float('-inf'))
            )
        elif y == 0:
            new_array.append(
                (-1, 1) if x > 0 else (-1, 0)
            )
        else:
            if x > 0 and y > 0:
                data = (1, y/x)
            elif x > 0 and y < 0:
                data = (2, y/x)
            elif x < 0 and y > 0:
                data = (3, y/x)
            else:
                data = (4, y/x)
            new_array.append(data)

    return sorted(new_array)

def solution(monsters, bullets):
    answer = 0
    monsters = convert(monsters)
    bullets = convert(bullets)

    mlen, blen = len(monsters), len(bullets)
    mi, bi = 0, 0
    while mi < mlen and bi < blen:
        if monsters[mi] == bullets[bi]:
            answer += 1
            mi += 1
            bi += 1
        elif monsters[mi] < bullets[bi]:
            mi += 1
        else:
            bi += 1

    return answer if answer != 0 else -1


if __name__ == '__main__':
    print(solution(
        [[2,3],[4,5],[3,-3],[2,-4],[3,-6],[-3,-3],[-5,0],[-4,4]],
        [[4,1],[4,6],[1,-2],[-4,-4],[-3,0],[-4,4]])
    )

    print(solution(
        [[-4, 4], [-2, 2], [6, 2], [0, -2]],
        [[3, 1], [-1, 1], [-1, 1], [0, -4], [2, -3]]
    ))
    print(solution(
        [[1,2],[-2,-1],[1,-2],[3,-1]],
        [[1,0],[2,1]])
    )
