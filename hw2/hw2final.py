fileOpen = open('input23.txt', 'r')
fileOut = open('output23.txt', 'w')
lahsaApplicantList, splaApplicantList, allApplicantList, lahsaSplaSatisfiedList, lahsaSatisfiedList, splaSatisfiedList = [], [], [], [], [], []
splaDayList, lahsaDayList, splaPickUpList = [], [], []

class Node:
    def __init__(self, splaVal, lahsaVal, backtrackSplaVal, backtrackLahsaVal, ids):
        self.splaVal = splaVal
        self.lahsaVal = lahsaVal
        self.backtrackSplaVal = backtrackSplaVal
        self.backtrackLahsaVal = backtrackLahsaVal
        self.ids = ids

def addition(daysList, days):
    i = 0
    for char in days:
        daysList[i] += int(char)
        i += 1
    return daysList

def compatibility(iterableList, days, limit):
    i = 0
    for char in days:
        if iterableList[i] == limit and int(char) == 1:
            return False
        i += 1
    return True

def comparison(node_backtrackSplaVal, backtrackSpla, node_backtrackLahsaVal, backtrackLahsa, playerName):
    if playerName == "lahsa":
        if backtrackSpla > node_backtrackSplaVal:
            return backtrackSpla, backtrackLahsa
        elif backtrackSpla == node_backtrackSplaVal:
            if backtrackLahsa > node_backtrackLahsaVal:
                return backtrackSpla, backtrackLahsa
            else:
                return node_backtrackSplaVal, node_backtrackLahsaVal
        else:
            return node_backtrackSplaVal, node_backtrackLahsaVal
    else:
        if backtrackLahsa > node_backtrackLahsaVal:
            return backtrackSpla, backtrackLahsa
        elif backtrackLahsa == node_backtrackLahsaVal:
            if backtrackSpla > node_backtrackSplaVal:
                return backtrackSpla, backtrackLahsa
            else:
                return node_backtrackSplaVal, node_backtrackLahsaVal
        else:
            return node_backtrackSplaVal, node_backtrackLahsaVal

def countDays(iterableList, allApplicantList, iterableDayList):
    for ids in iterableList:
        for details in allApplicantList:
            if ids == details[:5]:
                string = details[13:]
                i = 0
                for char in string:
                    iterableDayList[i] += int(char)
                    i += 1
    return iterableDayList

def countMaxDays(maxDaysIterableList, iterableList, limit):
    for day in iterableList:
        if day == limit:
            maxDaysIterableList -= 1
    if maxDaysIterableList == 0:
        fileOut.write("00000")
        exit()
    else:
        return maxDaysIterableList

#spla
def minimaxSpla(startIndex, splaDaysList, lahsaDaysList, path):
        splaTurnSplaVal, splaTurnLahsaVal = sum(splaDaysList), sum(lahsaDaysList)
        if startIndex == len(newSplaList):
            return sum(splaDaysList), sum(lahsaDaysList)
        for details in newSplaList[startIndex:]:
            if details[:5] in path:
                    continue
            if compatibility(splaDaysList, details[5:], spacesParking) == True:
                i = newSplaList.index(details)
                path.append(details[:5])
                additionSplaList = addition(splaDaysList[:], details[5:])
                node = Node(sum(additionSplaList[:]), sum(lahsaDaysList), sum(additionSplaList[:]), sum(lahsaDaysList), details[:5])
                if (i + 1) < len(splaPickUpList):
                    backtrackSpla, backtrackLahsa = minimaxLahsa(0, additionSplaList[:], lahsaDaysList[:], path)
                else:
                    backtrackSpla, backtrackLahsa = minimaxSpla(i + 1, additionSplaList[:], lahsaDaysList[:], path)
                node.backtrackSplaVal, node.backtrackLahsaVal = comparison(node.backtrackSplaVal, backtrackSpla, node.backtrackLahsaVal, backtrackLahsa, "spla")
                path.pop()
                if node.backtrackSplaVal > splaTurnSplaVal:
                    splaTurnSplaVal = node.backtrackSplaVal
                    splaTurnLahsaVal = node.backtrackLahsaVal
        return splaTurnSplaVal, splaTurnLahsaVal
#lahsa
def minimaxLahsa(startIndex, splaDaysList, lahsaDaysList, path):
    lahsaTurnSplaVal, lahsaTurnLahsaVal = sum(splaDaysList), sum(lahsaDaysList)
    if startIndex == len(newLahsaList):
        return sum(splaDaysList), sum(lahsaDaysList)
    for details in newLahsaList[startIndex:]:
        if details[:5] in path:
                continue
        if compatibility(lahsaDaysList, details[5:], noOfBeds) == True:
            i = newLahsaList.index(details)
            path.append(details[:5])
            additionLahsaList = addition(lahsaDaysList[:], details[5:])
            node = Node(sum(splaDaysList), sum(additionLahsaList[:]), sum(splaDaysList), sum(additionLahsaList[:]), details[:5])
            if (i + 1) < len(splaPickUpList):
                backtrackSpla, backtrackLahsa= minimaxSpla(0, splaDaysList[:], additionLahsaList[:], path)
                node.backtrackSplaVal, node.backtrackLahsaVal = comparison(node.backtrackSplaVal, backtrackSpla, node.backtrackLahsaVal, backtrackLahsa, "lahsa")
            else:
                backtrackSpla, backtrackLahsa= minimaxSpla(0, splaDaysList[:], additionLahsaList[:], path)
                node.backtrackSplaVal, node.backtrackLahsaVal = comparison(node.backtrackSplaVal, backtrackSpla, node.backtrackLahsaVal, backtrackLahsa, "lahsa")
            if backtrackSpla == sum(splaDaysList) and backtrackLahsa == sum(additionLahsaList):
                backtrackSpla, backtrackLahsa = minimaxLahsa(0, splaDaysList[:], additionLahsaList[:], path)
                node.backtrackSplaVal, node.backtrackLahsaVal = comparison(node.backtrackSplaVal, backtrackSpla, node.backtrackLahsaVal, backtrackLahsa, "lahsa")
            if node.backtrackLahsaVal > lahsaTurnLahsaVal:
                lahsaTurnSplaVal = node.backtrackSplaVal
                lahsaTurnLahsaVal = node.backtrackLahsaVal

            path.pop()
    return lahsaTurnSplaVal, lahsaTurnLahsaVal

