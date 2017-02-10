import collections

arr =[[0, 2, 3], [2, 0, 4], [3, 4, 0]]
print(dict(((j,i), arr[i][j]) for i in range(len(arr)) for j in range(len(arr[0])) if i<j))

def tree():
    return collections.defaultdict(tree)

# d = tree()
# d['js']['title'] = 'Script1'

d = collections.defaultdict(list)
d['js'].append({'foo': 'bar'})
d['js'].append({'other': 'thing'})

print(d)
