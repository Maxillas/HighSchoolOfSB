def GenerateBBSTArray(a: list):
    orderedMas = a
    orderedMas.sort()
    output = [None] * len(orderedMas)

    def rounder(massive, index):
        centerIndex = (int)(len(massive) / 2)
        output[index] = massive[centerIndex]
        leftPart = massive[:centerIndex]

        if len(leftPart) > 0:
            leftChildIndex = index * 2 + 1
            rounder(leftPart, leftChildIndex)

        rightPart = massive[centerIndex + 1:]
        if len(rightPart) > 0:
            rightChildIndex = index * 2 + 2
            rounder(rightPart, rightChildIndex)
        return

    rounder(orderedMas, 0)
    return output