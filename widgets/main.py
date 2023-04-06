import tkinter as tk
from parts import TopFrame, MedianFrame
# create canvas with tkinter
# paint image in canvas using tkinter


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = TopFrame(self)
        topFrame.pack()
        medianFrame = MedianFrame(self, borderwidth=0)
        medianFrame.pack(fill=tk.X)

    def radioButtonEventOMedianFrame(self,radioButtonValue):
        print(radioButtonValue)

def main():
    window = Window()
    window.title("widgets")
    window.mainloop()


if __name__ == "__main__":
    main()
