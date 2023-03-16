import tkinter 
import customtkinter 

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")
app.title("File")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

scrollable_frame = customtkinter.CTkScrollableFrame(master=app, width=200, height=200)
scrollable_frame.place(x=10, rely=10)
text_var = tkinter.StringVar(value="CTkLabel")

label = customtkinter.CTkLabel(master=scrollable_frame,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()