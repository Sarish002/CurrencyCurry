from customtkinter import *
import currency

set_appearance_mode("system")
set_default_color_theme("blue")

root = CTk()
root.geometry("500x500")
root.title("Curry Of Currencies")
root.configure(fg_color="#5790AB")

Frame = CTkFrame(root,
                border_color="white",
                border_width=5,
                corner_radius=5,
                width=450, height=450,
                fg_color="#9ccddb")

ComboBox_init = CTkComboBox(
    root, width = 200,
    font=("Trebuchet MS", 15),
    values=currency.countries,
    bg_color="#9ccddb",
    dropdown_fg_color="#064469",
    dropdown_font=("Trebuchet MS", 15),
    dropdown_hover_color="#579dab",
    fg_color="#5790ab"
)

ComboBox_output = CTkComboBox(
    root, width=200,
    font=("Trebuchet MS", 15),
    values=currency.countries,
    bg_color="#9ccddb",
    dropdown_fg_color="#064469",
    dropdown_font=("Trebuchet MS", 15),
    dropdown_hover_color="#579dab",
    fg_color="#5790ab"
)

ComboBox_init.place(relx = 0.5, rely = 0.3, anchor = "center")
ComboBox_output.place(relx = 0.5, rely = 0.4, anchor = "center")

Entry = CTkEntry(
    root, width = 200,
    font=("Trebuchet MS", 15),
    bg_color="#9ccddb",
    fg_color="#5790ab"
)
Entry.place(relx = 0.5, rely = 0.5, anchor = "center")

Label = CTkLabel(
    root, width = 200,
    height=40,
    font=("Trebuchet MS", 14, "bold"),
    text="", fg_color="#5790AB",
    bg_color="#9ccddb",
    corner_radius=6,
    text_color="#072d44", wraplength=200)
Label.place(relx = 0.5, rely = 0.615, anchor = "center")

def give_output(placeholder) -> None:
    output = currency.currency_conversion(ComboBox_init.get(),
                                          ComboBox_output.get(),
                                          Entry.get()
                                          )
    Label.configure(text=output)
Entry.bind("<Return>", give_output)

Frame.place(relx = 0.5, rely = 0.5, anchor = "center")

if __name__ == "__main__":
    root.mainloop()
