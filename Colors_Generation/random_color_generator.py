import random
import tkinter as tk

def project():
    def random_colors():
        list_of_tuples = []
        for _ in range(4):
            single_tuple = tuple(random.randint(0, 256) for _ in range(3))
            list_of_tuples.append(single_tuple)
        print(list_of_tuples)
        return list_of_tuples

    def create_color_label(rgb):
        label = tk.Label(root, bg=rgb_to_hex(rgb), width=50, height=10, relief="solid", borderwidth=1)
        label.pack()

    def rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

    root = tk.Tk()
    root.title("RGB Color Display")

    for color in random_colors():
        create_color_label(color)

    root.minsize(400, 300)
    root.maxsize(1280, 1024)
    root.mainloop()


