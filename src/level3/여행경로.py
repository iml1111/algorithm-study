from collections import defaultdict

def make_graph(tickets):
	graph = defaultdict(list)
	for s, t in tickets:
		graph[s].append(t)
	for name in graph:
		graph[name].sort(reverse=True)
	return graph

def solution(tickets):
	graph, answer = make_graph(tickets), []

	def dfs(cur):
		while graph[cur]:
			dfs(graph[cur].pop())
		else:
			nonlocal answer
			answer.append(cur)
	dfs('ICN')
	return answer[::-1]

def solution2(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())
    return path[::-1]

if __name__ == '__main__':
	# print(solution(
	# 	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
	# print(solution(
	# 	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
	# ['ICN', 'B', 'ICN', 'A', 'D', 'A']
	print(solution(
		[['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))
	print(solution2(
		[['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))
	