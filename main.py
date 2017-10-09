from tkinter import Tk
from gui import MainFrame


def main():
    root = Tk()
    w = 450
    h = 200
    ws = root.winfo_screenmmwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.minsize(w, h)
    app = MainFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()