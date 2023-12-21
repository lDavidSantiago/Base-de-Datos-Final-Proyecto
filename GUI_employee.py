import tkinter
import tkinter.messagebox
import customtkinter
from GenerarTablas import showinfo
from Clientes import Clientes
from Pedidos import Pedidos
from Proveedor import Proveedor
from ProductoTerminado import ProductoTerminado
from Colegio import Colegio
from Uniformes import Uniformes
from Materia import Materia
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Appa(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=14, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(14, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tienda de Ropa", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.clientescall,text="Clientes")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.callpedidos,text="Pedidos")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=self.callprod,text="Productos Terminados")
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "BUENOS DIAS \n\n" + "QUE DESEA HACER EL DIA DE HOY\n\n" + """
""")
        self.textbox.configure(state = "disabled")
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        guit = showinfo()
        self.iconify()
        guit.mainloop()
    def clientescall(self):
        cliente = Clientes()
        self.iconify()
        cliente.mainloop()
    def callpedidos(self):
        pedido = Pedidos()
        self.iconify()
        pedido.mainloop()
    def callprod(self):
        producto = ProductoTerminado()
        self.iconify()
        producto.mainloop()
    def callprov(self):
        proveedor = Proveedor()
        self.iconify()
        proveedor.mainloop()
    def callSchool(self):
        school = Colegio()
        self.iconify()
        school.mainloop()
    def callUniforms(self):
        uniform = Uniformes()
        self.iconify()
        uniform.mainloop()
    def callmateria(self):
        materia = Materia()
        self.iconify()
        materia.mainloop()
if __name__ == "__main__":
    app = Appa()
    app.mainloop()