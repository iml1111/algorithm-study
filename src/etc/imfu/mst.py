def get_parent(parents: list, v: int):
	if parents[v] != v:
		parents[v] = get_parent(parents, parents[v])
	return parents[v]


def union_parent(parents: list, v1: int, v2: int):
	v1_parent = get_parent(parents, v1)
	v2_parent = get_parent(parents, v2)
	if v1_parent < v2_parent:
		parents[v2_parent] = v1_parent
	else:
		parents[v1_parent] = v2_parent


def kruskal(vertex_num: int, edge_list: list):
	parents = [i for i in range(vertex_num)]
	edge_list = sorted(edge_list, key=lambda x:x[2])
	mst_edges = []

	for e in edge_list:
		v1, v2, weight = e
		if get_parent(parents, v1) != get_parent(parents, v2):
			union_parent(parents, v1, v2)
			mst_edges.append(e)

	return sum([e[2] for e in mst_edges])


if __name__ == '__main__':
	print(kruskal(
		5, 
		[
			(0, 1, 1),
			(1, 2, 6),
			(2, 4, 4),
			(1, 3, 2),
			(3, 4, 5),
			(0, 4, 3),
		]
	))
	print(kruskal(7,
[
	(1,3,4),
	(1,4,3),
	(1,5,1),
	(1,2,9),
	(3,6,6),
	(2,4,4),
	(2,5,5),
	(4,5,2),
	(4,6,8),
]
	))
	print(kruskal(
		3,
		[
			(0, 1, 1),
			(1, 2, 2),
			(0, 2, 3),
		]
	))