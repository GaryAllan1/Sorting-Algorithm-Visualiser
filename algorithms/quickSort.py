import time
PURPLE = '#BF01FB'
DARK_BLUE = '#4204CC'
YELLOW = '#F7E806'
BLUE = '#0CA8F6'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
RED = '#F22810'

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    # drawData(data, getColourArray(len(data), head, tail, border, border))
    # time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] <= pivot:

            drawData(data, getColourArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            
            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColourArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    drawData(data, getColourArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    return border

def quicksort(data, low, high, drawData, timeTick):
    if low < high:
        pivot = partition(data, low, high, drawData, timeTick)
      #  drawData(data, [PURPLE if x == pivot else BLUE for x in range(len(data))])
        quicksort(data, low, pivot - 1, drawData, timeTick)
        quicksort(data, pivot + 1, high, drawData, timeTick)

    drawData(data, [PINK for x in range(len(data))])

def getColourArray(dataLen, head, tail, border, currIdx, isSwapping=False):
    colour_array = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colour_array.append(BLUE)
        else:
            colour_array.append(PINK)

        if i == tail:
            colour_array[i] = PURPLE
        elif i == border:
            colour_array[i] = RED
        elif i == currIdx:
            colour_array[i] = YELLOW

        # if isSwapping and (i == border or i == currIdx):
        #     colour_array[i] = LIGHT_GREEN

    return colour_array