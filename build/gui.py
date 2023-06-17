from tkinter import Tk, Canvas

def create_canvas():
    window = Tk()

    width = 1920
    height = 1080
    window.geometry(f'{width}x{height}')


    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1920.0,
        1080.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        17.0,
        20.0,
        1897.0,
        1060.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        147.0,
        197.0,
        497.0,
        386.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        614.0,
        42.0,
        1307.0,
        266.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1111.0,
        291.0,
        1217.0,
        411.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1424.0,
        197.0,
        1774.0,
        386.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        147.0,
        197.0,
        497.0,
        386.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        162.0,
        207.0,
        482.0,
        376.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1034.494873046875,
        69.31707763671875,
        1250.8660125732422,
        237.5902557373047,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        1040.4500732421875,
        74.3779296875,
        1244.2260284423828,
        232.4408416748047,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        614.0,
        42.0,
        1307.0,
        266.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        624.2061767578125,
        52.92681884765625,
        1296.7938232421875,
        255.0731658935547,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        946.7216796875,
        93.35610961914062,
        974.2783813476562,
        122.85855102539062,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        946.7216796875,
        180.77073669433594,
        974.2783813476562,
        210.27317810058594,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1111.0,
        291.0,
        1217.0,
        411.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        1117.0,
        297.0,
        1211.8300018310547,
        405.7200012207031,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1424.0,
        197.0,
        1774.0,
        386.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        1439.0,
        207.0,
        1759.0,
        376.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        670.134033203125,
        69.31707763671875,
        886.5051727294922,
        237.5902557373047,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        676.0891723632812,
        74.3779296875,
        879.8651275634766,
        232.4408416748047,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1029.0,
        69.0,
        1245.3711395263672,
        237.27317810058594,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        1034.955078125,
        74.06085205078125,
        1238.7310333251953,
        232.12376403808594,
        fill="#000000",
        outline="")

    canvas.create_text(
        907.9381103515625,
        117.85853576660156,
        anchor="nw",
        text="time",
        fill="#FFFFFF",
        font=("Tinos Regular", 48 * -1)
    )

    canvas.create_text(
        162.0,
        207.0,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("MerriweatherSansRoman Regular", 140 * -1)
    )

    canvas.create_text(
        1439.0,
        207.0,
        anchor="nw",
        text="0",
        fill="#FFFFFF",
        font=("MerriweatherSansRoman Regular", 140 * -1)
    )

    canvas.create_text(
        23.0,
        20.0,
        anchor="nw",
        text="HOME",
        fill="#DA0909",
        font=("Karla Bold", 135 * -1)
    )

    canvas.create_text(
        704.0,
        296.0,
        anchor="nw",
        text="PERIOD",
        fill="#FFFFFF",
        font=("Karla Bold", 80 * -1)
    )

    canvas.create_text(
        1117.0,
        297.0,
        anchor="nw",
        text="1",
        fill="#FFFFFF",
        font=("Karla Bold", 80 * -1)
    )

    canvas.create_text(
        1300.0,
        20.0,
        anchor="nw",
        text="VISITOR",
        fill="#DA0909",
        font=("Karla Bold", 135 * -1)
    )

    canvas.create_text(
        681.0,
        849.0,
        anchor="nw",
        text="penalties",
        fill="#FFFFFF",
        font=("Inter", 36 * -1)
    )

    canvas.create_rectangle(
        3.9998779296875,
        475.5032043457031,
        1897.0001220703125,
        488.5032043457031,
        fill="#FFFFFF",
        outline="")

    return canvas

if __name__ == "__main__":
    canvas = create_canvas()
    canvas.mainloop()
