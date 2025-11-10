from keypad_functions import opr, conv
from sim_data import low_lim, up_lim
from tkinter import *

import numpy as np
import random
import serial
import time


# Initiate window
interface = Tk()
# Tkinter color chart: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
interface.configure(background = "honeydew3")
interface.title("MDAS Calculator")
# Window size
interface.geometry('475x221')

# int2 = Toplevel(interface)
# int2.geometry('280x180')
# int2.title("Calculator Screen")

int3 = Toplevel(interface)
int3.geometry('250x221')
int3.title("Sending Info")
bgcolor = "slate gray"
int3.config(bg = bgcolor)

# int3 = Toplevel(interface)
# int3.geometry('180x100')

serial_comm = serial.Serial("COM8", 57600, timeout = 1)
time.sleep(2)


# int3 = Toplevel(interface)
# int3.geometry('180x100')

# serial_comm = serial.Serial("COM8", 57600, timeout = 1)
# time.sleep(2)

xstart = 274
ystart = 20

def entval(val):
    # text_value = text.get()
    if val == 1:
        gen = random.randint(low_lim[0], up_lim[0])
        # return gen1
        # print(gen1)
    
    elif val == 2:
        gen = random.randint(low_lim[1], up_lim[1])
        # return gen1
        # print(gen1)

    elif val == 3:
        gen = random.randint(low_lim[2], up_lim[2])
        # return gen1
        # print(gen1)

    elif val == 4:
        gen = random.randint(low_lim[3], up_lim[3])
        # return gen1
        # print(gen1)

    elif val == 5:
        gen = random.randint(low_lim[4], up_lim[4])
        # return gen1
        # print(gen1)

    elif val == 6:
        gen = random.randint(low_lim[5], up_lim[5])
        # return gen1
        # print(gen1)

    elif val == 7:
        gen = random.randint(low_lim[6], up_lim[6])
        # return gen1
        # print(gen1)
    
    elif val == 8:
        gen = random.randint(low_lim[7], up_lim[7])
        # return gen1
        # print(gen1)

    elif val == 9:
        gen = random.randint(low_lim[8], up_lim[8])
        # return gen1
        # print(gen1)

    elif val == 10:
        gen = random.randint(low_lim[9], up_lim[9])
        # return gen1
        # print(gen1)

    elif val == 11:
        gen = random.randint(low_lim[10], up_lim[10])
        # return gen1
        # print(gen1)
    
    elif val == 12:
        gen = random.randint(low_lim[11], up_lim[11])
        # return gen1
        # print(gen1)

    elif val == 13:
        gen = random.randint(low_lim[12], up_lim[12])
        # return gen1
        # print(gen1)

    elif val == 14:
        gen = random.randint(low_lim[13], up_lim[13])
        # return gen1
        # print(gen1)

    elif val == 15:
        gen = random.randint(low_lim[14], up_lim[14])
        # return gen1
        # print(gen1)

    elif val == 16:
        gen = random.randint(low_lim[15], up_lim[15])
        # return gen1
        # print(gen1)

    # now = label1.cget("text")
    # label1.config(text = now + gen)
    # label1.config(text = "{} mV".format(gen))
    # label2.config(text = "SENT")
    label3.config(text = "{} mV".format(gen))
    label4.config(text = "SENT")
    int3.after(2000, lambda : label4.config(text = ""))
    serial_comm.write(f'{gen}\n'.encode())

    info = ""
    while info == "":
        info = serial_comm.readline().decode().strip()
    gen_ = conv(int(info))
    # print(info)
    
    if gen_ == "=":
        u = label1.cget("text")
        # if "++"
        
        ans = opr(u)
        if ans == "Syntax ERROR":
            label2.config(text = ans, font = ("Helvetica", 20, "bold"))
        elif ans == "Division by zero!":
            label2.config(text = ans, font = ("Helvetica", 15, "bold"))
        elif ans == "Undefined":
            label2.config(text = ans, font = ("Helvetica", 20, "bold"))
        else:
            ans_ = str(ans)
            if len(ans_) > 11:
                ans_ = ans_[:11]
            label2.config(text = ans_, font = ("Helvetica", 25, "bold"))

    elif gen_ == "AC":
        label1.config(text = "")
        label2.config(text = "", font = ("Helvetica", 25, "bold"))
    else:
        now = label1.cget("text")
        label1.config(text = now + gen_)

    # int2.after(2000, lambda : label2.config(text = ""))
    # serial_comm.write(f'{gen}\n'.encode())

    # info = ""
    # while info == "":
    #     info = serial_comm.readline().decode().strip()
    # print(info)

    # time.sleep(0.5)
    # while serial_comm.in_waiting > 0:
    #     info = serial_comm.readline().decode().strip()
    #     print(info)

# def
# # Text Entry
# text = Entry(interface)
# text.place(x = 20, y = 20, width = 181, height = 50)

# Text Entry
label1 = Label(interface, bg = "white", font = ("Helvetica", 15), wraplength = 200, anchor = "e")
label1.place(x = 20, y = 20, width = 240, height = 101)

label2 = Label(interface, bg = "black", font = ("Helvetica", 25, "bold"), fg = "green")
label2.place(x = 20, y = 141, width = 240, height = 60)



label3 = Label(int3, bg = "white", font = ("Helvetica", 25))
label3.place(x = 20, y = 43, width = 210, height = 60)
label3_ = Label(int3, bg = bgcolor, font = ("Helvetica", 10, "bold"), fg = "white", anchor = "w")
label3_.place(x = 20, y = 15, width = 210, height = 20)
label3_.config(text = "Analog Voltage")
# text_3 = Text(int3, width = 210, height = 20)
# text_3.insert("1.0", "Analog Voltage")
# text_3.config(font = ("Helvetica", 20, "bold"), fg = "white")


