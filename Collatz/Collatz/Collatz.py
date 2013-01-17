cache = dict()
def RunCollatz ( x ):
    numCycles = 1
    cacheList = []
    while x > 1:
        if x in cache:
            numCycles += cache [ x ]
            break        
        cacheList.append ( x )
        numCycles += 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
    temp = numCycles - 1
    for i in cacheList:
        cache[i] = temp
        temp -= 1
    return numCycles

numCases = int ( input () )
while numCases:
    textInput = input ()
    if textInput == "":
        break
    inputs = textInput.split ()
    xO = int ( inputs [ 0 ] )
    x = xO
    yO = int ( inputs [ 1 ] )
    y = yO
    temp = 0
    if y < x:
        temp = x
        x = y
        y = temp
    maxCycles = 1
    if x == y:        
        temp = RunCollatz ( z )
        if temp > maxCycles:
            maxCycles = temp
    for z in range ( x, y ):
        temp = RunCollatz ( z )
        if temp > maxCycles:
            maxCycles = temp
    print ( str ( xO ) + " " + str ( yO ) + " " + str ( maxCycles ) )
    numCases -= 1