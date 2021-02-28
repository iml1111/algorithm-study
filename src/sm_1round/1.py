from collections import defaultdict

def get_graph(stree):
    graph = defaultdict(list)
    for src, tgt in stree:
        graph[src].append(tgt)
    return graph

def get_single_skill(stree):
    first, last = set(), set()
    for src, tgt in stree:
        first.add(src)
        last.add(tgt)
    return first - last

def dfs(graph, node):
    if not graph[node]:
        return [[node]]
    routes = []
    for tgt in graph[node]:
        routes.extend([[node] + i for i in dfs(graph, tgt)])
    return routes

def solution(skills, stree):
    singles = get_single_skill(stree)
    graph = get_graph(stree)
    answer = []
    for node in skills:
        if node in singles:
            answer.extend(dfs(graph, node))
    return answer


if __name__ == '__main__':
    test_cases = [
        (
            ['h', 'g', 'f', 'w', 'r', 'a'],
            [
                ['h', 'g'],
                ['h', 'r'],
                ['g', 'r'],
                ['g', 'w'],
                ['a', 'w'],
            ]
        ),
    ]

    for skills, stree in test_cases:
        print(solution(skills, stree))