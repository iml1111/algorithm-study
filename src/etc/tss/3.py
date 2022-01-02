from collections import defaultdict

def make_graph(csv_list):

    id2name = {}
    for id, name, parent, num_member in csv_list:
        id2name[id] = name

    graph = defaultdict(
        lambda: {'parent':None, 'children':[], 'num_member':None})

    for id, name, parent, num_member in csv_list:
        if parent != "":
            graph[name]['parent'] = id2name[parent]
        graph[name]['num_member'] = int(num_member)
        if parent != "":
            graph[id2name[parent]]['children'].append(name)

    return graph

def get_nums(matched_dict, graph, target):
    matched_dict[target] = graph[target]['num_member']
    for child in graph[target]['children']:
        get_nums(matched_dict, graph, child)

def solution(csv_string, keyword):
    csv_list = csv_string.split("\n")[1:]
    csv_list = [i.split(",") for i in csv_list]
    graph = make_graph(csv_list)

    matched_list = []
    for name in graph.keys():
        if keyword in name:
            matched_list.append(name)

    if matched_list == []:
        return -1

    matched_dict = {}
    for target in matched_list:
        get_nums(matched_dict, graph, target)
    return sum(matched_dict.values())

if __name__ == '__main__':
    print(solution(
        "조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11",
        "아웃"
    ))