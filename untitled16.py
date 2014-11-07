import sys

sys.setrecursionlimit(10000)
DIFF=0

def reconstruct(node, visited, adj, tree):
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            tree[node].append(i)
            reconstruct(i, visited, adj, tree)

def dfs(node, tree, weights, total_weight):
    if len(tree[node]) == 0:
        # leaf
        #print 'Leaf {0}: {1}'.format(node, weights[node])
        subtree_weight = weights[node]
    elif len(tree[node]) == 1:
        child_weight = dfs(tree[node][0], tree, weights, total_weight)
        #print 'One child {0}: {1}'.format(node, weights[node])
        #print 'Child weight {0}'.format(child_weight)
        subtree_weight = weights[node] + child_weight
    else:
        left = dfs(tree[node][0], tree, weights, total_weight)
        right = dfs(tree[node][1], tree, weights, total_weight)
        #print 'Two child {0}: {1}'.format(node, weights[node])
        #print 'Child weight {0} and {1}'.format(left, right)
        subtree_weight = weights[node] + left + right

    diff = abs(total_weight - 2 * subtree_weight)
    
    global DIFF
    if diff < DIFF:
        DIFF = diff
    return subtree_weight


def main():
    N = int(raw_input())
    weights = map(int, raw_input().split())
    total_weight = sum(weights)
    adj = [ [] for _ in xrange(N) ]

    for _ in xrange(N - 1):
        (a, b) = map(int, raw_input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    tree = [ [] for _ in xrange(N) ]
    visited = [ False ] * N

    global DIFF
    DIFF = total_weight

    reconstruct(0, visited, adj, tree)

    dfs(0, tree, weights, total_weight)

    print DIFF


if __name__ == '__main__':
    main()