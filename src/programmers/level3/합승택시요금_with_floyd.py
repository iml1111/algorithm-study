def get_dist(n, fares):
    dist = [[float('inf')] * (n) for _ in range(n)]
    for i in range(1, n):
        dist[i][i] = 0
    for src, tgt, point in fares:
        dist[src][tgt], dist[tgt][src] = point, point
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def solution(n, s, a, b, fares, answer=float('inf')):
    dist = get_dist(n+1, fares)
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer

if __name__ == '__main__':
    print(
        solution(
            n=6, s=4, a=5, b=6,
            fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
        )
    )