from tkinter import *
from tkinter import ttk
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.insertionSort import insertion_sort
from algorithms.quickSort import quicksort
from useful_colours import *
import random

window = Tk()
window.title("Sorting Algorithm Visualiser")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Quicksort']

data = []
NO_ITEMS = 50

def drawData(data, colourArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width/ (len(data) + 1)
    offset = 4
    spacing = 2
    normalized_data = [i/max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colourArray[i])

    window.update_idletasks()


def generate():
    global data

    data = []
    for i in range(0, NO_ITEMS):
        random_value = random.randint(1,150)
        data.append(random_value)

    drawData(data, ['#0CA8F6' for x in range(len(data))])


def sort():
    global data
    timeTick = 0.01

    if alg_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, timeTick)
    elif alg_menu.get() == "Merge Sort":
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif alg_menu.get() == "Insertion Sort":
        insertion_sort(data, drawData, timeTick)
    elif alg_menu.get() == "Quicksort":
        quicksort(data, 0, len(data) - 1, drawData, timeTick)


# UI From here
UI_frame = Frame(window, width=900, height=300, bg='#FFFFFF')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

selectSortLabel = Label(UI_frame, text="Algorithm: ", bg='#FFFFFF')
selectSortLabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)
alg_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
alg_menu.grid(row=0, column=1, padx=5, pady=5)
alg_menu.current(0)

sort_button = Button(UI_frame, text="Sort", command=sort, bg='#C4C5BF')
sort_button.grid(row=2, column=1, padx=5, pady=5)

generate_array_button = Button(UI_frame, text="Generate Array", command=generate, bg='#C4C5BF')
generate_array_button.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg='#FFFFFF')
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
