from heapq import heappush, heappop
from collections import defaultdict

def get_graph(fares):
    graph = defaultdict(lambda: {})
    for src, tgt, dist in fares:
        graph[src].update({tgt:dist})
        graph[tgt].update({src:dist})
    return graph

def get_dist(n, graph, src, tgts):
    dists = {v: float('inf') for v in range(1, n+1)}
    dists[src], heap = 0, []
    heappush(heap, [dists[src], src])

    while heap:
        cur_dist, cur_tgt = heappop(heap)
        if dists[cur_tgt] >= cur_dist:
            for next_tgt, next_dist in graph[cur_tgt].items():
                if cur_dist + next_dist < dists[next_tgt]:
                    dists[next_tgt] = cur_dist + next_dist
                    heappush(heap, [dists[next_tgt], next_tgt])

    return sum([dists[tgt] for tgt in tgts])

def solution(n, s, a, b, fares, answer=float('inf')):
    graph = get_graph(fares)
    for i in range(1, n+1):
        answer = min(
            answer,
            get_dist(n, graph, s, [i]) + get_dist(n, graph, i, [a, b])
        )
    return answer

if __name__ == '__main__':
    print(
        solution(
            n=6, s=4, a=5, b=6,
            fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
        )
    )