from pprint import pprint

def make_tree(enroll, referral):
    tree = {'-': {'pay': 0, 'parent': None}}
    for enr, ref in zip(enroll, referral):
        tree[enr] = {'pay': 0, 'parent': ref}
    return tree

def piramid(tree, node, amount):
    amount_10 = amount // 10
    amount_90 = amount - amount_10
    tree[node]['pay'] += amount_90
    if tree[node]['parent'] is not None:
        piramid(tree, tree[node]['parent'], amount_10)
    else:
        tree[node]['pay'] += amount_10


def solution(enroll, referral, seller, amount):
    tree = make_tree(enroll, referral)
    for node, amount in zip(seller, amount):
        piramid(tree, node, amount * 100)
    return [tree[i]['pay'] for i in enroll]

if __name__ == '__main__':
    print(solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-",       "-", "mary",    "edward", "mary", "mary", "jaimie", "edward"],

        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10]

    ))