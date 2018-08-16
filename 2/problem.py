def main():
    inArray = [1,2,3,4,5]
    total = 1
    outArray = []
    for range in inArray:
        total *=range
    print inArray
    for range in inArray:
        outArray.append(total/range)
    print outArray
main()
