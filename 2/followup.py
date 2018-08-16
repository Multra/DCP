def main():
    inArray = [1,2,3,4,5]
    total = 1
    outArray = []
    for outRange in range(len(inArray)):
        for inRange in range(len(inArray)):
            if inArray[outRange] != inArray[inRange]:
                total *= inArray[inRange]
        outArray.append(total)
        total = 1
    print outArray
main()
