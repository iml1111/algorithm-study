import re
from collections import defaultdict

def ArrayChallenge(strArr):
    parsedArr = [re.findall("\d+", i) for i in strArr]
    tree = defaultdict(lambda : {'parent': None, 'left': None, 'right': None})

    for child, parent in parsedArr:
        if tree[child]['parent'] is None:
           tree[child]['parent'] = parent
        else:
            return False

        if tree[parent]['left'] is None:
            tree[parent]['left'] = child
        elif tree[parent]['right'] is None:
            tree[parent]['right'] = child
        else:
            return False

    num_of_root = sum([tree[node]['parent'] is None for node in tree])
    return num_of_root == 1

# keep this function call here
print(ArrayChallenge(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))