label4 = Label(int3, bg = "black", font = ("Helvetica", 25, "bold"), fg = "green")
label4.place(x = 20, y = 138, width = 210, height = 60)
label4_ = Label(int3, bg = bgcolor, font = ("Helvetica", 10, "bold"), fg = "white", anchor = "w")
label4_.place(x = 20, y = 115, width = 210, height = 20)
label4_.config(text = "Status")
# text_4 = Text(int3, width = 210, height = 20)
# text_4.insert("1.0", "Status")
# text_4.config(font = ("Helvetica", 20, "bold"), fg = "white")

# Buttons
# Button dimensions
bx, by = 40, 40

# Row 1
def entval1():
    return entval(1)
button11 = Button(interface,
                  text = "1",
                  font = ("Helvetica", 15),
                  command = entval1
                 )
button11.place(x = xstart, y = ystart, width = bx, height = by)

def entval2():
    return entval(2)
button12 = Button(interface,
                  text = "2",
                  font = ("Helvetica", 15),
                  command = entval2
                 )
button12.place(x = xstart + 7 + bx, y = ystart, width = bx, height = by)

def entval3():
    return entval(3)
button13 = Button(interface,
                  text = "3",
                  font = ("Helvetica", 15),
                  command = entval3
                 )
button13.place(x = xstart + 2 * 7 + 2 * bx, y = ystart, width = bx, height = by)

def entval4():
    return entval(4)
button14 = Button(interface,
                  text = "AC",
                  font = ("Helvetica", 15),
                  fg = "white",
                  bg = "red",
                  command = entval4
                 )
button14.place(x = xstart + 3 * 7 + 3 * bx, y = ystart, width = bx, height = by)

# Row 2
def entval5():
    return entval(5)
button21 = Button(interface,
                  text = "4",
                  font = ("Helvetica", 15),
                  command = entval5
                 )
button21.place(x = xstart, y = ystart + 7 + by, width = bx, height = by)

def entval6():
    return entval(6)
button22 = Button(interface,
                  text = "5",
                  font = ("Helvetica", 15),
                  command = entval6
                 )
button22.place(x = xstart + 7 + bx, y = ystart + 7 + by, width = bx, height = by)

def entval7():
    return entval(7)
button23 = Button(interface,
                  text = "6",
                  font = ("Helvetica", 15),
                  command = entval7
                 )
button23.place(x = xstart + 2 * 7 + 2 * bx, y = ystart + 7 + by, width = bx, height = by)

def entval8():
    return entval(8)
button24 = Button(interface,
                  text = "+",
                  font = ("Helvetica", 15),
                  fg = "white",
                  bg = "snow4",
                  command = entval8
                 )
button24.place(x = xstart + 3 * 7 + 3 * bx, y = ystart + 7 + by, width = bx, height = by)

# Row 3
def entval9():
    return entval(9)
button31 = Button(interface,
                  text = "7",
                  font = ("Helvetica", 15),
                  command = entval9
                 )
button31.place(x = xstart, y = ystart + 2 * 7 + 2 * by, width = bx, height = by)

def entval10():
    return entval(10)
button32 = Button(interface,
                  text = "8",
                  font = ("Helvetica", 15),
                  command = entval10
                 )
button32.place(x = xstart + 7 + bx, y = ystart + 2 * 7 + 2 * by, width = bx, height = by)

def entval11():
    return entval(11)
button33 = Button(interface,
                  text = "9",
                  font = ("Helvetica", 15),
                  command = entval11
                 )
button33.place(x = xstart + 2 * 7 + 2 * bx, y = ystart + 2 * 7 + 2 * by, width = bx, height = by)

def entval12():
    return entval(12)
button34 = Button(interface,
                  text = "–",
                  font = ("Helvetica", 15),
                  fg = "white",
                  bg = "snow4",
                  command = entval12
                 )
button34.place(x = xstart + 3 * 7 + 3 * bx, y = ystart + 2 * 7 + 2 * by, width = bx, height = by)

# Row 4
def entval13():
    return entval(13)
button41 = Button(interface,
                  text = "×",
                  font = ("Helvetica", 15),
                  fg = "white",
                  bg = "ivory4",
                  command = entval13
                 )
button41.place(x = xstart, y = ystart + 3 * 7 + 3 * by, width = bx, height = by)

def entval14():
    return entval(14)
button42 = Button(interface,
                  text = "0",
                  font = ("Helvetica", 15),
                  command = entval14
                 )
button42.place(x = xstart + 7 + bx, y = ystart + 3 * 7 + 3 * by, width = bx, height = by)

def entval15():
    return entval(15)
button43 = Button(interface,
                  text = "/",
                  font = ("Helvetica", 15),
                  fg = "white",
                  bg = "ivory4",
                  command = entval15
                 )
button43.place(x = xstart + 2 * 7 + 2 * bx, y = ystart + 3 * 7 + 3 * by, width = bx, height = by)

def entval16():
    return entval(16)
button44 = Button(interface,
                  text = "=",
                  font = ("Helvetica", 15),
                  fg = "white",
                  bg = "snow4",
                  command = entval16
                 )
button44.place(x = xstart + 3 * 7 + 3 * bx, y = ystart + 3 * 7 + 3 * by, width = bx, height = by)


interface.mainloop()

# while True:
#     if serial_comm.in_waiting > 0:
#         line = serial_comm.readline().decode().strip()
#         print(line)
#         break  # Stop after reading one response

# while serial_comm.in_waiting > 0:
#     info = serial_comm.readline().decode().strip()
#     print(info)

serial_comm.close()