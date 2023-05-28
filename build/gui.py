from tkinter import Tk, Canvas

def create_canvas():
    window = Tk()

    window.geometry("1366x768")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=768,
        width=1366,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        50.0,
        30.0,
        954.0,
        414.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        575.0,
        70.0,
        683.0,
        230.0,
        fill="#DA0909",
        outline="")

    canvas.create_text(
        595.0,
        118.0,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("Inter", 12 * -1),
        tags="away_score"
    )

    canvas.create_rectangle(
        140.0,
        70.0,
        248.0,
        230.0,
        fill="#DA0909",
        outline="")

    canvas.create_text(
        160.0,
        118.0,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("Inter", 12 * -1),
        tags="home_score"
    )

    canvas.create_text(
        382.0,
        105.0,
        anchor="nw",
        text="00:00",
        fill="#000000",
        font=("Inter", 12 * -1),
        tags="time"
    )

    canvas.create_text(
        323.0,
        284.0,
        anchor="nw",
        text="penalties",
        fill="#000000",
        font=("Inter", 12 * -1),
        tags="penalities"
    )

    window.resizable(False, False)

    return canvas
