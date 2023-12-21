import sys
sys.path.append('..') 
import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from postgres_folder.pythonpostgres import *
from mainGUI import App
from GUI_employee import Appa

# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 

app = ctk.CTk() 
app.geometry("400x400") 
app.title("Tienda Ropa A") 
gui = App()
guiem = Appa()
def login():
    entered_username = user_entry.get()
    entered_password = user_pass.get()

    usuario = verificar_credenciales(entered_username, entered_password)

    if usuario:
        tkmb.showinfo(title="Login Successful", message=f"Welcome, {usuario[1]} ({usuario[3]})!")
        # Realizar acciones según el rol (administrador o vendedor)
        if usuario[3] == 'admin':
            app.iconify
            gui.mainloop()
            print("Acciones de administrador")
        elif usuario[3] == 'vendedor':
            app.iconify
            guiem.mainloop()
    else:
        tkmb.showwarning(title='Invalid Credentials', message='Invalid username or password')



label = ctk.CTkLabel(app,text="Please Log In") 

label.pack(pady=20) 


frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label = ctk.CTkLabel(master=frame,text='Log In') 
label.pack(pady=12,padx=10) 


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 


button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 



app.mainloop()
