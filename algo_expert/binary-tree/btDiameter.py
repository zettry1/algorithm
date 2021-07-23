class TreeInfo:
    def __init__(self,diameter ,height ):
        self.diameter = diameter
        self.height = height

def binaryTreeDiameter(tree):

    return getTreeInfo(tree).diameter



def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)


    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter,rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot,maxDiameterSoFar)
    currentHeight = 1+max(leftTreeInfo.height,rightTreeInfo.height)

    return TreeInfo(currentDiameter,currentHeight)