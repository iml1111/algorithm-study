# -*- coding: utf-8 -*- 
'''
해시
완주하지 못한 선수
'''
from collections import defaultdict


def solution(participant, completion):
	complete_dict = defaultdict(int)
	for i in completion:
		complete_dict[i] += 1

	for name in participant:
		if name in complete_dict and complete_dict[name] > 0:
			complete_dict[name] -= 1
		else:
			return name


'''
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''