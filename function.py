def getBestColours(parent, number):
    ratio = []
    if(len(parent) < number):
        number = len(parent)

    for i in range(0, len(parent)):
        ratio.append(parent[i]['ratio'])

    ratio.sort(reverse=True)

    resultColor = []

     # COMPARE WITH ORIGINAL JSON
    for i in range(0, len(ratio)):
         for j in range(0, len(parent)):
              if(ratio[i] == parent[j]):
                   resultColor.append(parent[j]['colorGeneralCategory'])

    return resultColor

def getBestStyles(parent, number):
    confidence = []
    if(len(parent) < number):
        number = len(parent)

    for i in range(0, len(parent)):
        confidence.append(parent[i]['confidence'])

    confidence.sort(reverse=True)

    resultStyles = []

     # COMPARE WITH ORIGINAL JSON
    for i in range(0, len(confidence)):
         for j in range(0, len(parent)):
              if(confidence[i] == parent[j]):
                   resultStyles.append(parent[j]['styleName'])

    return resultStyles

def getBestGarments(parent, number): 
    if(len(parent) < number):
        numbers = len(parent)
 
    confidence = []

    for i in range(0, len(parent)):
        confidence.append(parent[i]['confidence'])
        
    confidence.sort(reverse=True)

     resultGarment = []

     # COMPARE WITH ORIGINAL JSON
    for i in range(0, len(confidence)):
         for j in range(0, len(parent)):
              if(confidence[i] == parent[j]):
                   resultGarment.append(parent[j]['typeName'])

    return resultGarment
