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
from postgres_folder.pythonpostgres import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Informes(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        def crear_ventana_entrada():
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("BUSCAR PEDIDOS POR CLIENTE")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            tk.Label(ventana_entrada, text="DNI Cliente: ", font=("Helvetica", 10)).grid(row=1, pady=(10, 0), padx=10, sticky="e")
            nombre_entry = tk.Entry(ventana_entrada)
            nombre_entry.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="w")
            boton_anadir = ttk.Button(ventana_entrada, text="Añadir", command=lambda: mostrarPedidosEnEsperaPorDNI(nombre_entry.get()))
            boton_anadir.grid(row=3, column=1, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")
        def colegio():
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("CARACTERISTICA UNIFORME ")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            tk.Label(ventana_entrada, text="ID Colegio: ", font=("Helvetica", 10)).grid(row=1, pady=(10, 0), padx=10, sticky="e")
            nombre_entry = tk.Entry(ventana_entrada)
            nombre_entry.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="w")
            boton_anadir = ttk.Button(ventana_entrada, text="Añadir", command=lambda: caracteristicasUniformes(nombre_entry.get()))
            boton_anadir.grid(row=3, column=1, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=14, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(14, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="INFORMES", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:mostrarPedidosEnEspera(), text="➢ Listado de Productos encargados pendientes por entregar \n(ordenados por fecha)")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_entrada,text="➢ Por cada cliente, listar los productos encargados \nque no han sido entregados")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:existenciaEncargados(),text="➢ Por cada producto, cantidad en existencia descontando \nlos que están encargados")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:seFabricanUniformes(),text="➢ Listado de colegios de los que se fabrican uniformes.")
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=colegio,text="➢ Dado un colegio las características de su uniforme.")
        self.sidebar_button_6.grid(row=7, column=0, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: mostrar_tabla_postgres("factura_venta"),text="➢Tabla de Ventas")
        self.sidebar_button_7.grid(row=8, column=0, padx=20, pady=10)
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: total_ventas(),text="➢ Calcular el total de ventas.")
        self.sidebar_button_8.grid(row=9, column=0, padx=20, pady=10)
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: total_ventas_school(),text="➢ Calcular el total de ventas de solo colegios.")
        self.sidebar_button_8.grid(row=10, column=0, padx=20, pady=10)




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

if __name__ == "__main__":
    app = Informes()
    app.mainloop()