class IntersectedArea:

    def __init__(self, id, interesctingCircleIds):
        self.id = id
        if interesctingCircleIds:
            self.interesctingCircleIds = set(interesctingCircleIds.split('|'))
        else:
            self.interesctingCircleIds = set()


intersectedAreas = [
    IntersectedArea('I1', 'C3'),
    IntersectedArea('I2', 'C2'),
    IntersectedArea('I3', 'C2|C3'),
    IntersectedArea('I4', 'C1'),
    IntersectedArea('I5', 'C1|C3'),
    IntersectedArea('I6', 'C2|C1'),
    IntersectedArea('I7', 'C1|C2|C3'),
    IntersectedArea('I8', 'C4'),
    IntersectedArea('I9', 'C4|C3'),
    IntersectedArea('I10', 'C4|C1'),
    IntersectedArea('I11', 'C1|C4|C3'),
    IntersectedArea('I12', 'C5'),
    IntersectedArea('I13', 'C5|C3'),
    IntersectedArea('I14', 'C5|C1|C3'),
    IntersectedArea('I15', 'C4|C5'),
    IntersectedArea('I16', 'C4|C5|C3'),
    IntersectedArea('I17', 'C1|C4|C3|C5'),

]



def getBestCandidate(intersectedAreas, currentUnion):

    currentBestIntersectedArea = IntersectedArea(0, '')
    for intersectedArea in intersectedAreas:
        if len(currentUnion.union(intersectedArea.interesctingCircleIds)) > len(currentUnion.union(currentBestIntersectedArea.interesctingCircleIds)):
            currentBestIntersectedArea = intersectedArea

    return currentBestIntersectedArea



finalIntersectedAreas = []
currentUnionOfCircles = set()

for i in range(len(intersectedAreas)):
    currentBestCandidate = getBestCandidate(intersectedAreas, currentUnionOfCircles)

    if currentBestCandidate.interesctingCircleIds:
        currentUnionOfCircles = currentUnionOfCircles.union(currentBestCandidate.interesctingCircleIds)
        finalIntersectedAreas.append(currentBestCandidate)



print('Minimized intersectedArea list covering all circles')
for area in finalIntersectedAreas:
    print(area.id, area.interesctingCircleIds)
print()

print('Union of intersected circles')
print(currentUnionOfCircles)