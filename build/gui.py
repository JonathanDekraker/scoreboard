from tkinter import Tk, Canvas

def create_canvas():
    window = Tk()

    width = 1920
    height = 1080
    window.geometry(f'{width}x{height}')

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=height,
        width=width,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0, 0, width, height,
        fill="#FFFFFF",
        outline=""
    )

    canvas.create_rectangle(
        17, 20, 1897, 1060,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        147, 197, 497, 386,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        614, 42, 1307, 266,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        1111, 291, 1217, 411,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        1424, 197, 1774, 386,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        670, 69, 886, 237,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        1034, 69, 1250, 237,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        147, 197, 497, 386,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        162, 207, 482, 376,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        614, 42, 1307, 266,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        624, 52, 1296, 255,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        946, 93, 974, 122,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        946, 180, 974, 210,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        1111, 291, 1217, 411,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        1117, 297, 1211, 405,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        1424, 197, 1774, 386,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        1439, 207, 1759, 376,
        fill="#000000",
        outline=""
    )

    canvas.create_text(
        907, 117,
        anchor="nw",
        text="time",
        fill="#FFFFFF",
        font=("Tinos Regular", 48),
        tags="time"
    )

    canvas.create_text(
        162, 207,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("MerriweatherSansRoman Regular", 140),
        tags="home_score"
    )

    canvas.create_text(
        1439, 207,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("MerriweatherSansRoman Regular", 140),
        tags="away_score"
    )

    canvas.create_text(
        23, 20,
        anchor="nw",
        text="HOME",
        fill="#DA0909",
        font=("Karla Bold", 135)
    )

    canvas.create_text(
        704, 296,
        anchor="nw",
        text="PERIOD",
        fill="#FFFFFF",
        font=("Karla Bold", 80)
    )

    canvas.create_text(
        1117, 297,
        anchor="nw",
        text="1",
        fill="#FFFFFF",
        font=("Karla Bold", 80)
    )

    canvas.create_text(
        1300, 20,
        anchor="nw",
        text="VISITOR",
        fill="#DA0909",
        font=("Karla Bold", 135)
    )

    canvas.create_text(
        681, 849,
        anchor="nw",
        text="penalties",
        fill="#FFFFFF",
        font=("Inter", 36),
        tags="penalties"
    )

    canvas.create_rectangle(
        4, 475.5, 1897, 488.5,
        fill="#FFFFFF",
        outline=""
    )

    return canvas

if __name__ == "__main__":
    canvas = create_canvas()
    canvas.mainloop()
