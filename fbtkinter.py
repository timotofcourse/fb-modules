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
            f.grid(padx=px, pady=py, sticky=sti)
        elif mode == 'place':
            f.place(padx=px, pady=py, sticky=sti)
        else:
            print('Error: {} not supported'.format(mode))

    # Textbox

    def txtbox(master, px, py, mode, line, txt, state):
        a = customtkinter.CTkTextbox(master)
        a.insert(line, txt)
        a.config(state)

        if mode == 'pack':
            a.pack(row=px, colimn=py)
        elif mode == 'grid':
            a.grid(row=px, colimn=py)
        elif mode == 'place':
            a.place(row=px, colimn=py)
        else:
            print('Error: {} not supported'.format(mode))

    # 