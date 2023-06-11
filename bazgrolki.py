from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
#import Image, ImageDraw
#import PIL
#from PIL import Image, ImageTk


bg_color = '#FFFFFF'
color = '#FF0000'
MAXX = 490  # as for T. 1480
MAXY = 300  # as for T. 900
ereaser = False


def mouse_press(event):
    global prev
    prev = event
    '''--just to check event valls, for debuggin
    print(f'type: {event.type}')
    print(f'widget: {event.widget}')
    print(f'num: {event.num}')
    print(f'x: {event.x}')
    print(f'y: {event.y}')
    print(f'x_root: {event.x_root}')
    print(f'y_root: {event.y_root}')'''


def draw(event):
    global prev
    global color
    global ereaser
    '''print(f'event.x: {event.x}')
    print(f'event.x: {event.y}')
    print(f'color: {color}')'''
    if not ereaser:
        line = canvas.create_line(
            prev.x, prev.y, event.x, event.y, width=5, fill=color)
    else:
        oval = canvas.create_oval(
            event.x-50, event.y-50, event.x+50, event.y+50, fill=bg_color, outline=bg_color)
    prev = event


def drawpoints(event, num=2):
    global ereaser

    if ereaser:
        oval = canvas.create_oval(event.x-20, event.y-20,
                                  event.x+20, event.y+20, fill=bg_color, outline=bg_color)
    else:
        oval = canvas.create_oval(event.x-2, event.y-2,
                                  event.x+2, event.y+2, fill='red', outline='red')


def drawdotts(event, num=1):
    global ereaser
    ereaser = False
    rect = canvas.create_rectangle(
        event.x-num, event.y-num, event.x+num, event.y+num, fill='green', outline='green')


def erease():
    '''for debugging'''
    print(f'<from B4 circle>')
    global ereaser
    ereaser = True


def clearall():
    global ereaser
    ereaser = False
    screen = canvas.create_rectangle(0, 0, MAXX, MAXY, fill=bg_color)


def colorpicker():
    global ereaser
    ereaser = False
    global color
    clr = colorchooser.askcolor(title='select color')
    if clr[1] is not None:
        color = clr[1]

def bgchange():
    global ereaser
    ereaser=False
    global bg_color
    clr = colorchooser.askcolor(title='Select New Background Color')
    if clr[1] is not None:
        bg_color=clr[1]
        clearall()

def tofile():
    #img = Image.new("RGB", (MAXX, MAXY),white)
    #draw = ImageDraw.Draw(img)
    #filename = 'file_to_save.jpg'
    #img.save(filename)
    pass

if __name__ == '__main__':
    root = Tk()
    root.title("BAZGROŁki")
    root.iconbitmap('img//car.ico')

    delete = PhotoImage(file='img\\basket.png')
    btn1 = Button(root, text='Clear All',
                  command=clearall, fg='#F1A617', bg='#456782', font=('Arial', 16, 'bold'))
    btn1.grid(row=0, column=0, stick='nwe')
    btn1.config(image=delete,compound='left')

'''---custom style for ttk.Button
    clear_button = ttk.Button(root, text='Clear All', command=clearall)
    clear_button.grid(row=1, column=0, stick='n')
    style = ttk.Style()
    style.map('Large.TButton', foreground=[
              ('pressed', 'pink'), ('disabled', 'lightblue')])
    style.configure('Large.TButton', font=(
        'Courier', 24, 'bold'), background='red')
    clear_button.config(style='Large.TButton')
    '''
# print(clear.winfo_class())
# print(style.theme_use())
# print(clear_button.winfo_class())

rainbow = PhotoImage(file='img\\color_wheel.png')
btn2 = Button(root, text='Change Color', command=colorpicker,
              fg='#F1A617', bg='#456782', font=('Arial', 16, 'bold'))
btn2.grid(row=1, column=0, stick='nwe')
btn2.config(image=rainbow, compound='left')

rubber = PhotoImage(file='img\\rubber.png')
btn3 = Button(root, text='Ereaser',
              command=erease, fg='#F1A617', bg='#456782', font=('Arial', 16, 'bold'))
btn3.grid(row=2, column=0, stick='nwe')
btn3.config(image=rubber, compound='left')

bg_change = PhotoImage(file='img\\rubber.png')
btn4 = Button(root, text='Change Background',
              command=bgchange, fg='#F1A617', bg='#456782', font=('Arial', 16, 'bold'))
btn4.grid(row=3, column=0, stick='nwe')
btn4.config(image=bg_change, compound='left')

bg_change = PhotoImage(file='img\\rubber.png')
#btn5 = Button(root, text='Save File',
#              command=tofile, fg='#F1A617', bg='#456782', font=('Arial', 16, 'bold'))
#btn5.grid(row=3, column=0, stick='nwe')
#btn5.config(image=bg_change, compound='left')

canvas = Canvas(root, width=MAXX, height=MAXY, background=bg_color)
canvas.grid(row=0, column=1, stick='news', rowspan=3)
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<B2-Motion>', drawdotts)
canvas.bind('<B3-Motion>', drawpoints)
#canvas.bind('<Button-4>', circle)
#canvas.bind('<Button-5>', circle)


root.mainloop()
