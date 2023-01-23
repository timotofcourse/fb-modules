import tkinter
import customtkinter
import time

lines = 0.0
texthere = ''

# Only run when called directly

if __name__ == '__main__':

    # first part of an app, mainly properties

    def mainapp(title, size):
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

    def frame(master, lar, alt, cradius, px, py, sti, mode):
        f = customtkinter.CTkFrame(master, width=lar, height=alt, corner_radius=cradius)

        if mode == 'pack':
            f.pack(padx=px, pady=py, sticky=sti)
        elif mode == 'grid':
            f.grid(row=px, colimn=py, sticky=sti)
        else:
            print('Error: {} not supported'.format(mode))

    # Textbox

    def txtbox(master, px, py, mode, line, txt, state):
        a = customtkinter.CTkTextbox(master)
        a.insert(line, txt)
        a.config(state)

        if mode == 'pack':
            a.pack(padx=px, pady=py)
        elif mode == 'grid':
            a.grid(row=px, colimn=py)
        else:
            print('Error: {} not supported'.format(mode))

    # Scrollbar

    def scroll(master, mode, px, py, stick):
        tbox = tkinter.Text(master, highlightthickness=0)
        ctbox = customtkinter.CTkScrollbar(master, command=tbox.yview)
        tbox.configure(yscrollcommand=ctbox.set)

        if mode == 'pack':
            tbox.pack(padx=px, pady=py, sticky=stick)
            ctbox.pack(padx=px, pady=py + 1, sticky=stick)
        elif mode == 'grid':
            tbox.grid(row=px, column=py, sticky=stick)
            ctbox.pack(row=px, column=py + 1, sticky=stick)
        else:
            print('Error: {} not supported'.format(mode))

    # Button

    def button(master, text, command, px, py, mode, cradius, bradius):
        btn = customtkinter.CTkButton(master, text=text, command=command, border_width=bradius, corner_radius=cradius)

        if mode == 'pack':
            btn.pack(padx=px, pady=py)
        elif mode == 'grid':
            btn.grid(row=px, column=py)
        else:
            print('Error: {} not supported'.format(mode))

    
    # Checkbox

    def check(master, text, var, mode, on, off, command, px, py, nm):
        nm = customtkinter.CTkCheckBox(master, text=text, variable=var, command=command, onvalue=on, offvalue=off)

        if mode == 'pack':
            nm.pack(padx=px, pady=py)
        elif mode == 'grid':
            nm.grid(row=px, column=py)
        else:
            print('Error: {} not supported'.format(mode))

    
    