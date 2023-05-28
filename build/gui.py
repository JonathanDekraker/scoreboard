from tkinter import Tk, Canvas

def create_canvas():
    window = Tk()


    # getting screen's height and width
    height = window.winfo_screenheight()
    width = window.winfo_screenwidth()
    window.geometry(f'{width}x{height}')
    # Calculate the scale factor based on the screen width and height
    scale_x = width / 1366
    scale_y = height / 768

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
        50.0 * scale_x,
        30.0 * scale_y,
        954.0 * scale_x,
        414.0 * scale_y,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        575.0 * scale_x,
        70.0 * scale_y,
        683.0 * scale_x,
        230.0 * scale_y,
        fill="#DA0909",
        outline=""
    )

    canvas.create_text(
        595.0 * scale_x,
        118.0 * scale_y,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("Inter", int(12 * scale_x)),
        tags="away_score"
    )

    canvas.create_rectangle(
        140.0 * scale_x,
        70.0 * scale_y,
        248.0 * scale_x,
        230.0 * scale_y,
        fill="#DA0909",
        outline=""
    )

    canvas.create_text(
        160.0 * scale_x,
        118.0 * scale_y,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("Inter", int(12 * scale_x)),
        tags="home_score"
    )

    canvas.create_text(
        382.0 * scale_x,
        105.0 * scale_y,
        anchor="nw",
        text="00:00",
        fill="#000000",
        font=("Inter", int(12 * scale_x)),
        tags="time"
    )

    canvas.create_text(
        323.0 * scale_x,
        284.0 * scale_y,
        anchor="nw",
        text="penalties",
        fill="#000000",
        font=("Inter", int(12 * scale_x)),
        tags="penalties"
    )

    return canvas
