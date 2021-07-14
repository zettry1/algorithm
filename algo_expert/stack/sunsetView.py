#O(n)|O(n)
def sunsetView(buildings,direction):
    builderingsWithSunetViews=[]

    startIdx = 0 if direction== "WEST" else len(buildings)-1
    step = 1 if direction =="WEST" else -1

    idx = startIdx

    runningMaxHeight = 0

    while idx>=0 and idx < len(buildings):
        buildingHeight = buildings[idx]
        if buildingHeight>runningMaxHeight:
            builderingsWithSunetViews.append(idx)

        runningMaxHeight = max(runningMaxHeight,buildingHeight)
        idx +=step

    if direction =="EAST":
        return builderingsWithSunetViews[::-1]

    return builderingsWithSunetViews


# STack solution
#O(n)|O(n)
def sunsetView2(buildings,direction):
    candiateBuildings= []

    startIdx = 0 if direction =="EAST" else len(buildings)-1
    step = 1 if direction =="EAST" else -1

    idx =startIdx

    while idx>=0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        while len(candiateBuildings)>0  and buildings[candiateBuildings[-1]]<=buildingHeight:
            candiateBuildings.pop()
        candiateBuildings.append(idx)
        idx+=step

    if direction =="WEST":
        return candiateBuildings[::-1]
    return candiateBuildings