with fileOpen as inputFile:
    daysListSpla, daysListLahsa = [0]*7, [0]*7
    lines = inputFile.readlines()

    noOfBeds = int(lines[0])
    spacesParking = int(lines[1])

    lahsaApplicants = int(lines[2])
    i = 2
    for i in range(3, 3 + lahsaApplicants):
        lahsaApplicantList.append(str(lines[i]).rstrip())

    j = i+1
    splaApplicants = int(lines[j])
    k = j
    for k in range(j+1, j+1 + splaApplicants):
        splaApplicantList.append(str(lines[k]).rstrip())

    i = k+1
    totalApplicants = int(lines[i])
    for k in range(i+1, i + 1+totalApplicants):
        allApplicantList.append(str(lines[k]).rstrip())

    for details in allApplicantList:
        ids = details[:5]
        if ids in lahsaApplicantList or ids in splaApplicantList:
            continue
        if details[5:6] == "F" and int(details[7:9]) > 17 and details[9:10] == "N":
            if details[10:13] == "NYY":
                lahsaSplaSatisfiedList.append(details[:5]+details[13:])
            else:
                lahsaSatisfiedList.append(details[:5]+details[13:])
        elif details[10:13] == "NYY" and (details[5:6] != "F" or int(details[7:9]) <= 17 or details[9:10] != "N"):
            splaSatisfiedList.append(details[:5]+details[13:])

    splaDayList = countDays(splaApplicantList, allApplicantList, daysListSpla)
    lahsaDayList = countDays(lahsaApplicantList, allApplicantList, daysListLahsa)
    maxEfficiency = sum(daysListSpla)

    maxDaysSpla = countMaxDays(7, daysListSpla, spacesParking)
    maxDaysLahsa = countMaxDays(7, daysListLahsa, noOfBeds)

    for details in lahsaSplaSatisfiedList:
        days = details[5:]
        i = 0
        for j in days:
            canTake = False
            if daysListLahsa[i] == noOfBeds and int(j) == 1:
                canTake == True
                if daysListSpla[i] == spacesParking and int(j) == 1:
                    canTake = False
                    break
            i += 1
        if canTake == True:
            splaSatisfiedList.append(details)

    for details in lahsaSplaSatisfiedList:
        count = 0
        days = details[5:]
        i = 0
        for j in days:
            if (daysListLahsa[i] != noOfBeds) or (daysListLahsa[i] == noOfBeds and int(j) == 0):
                count += 1
            i += 1

        i = 0
        if count == 7:
            count = 0
            for j in days:
                if (daysListSpla[i] != spacesParking) or (daysListSpla[i] == spacesParking and int(j) == 0):
                    count += 1
                i += 1
            if count == 7:
                splaPickUpList.append(details)

    # sorting of lists
    splaPickUpList = sorted(splaPickUpList, key = lambda x: int(str(x)[:5]))
    lahsaSatisfiedList = sorted(lahsaSatisfiedList, key = lambda x: int(str(x)[:5]))
    splaSatisfiedList = sorted(splaSatisfiedList, key = lambda x: int(str(x)[:5]))
    newSplaList = splaPickUpList + splaSatisfiedList
    newLahsaList = splaPickUpList + lahsaSatisfiedList

    finalSplaVal, finalLahsaVal = sum(splaDayList), sum(lahsaDayList)

if newSplaList == []:
    fileOut.write("00000")
    exit()
finalId = (newSplaList[0])[:5]
for details in newSplaList:
    path = []
    additionSplaList = addition(splaDayList[:], details[5:])
    node = Node(sum(additionSplaList), sum(lahsaDayList), sum(additionSplaList), sum(lahsaDayList), details[:5])
    i = newSplaList.index(details)
    path.append(details[:5])
    if i + 1 < len(splaPickUpList):
        backtrackSpla, backtrackLahsa = minimaxLahsa(0, additionSplaList[:], lahsaDayList[:], path)
    else:
        backtrackSpla, backtrackLahsa= minimaxSpla(0, additionSplaList[:], lahsaDayList[:], path)
    node.backtrackSplaVal, node.backtrackLahsaVal = comparison(node.backtrackSplaVal, backtrackSpla, node.backtrackLahsaVal, backtrackLahsa, "spla")
    if node.backtrackSplaVal > finalSplaVal:
        finalSplaVal = node.backtrackSplaVal
        finalLahsaVal = node.backtrackLahsaVal
        finalId = details[:5]
    path.pop()
fileOut.write(finalId)