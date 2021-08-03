from collections import defaultdict
import heapq

def make_graph(road):
    graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for src, tgt, dist in road:
        graph[src][tgt] = min(dist, graph[src][tgt])
        graph[tgt][src] = min(dist, graph[src][tgt])
    return graph

def solution(N, road, K):
    graph = make_graph(road)
    dists = [0, 0] + [float('inf') for _ in range(N - 1)]
    q = []
    heapq.heappush(q, [0, 1])
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if dists[cur_node] >= cur_dist:
            for next_node, next_dist in graph[cur_node].items():
                new_dist = cur_dist + next_dist
                if new_dist < dists[next_node]:
                    dists[next_node] = new_dist
                    heapq.heappush(q, [new_dist, next_node])

    return sum([True if i <= K else False for i in dists]) - 1