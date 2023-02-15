import tkinter
import customtkinter
import time

lines = 0.0
texthere = ''

# First part of an app

def mainapp(title, size):
    customtkinter.CTk().geometry(size).title(title)
    root = customtkinter.CTk()
    root.geometry(size)
    root.title(title)
    root.resizable(False)

# Window Theme

def defaulttheme(theme, color):
    customtkinter.set_appearance_mode(theme)
    customtkinter.set_default_color_theme(color)

# HDPI Support

def hdpisupport(mode):
    if mode == True:
        time.sleep(0)
    elif mode == False:
        customtkinter.deactivate_automatic_dpi_awareness()
    else:
        print('Error: {} not supported'.format(mode))

# Frame

def frame(master, lar, alt, cradius, px, py, sti, mode, framename):
    framename = customtkinter.CTkFrame(master, width=lar, height=alt, corner_radius=cradius)

    if mode == 'pack':
        framename.pack(padx=px, pady=py, sticky=sti)
    elif mode == 'grid':
        framename.grid(row=px, column=py, sticky=sti)
    else:
        print('Error: {} not supported'.format(mode))

    # Textbox

def txtbox(master, px, py, mode, line, txt, state, textboxname):
    textboxname = customtkinter.CTkTextbox(master)
    textboxname.insert(line, txt)

    if mode == 'pack':
        textboxname.pack(padx=px, pady=py)
    elif mode == 'grid':
        textboxname.grid(row=px, column=py)
    else:
        print('Error: {} not supported'.format(mode))
        
    textboxname.config(state)
# Scrollbar

def scroll(master, mode, px, py, stick, text, scroll):
    text = tkinter.Text(master, highlightthickness=0)
    scroll = customtkinter.CTkScrollbar(master, command=text.yview)
    text.configure(yscrollcommand=scroll.set)

    if mode == 'pack':
        text.pack(padx=px, pady=py, sticky=stick)
        scroll.pack(padx=px, pady=py + 1, sticky=stick)
    elif mode == 'grid':
        text.grid(row=px, column=py, sticky=stick)
        scroll.pack(row=px, column=py + 1, sticky=stick)
    else:
        print('Error: {} not supported'.format(mode))

# Button

def button(master, text, command, px, py, mode, cradius, bradius, buttonname):
    buttonname = customtkinter.CTkButton(master, text=text, command=command, border_width=bradius, corner_radius=cradius)

    if mode == 'pack':
        buttonname.pack(padx=px, pady=py)
    elif mode == 'grid':
        buttonname.grid(row=px, column=py)
    else:
        print('Error: {} not supported'.format(mode))

    
# Checkbox

def check(master, text, variable, mode, on, off, command, px, py, checkboxname):
    checkboxname = customtkinter.CTkCheckBox(master, text=text, variable=variable, command=command, onvalue=on, offvalue=off)

    if mode == 'pack':
        checkboxname.pack(padx=px, pady=py)
    elif mode == 'grid':
        checkboxname.grid(row=px, column=py)
    else:
        print('Error: {} not supported'.format(mode))

    
# Slider

def slider(master, command, px, py, mode, slidername):
    slidername = customtkinter.CTkSlider(master, from_=0, to=100, command=command)
    if mode == 'pack':
        slidername.pack(padx=px, pady=py)
    elif mode == 'grid':
        slidername.grid(row=px, column=py)
    else:
        print('Error: {} not supported'.format(mode))


# Progressbar

def progress(master, px, py, mode, progressbarmode, speed, progressbarname):
    if progressbarmode == 'normal':
        progressbarname = customtkinter.CTkProgressBar(master, mode='determinate', determinate_speed=speed)
    elif progressbarmode == 'infinite':
        progressbarname = customtkinter.CTkProgressBar(master, mode='indeterminate', indeterminate_speed=speed)
    else:
        print('Not found')

    if mode == 'pack':
        progressbarname.pack(padx=px, pady=py)
    elif mode == 'grid':
        progressbarname.grid(row=px, column=py)
    else:
        print('Error: {} not supported'.format(mode))

# Dialog

def diag(text, title):
    customtkinter.CTkInputDialog(text=text, title=title)
    

# Only run when called directly

if __name__ == '__main__':
    time.sleep(0)
