import tkinter
import customtkinter
import time

# Only run when called directly

if __name__ == '__main__':

    # first part of an app, mainly properties

    def mainapp(title, size):
        root = customtkinter.CTk()
        root.geometry(size)
        root.title(title)
    
    