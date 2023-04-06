from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk


class TopFrame(ttk.LabelFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # using ttk.Style to change the style of the self widget
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('xpnative')
        # ttkStyle change ttk.LabelFrame border width
        ttkStyle.configure('TLabelframe', borderwidth=0)
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        self.canvas = tk.Canvas(self, width=500, height=200)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.flowerPhoto1, anchor='nw')
        self.canvas.create_text(87, 200, text='init', fill='yellow',
                                font=('italic', 36), anchor='s')

        diamondImage1 = Image.open("./images/diamond.png")
        self.diamondPhoto1 = ImageTk.PhotoImage(diamondImage1)
        self.canvas.create_image(175, 5, image=self.diamondPhoto1, anchor='nw')

        # created ttk.scrollbar of tkinter in canvas
        self.scrollbar = ttk.Scrollbar(
            self, orient='horizontal', command=self.canvas.xview)
        self.scrollbar.pack(side='bottom', fill='x')
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.configure(scrollregion=(0, 0, 500, 200))


class MedianFrame(ttk.LabelFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # create ttk.radiobuttons in self
        # using ttk.Style to change the style of the self widget
        self.window = master
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('xpnative')
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.RIGHT, padx=10, pady=10)
        self.radioStringVar = tk.StringVar()
        self.radiobutton1 = ttk.Radiobutton(
            radionFrame, text='Option 1', variable=self.radioStringVar, value='red', command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(
            radionFrame, text='Option 2', variable=self.radioStringVar, value='blue', command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(
            radionFrame, text='Option 3', variable=self.radioStringVar, value='yellow', command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(
            radionFrame, text='Option 4', variable=self.radioStringVar, value='green', command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set('red')

       # create event of ttk.radionbuttons
        # self.radiobutton1.bind('<Button-1>', self.radioEvent)
        # self.radiobutton2.bind('<Button-1>', self.radioEvent)
        # self.radiobutton3.bind('<Button-1>', self.radioEvent)
        # self.radiobutton4.bind('<Button-1>', self.radioEvent)

     # create ttk.checkbuttons in self
        checkFrames = ttk.LabelFrame(self, text='Check Buttons')
        checkFrames.pack(side=tk.RIGHT, padx=10, pady=10)

        self.checkStringVar = tk.StringVar()
        self.checkbutton1 = ttk.Checkbutton(
            checkFrames, text='Option 1', variable=self.checkStringVar, command=self.checkEvent, offvalue='op1check', onvalue='op1')
        self.checkbutton1.pack()
        self.checkbutton2 = ttk.Checkbutton(
            checkFrames, text='Option 2', variable=self.checkStringVar, command=self.checkEvent, offvalue='op2check', onvalue='op2')
        self.checkbutton2.pack()
        self.checkbutton3 = ttk.Checkbutton(
            checkFrames, text='Option 3', variable=self.checkStringVar, command=self.checkEvent, offvalue='op3check', onvalue='op3')
        self.checkbutton3.pack()
        self.checkbutton4 = ttk.Checkbutton(
            checkFrames, text='Option 4', variable=self.checkStringVar, command=self.checkEvent, offvalue='op4check', onvalue='op4')
        self.checkbutton4.pack()
        self.checkStringVar.set('Option 1')

    def checkEvent(self):
        print(self.checkStringVar.get())
        # self.w.radioButtonEventOfMedianFrame(self.checkStringVar.get())

    def radioEvent(self):
        self.window.radioButtonEventOMedianFrame(self.radioStringVar.get())
