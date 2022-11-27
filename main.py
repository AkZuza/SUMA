import gui

def main():
    sumaApp = gui.App()
    sumaApp.geometry("1280x700")
    sumaApp.wm_resizable(False, False)
    sumaApp.mainloop()

if __name__ == "__main__":
    main()