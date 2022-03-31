import time
BLUE = '#0CA8F6'

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key <= data[j]:
            drawData(data, ['#F7E806' if x == j else '#0CA8F6' for x in range(len(data))])
            time.sleep(timeTick)
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key

    drawData(data, ['#0CA8F6' for x in range(len(data))])