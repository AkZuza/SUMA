import gui, logger

def main():
    logger.init()
    sumaApp = gui.App()
    logger.log("App: SUMA opened")
    sumaApp.geometry("1280x720")
    sumaApp.wm_resizable(False, False)
    sumaApp.mainloop()
    logger.log('App: SUMA closed')
    logger.close()

if __name__ == "__main__":
    main()