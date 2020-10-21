from re import findall
import tkinter as tk
from PIL import ImageTk, Image
import requests
import webbrowser
from io import BytesIO


def callback(url):
    webbrowser.open_new(url)


def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def onMousewheel(event, canvas):
    canvas.yview_scroll(-event.delta, "units")


def run(posts):
    root = tk.Tk()
    window_width = root.winfo_screenwidth()/2
    window_height = root.winfo_screenheight()

    root.title("RSS Reader")
    root.geometry("{0}x{1}+0+0".format(
        round(window_width), window_height))

    canvas = tk.Canvas(root)

    scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll_y.set)

    main_frame = tk.Frame(canvas)
    current_row = 0
    for post in posts:
        if 'img' in post:
            img_data = requests.get(post['img']).content
            render = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
            img = tk.Label(main_frame, image=render, width=window_width/4)
            img.image = render
            img.grid(column=0, row=current_row, padx=(0, 20))

        text_frame = tk.Frame(main_frame, width=(window_width/4)*3)
        tk.Label(text_frame, text=post['title'], font=(
            "Arial", 30), wraplength=window_width/1.5).pack()
        tk.Label(text_frame, text=post['date'],
                 wraplength=window_width/1.5).pack()
        tk.Label(text_frame, text=post['body'],
                 wraplength=window_width/1.5).pack()
        link = tk.Label(text_frame, text="Read More...", fg="blue",
                        cursor="pointinghand", wraplength=window_width/1.5)
        link.pack()
        link.bind("<Button-1>", lambda e: callback(post['link']))
        text_frame.grid(column=1, row=current_row)

        current_row += 1

    scroll_y.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window(4, 4, window=main_frame, anchor="nw")
    main_frame.bind("<Configure>", lambda e,
                    canvas=canvas: onFrameConfigure(canvas))
    canvas.bind_all("<MouseWheel>", lambda e,
                    canvas=canvas: onMousewheel(e, canvas))

    root.mainloop()

# https://www.buzzfeed.com/world.xml
# https://jacob.wrenn.me/feed.xml
# https://www.globalissues.org/news/feed
