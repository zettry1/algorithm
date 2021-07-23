#O(n)|O(h) h height of binary tree
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node":root,"depth":0}]

    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"],nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths +=depth
        stack.append({"node":node.left,"depth":depth+1})
        stack.append({"node":node.right,"depth":depth+1})
    return sumOfDepths


#O(n)| O(h)
def nodeDepths2(root,depth=0):
    if root is None:
        return 0
    return depth + nodeDepths2(root.left,depth+1) + nodeDepths2(root.right,depth+1)
