
def branchSum(root):
    sums =[]
    calculateBranchSums(root,0,sums)
    return sums


def calculateBranchSums(node,runningSum,sums):
    if node is None:
        return
    newRunningSum = runningSum +node.value
    if node.left is None and node.righjt is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left,newRunningSum,sums)
    calculateBranchSums(node.right,newRunningSum,sums)
