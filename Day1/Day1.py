import sys

# Day 1: 2024

leftColumn = []
rightColumn = []

with open(sys.argv[1]) as file:
        while line := file.readline():
                    lineVals = line.split()
                    leftColumn.append(int(lineVals[0]))
                    rightColumn.append(int(lineVals[1]))

leftColumn.sort()
rightColumn.sort()

distanceSum = 0
similarityScore = 0

i = 0
for rowElement in leftColumn:
    distance = abs(rowElement - rightColumn[i])
    distanceSum += distance
    similarityScore += (rowElement * rightColumn.count(rowElement))
    i+=1


print("Distance Sum: " + str(distanceSum))
print("Similarity Score: " + str(similarityScore))
