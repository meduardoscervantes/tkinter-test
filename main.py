import pandas as pd
import time
from threading import Thread
from tkinter import *
from random import randint
from datetime import datetime
def getRandomDf():
    time.sleep(randint(2,10))
    return pd.DataFrame([[randint(1,100) for y in range(10)] for x in range(10)], columns=[f'c{x}' for x in range(10)])


class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('1100x700')
        self.main.title('Top Ten At Home Thing')

        # Text
        l = Label(self.main, text='FOR SYSTEM AWARENESS ONLY')
        l.config(font=("Courier", 15), foreground='red')
        l.pack()

        # Frame 1
        self.f1_master = f = Frame(self.main)
        f.pack()
        self.f1 = f = Frame(self.f1_master)
        f.pack()

        # Frame 2
        self.f2_master = f = Frame(self.main)
        f.pack()
        self.f2 = f = Frame(self.f2_master)
        f.pack()

        self.start()
        return
    
    def getTkTable(self, frame):
        df = getRandomDf()
        # Frame 1
        frame1 = Frame(frame)

        # Frame 2
        frame2 = Frame(frame1)
        frame2.pack(pady=5,padx=5)
        
        l = Label(frame2, text=str(datetime.now()))
        l.config(font=("Courier", 15), foreground='red')
        l.pack()

        frame3 = Frame(frame1)
        frame3.pack(pady=5,padx=5)
        for i,x in enumerate(df):
            Label(frame3, text=x).grid(row=0, column=i, sticky=W, padx=2, pady=2)
            for j,y in df.iterrows():
                if df.at[j,x] > 50 and df.at[j,x] < 80:
                    Label(frame3, text=df.at[j,x], bg="orange").grid(row=j+1, column=i, sticky=W, padx=2, pady=2)
                elif df.at[j,x] > 80:
                    Label(frame3, text=df.at[j,x], bg="red").grid(row=j+1, column=i, sticky=W, padx=2, pady=2)
                else:
                    Label(frame3, text=df.at[j,x]).grid(row=j+1, column=i, sticky=W, padx=2, pady=2)

        return frame1
    
    def updateF1(self):
        while True:
            print('Starting update F1')
            f = self.getTkTable(self.f1_master)
            self.f1.destroy()
            self.f1 = f
            self.f1.pack()
            print('Complete update F1')
            if self.stop == True:
                break
        return
    
    def updateF2(self):
        while True:
            print('Starting update F2')
            f = self.getTkTable(self.f2_master)
            self.f2.destroy()
            self.f2 = f
            self.f2.pack()
            print('Complete update F2')
            if self.stop == True:
                break
        return

    def start(self):
        self.stop = False
        t1 = Thread(target=self.updateF1)
        t2 = Thread(target=self.updateF2)
        t1.start()
        t2.start()

    def stop(self):
        self.stop = True
        return

App().mainloop()


