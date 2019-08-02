# Globals for recursion
visited = []
possiblePath = []
allPossiblePaths = []

# Input for the problem
changeTable = [[0,0,0,0,0,1,0,0,1,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0]]

# function notVistited: checkes if a particular color is already checked for color transition 
# params: 
#   position: the color to check for occurence
def notVisited(position):
    for place in visited:
        if position == place:
            return False
    return True

# function checkPath: checkes for a paths from start to end and adds them to allPossiblePaths in recursion
# params: 
#   start: starting color of the chameleon
#   end: ending color of the chameleon

def checkPath(start, end):
    global possiblePath
    if len(visited) == 10:
        return
    print("checking path from "+str(start)+" to "+str(end))
    for i in range(10):
        if(changeTable[start][i] == 1 and i == end):
            possiblePath.append(end)
            allPossiblePaths.append(possiblePath)
            possiblePath = []
            return 
        if(changeTable[start][i] == 1 and notVisited(i)):
            visited.append(i)
            possiblePath.append(i)
            checkPath(i, end)
    if len(possiblePath) == 0:
        print("-1")
    else:
        possiblePath.pop()
    
    return 
            
# function main: calls checkPaths and calculates minimum distance in all possible color paths 
# params: 
#   start: starting color of the chameleon
#   end: ending color of the chameleon
def main(start, end):
    checkPath(start, end)
    minPath = len(allPossiblePaths[0])
    for path in allPossiblePaths:
        minPath = len(path) if minPath > len(path) else minPath
    print("Number of changes required are: ")    
    print(minPath)
    print("All possiible color changes are: ")
    print(allPossiblePaths)

main(0,8)