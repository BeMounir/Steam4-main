import tkinter as tk
from PIL import Image, ImageTk
from icecream import ic
from time import sleep
import requests as rq
import json


def dev_funcs():
    test_tiles()
    # root.after(0, SmallTile.update_tile, 5, 'Game', 'Games!')
    first_game()


def first_game():
    game = ic(get_game(None, 1))
    SmallTile.instances['Tile1'].__dict__['body_frame'].__dict__['children']['!label'].config(
        font=('Arial', 30, 'bold'))
    Window.temp_frame1.update_tile('First Game', game['name'])


def test_tiles():
    for index, tile in enumerate(SmallTile.instances.values(), start=1):
        tile.update_tile(new_header=f'new_header{index}', new_body=f'new_body{index}' * 100)


def get_game(name, index):
    with open('steam.json', 'r') as steam:
        steam_data = json.load(steam)
    if name:
        ic('name')
        for game in steam_data:
            if game['name'] == name:
                return game
    elif index:
        ic('index')
        return steam_data[index - 1]


class DashBoard:
    instances = []

    def __init__(self):
        self.temp_frame1 = None
        self.temp_frame2 = None
        self.temp_frame3 = None
        self.temp_frame4 = None
        self.temp_frame5 = None
        self.instances.append(self)
        w_width, w_height = 1600, 900
        self.root = tk.Tk()
        self.root.title("Dashboard Steam")
        self.root.geometry(f"{w_width}x{w_height}")
        self.root.config(bg="white")
        self.root.columnconfigure(0, weight=33, uniform='root_column')
        self.root.columnconfigure(1, weight=33, uniform='root_column')
        self.root.columnconfigure(2, weight=33, uniform='root_column')
        self.root.rowconfigure(0, weight=50, uniform='root_row')
        self.root.rowconfigure(1, weight=50, uniform='root_row')
        self.root.grid_propagate(False)

        self.draw_bg(w_width, w_height)
        self.call_tiles()

    def draw_bg(self, w_width, w_height):
        global img
        img = ImageTk.PhotoImage(Image.open("Assets/SteamBG.png").resize((w_width, w_height)))
        bg = tk.Canvas(self.root, bg='black', height=w_height, width=w_width, highlightthickness=0)
        bg.create_image(0, 0, anchor='nw', image=img)
        bg.place(relx=0.5, rely=0.5, anchor='center')

    def call_tiles(self):
        self.temp_frame1 = SmallTile(frame_root=self.root, frame_color='#FFD166',
                                     frame_column=0, frame_row=0, header="Tile1",
                                     body=f"{'test1 ' * 500}")
        self.temp_frame2 = SmallTile(frame_root=self.root, frame_color='#06D6A0',
                                     frame_column=1, frame_row=0, header="Tile2",
                                     body=f"{'test2 ' * 500}")
        self.temp_frame3 = SmallTile(frame_root=self.root, frame_color='#EE6C4D',
                                     frame_column=2, frame_row=0, header="Tile3",
                                     body=f"{'test3 ' * 500}")
        self.temp_frame4 = SmallTile(frame_root=self.root, frame_color='#0063FF',
                                     frame_column=0, frame_row=1, header="Tile4",
                                     body=f"{'test4 ' * 500}")
        self.temp_frame5 = SmallTile(frame_root=self.root, frame_color='#C700FF',
                                     frame_column=1, frame_row=1, header="Tile5",
                                     body=f"{'test5 ' * 500}")


class SmallTile:
    instances = {}

    def __init__(self, frame_root, frame_color, frame_column, frame_row, header, body):
        self.instances[header] = self
        self.frame = tk.Frame(frame_root)
        self.frame.columnconfigure(0, weight=100, uniform='frame_column')
        self.frame.rowconfigure(0, weight=15, uniform='frame_row')
        self.frame.rowconfigure(1, weight=85, uniform='frame_row')
        self.frame.grid_propagate(False)

        self.header_var = tk.StringVar(self.frame)
        self.body_var = tk.StringVar(self.frame)
        self.test_var = tk.StringVar(self.frame)
        self.header_var.set(header)
        self.body_var.set(body)
        self.header_frame = tk.Frame(self.frame, bg=self.header_color(frame_color))

        self.body_frame = tk.Frame(self.frame, bg=frame_color)
        self.body_frame.columnconfigure(0, weight=50, uniform='body_column')
        self.body_frame.columnconfigure(1, weight=50, uniform='body_column')
        self.body_frame.rowconfigure(0, weight=50, uniform='body_row')
        self.body_frame.rowconfigure(1, weight=50, uniform='body_row')

        self.render_frames(frame_column, frame_row, frame_color)

    def render_frames(self, frame_column, frame_row, frame_color):
        self.frame.grid(column=frame_column, row=frame_row, sticky='news', padx=20, pady=20)
        self.header_frame.grid(column=0, row=0, sticky='news')
        self.body_frame.grid(column=0, row=1, sticky='news')
        header_label = tk.Label(self.header_frame, textvariable=self.header_var, fg='#FFFFFF',
                                bg=self.header_color(frame_color),
                                font=('Arial', 20, 'bold'))
        body_label = tk.Label(self.body_frame, textvariable=self.body_var, fg='#FFFFFF', bg=frame_color,
                              font=('Arial', 16, 'bold'), wraplength=450, justify='left')
        header_label.place(relx=0.05, rely=0.5, anchor='w')
        body_label.grid(columnspan=2, row=1, sticky='news')

    def update_tile(self, new_header, new_body):
        self.header_var.set(new_header)
        self.body_var.set(new_body)
        ic(self.frame.__dict__['children']['!frame2'].__dict__['children']['!label'].cget("text"))

    @staticmethod
    def header_color(fc):
        hex_pairs = [f"{fc[1]}{fc[2]}", f"{fc[3]}{fc[4]}", f"{fc[5]}{fc[6]}"]
        body = [int(pair, 16) for pair in hex_pairs]
        for index, value in enumerate(body):
            if value - 40 > 0:
                body[index] -= 40
            else:
                body[index] = 0
        body = "".join([f"{rgb:0{2}x}" for rgb in body])
        return f"#{body}"


if __name__ == '__main__':
    Window = DashBoard()
    root = Window.root
    root.after(0, dev_funcs)
    root.mainloop()
