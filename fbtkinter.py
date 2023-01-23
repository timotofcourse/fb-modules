import tkinter
import customtkinter
import time

lines = 0.0
texthere = ''

# Only run when called directly

if __name__ == '__main__':

    # First part of an app

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

    def frame(master, lar, alt, cradius, px, py, sti, mode, var):
        var = customtkinter.CTkFrame(master, width=lar, height=alt, corner_radius=cradius)

        if mode == 'pack':
            var.pack(padx=px, pady=py, sticky=sti)
        elif mode == 'grid':
            var.grid(row=px, colimn=py, sticky=sti)
        else:
            print('Error: {} not supported'.format(mode))

    # Textbox

    def txtbox(master, px, py, mode, line, txt, state, var):
        var = customtkinter.CTkTextbox(master)
        var.insert(line, txt)
        var.config(state)

        if mode == 'pack':
            var.pack(padx=px, pady=py)
        elif mode == 'grid':
            var.grid(row=px, colimn=py)
        else:
            print('Error: {} not supported'.format(mode))

    # Scrollbar

    def scroll(master, mode, px, py, stick, var1, var2):
        var1 = tkinter.Text(master, highlightthickness=0)
        var2 = customtkinter.CTkScrollbar(master, command=var1.yview)
        var1.configure(yscrollcommand=var2.set)

        if mode == 'pack':
            var1.pack(padx=px, pady=py, sticky=stick)
            var2.pack(padx=px, pady=py + 1, sticky=stick)
        elif mode == 'grid':
            var1.grid(row=px, column=py, sticky=stick)
            var2.pack(row=px, column=py + 1, sticky=stick)
        else:
            print('Error: {} not supported'.format(mode))

    # Button

    def button(master, text, command, px, py, mode, cradius, bradius, var):
        var = customtkinter.CTkButton(master, text=text, command=command, border_width=bradius, corner_radius=cradius)

        if mode == 'pack':
            var.pack(padx=px, pady=py)
        elif mode == 'grid':
            var.grid(row=px, column=py)
        else:
            print('Error: {} not supported'.format(mode))

    
    # Checkbox

    def check(master, text, var1, mode, on, off, command, px, py, var2):
        var2 = customtkinter.CTkCheckBox(master, text=text, variable=var1, command=command, onvalue=on, offvalue=off)

        if mode == 'pack':
            var2.pack(padx=px, pady=py)
        elif mode == 'grid':
            var2.grid(row=px, column=py)
        else:
            print('Error: {} not supported'.format(mode))

    
    # Slider

    def slider(master, command, px, py, mode, var):
        var = customtkinter.CTkSlider(master, from_=0, to=100, command=command)
        if mode == 'pack':
            var.pack(padx=px, pady=py)
        elif mode == 'grid':
            var.grid(row=px, column=py)
        else:
            print('Error: {} not supported'.format(mode))


    # Progressbar

    def progress(master, px, py, mode, pmode, speed, var):
        if pmode == 'normal':
            var = customtkinter.CTkProgressBar(master, mode='determinate', determinate_speed=speed)
        elif pmode == 'inv':
            var = customtkinter.CTkProgressBar(master, mode='indeterminate', indeterminate_speed=speed)
        else:
            print('Not found')

        if mode == 'pack':
            var.pack(padx=px, pady=py)
        elif mode == 'grid':
            var.grid(row=px, column=py)
        else:
            print('Error: {} not supported'.format(mode))

    # Dialog

    def diag(text, title, var):
        var = customtkinter.CTkInputDialog(text=text, title=title)
    
