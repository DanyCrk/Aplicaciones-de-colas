import tkinter as tk

from interfaz.vista_principal import vistaPrincipal


def main():

    root = tk.Tk()

    vistaPrincipal(root)

    root.mainloop()


if __name__ == "__main__":
    main()