import tkinter as tk
from tkinter import ttk
import psycopg2
import customtkinter
from postgres_folder.pythonpostgres import *
from prettytable import PrettyTable
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class ProductosMateria(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{800}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tienda de Ropa", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        def crear_ventana_entrada():
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("Entrada de datos")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            tk.Label(ventana_entrada, text="ID Producto:", font=("Helvetica", 10)).grid(row=1, pady=(10, 0), padx=10, sticky="e")
            nombre_entry = tk.Entry(ventana_entrada)
            nombre_entry.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="w")

            tk.Label(ventana_entrada, text="ID Materia Prima:", font=("Helvetica", 10)).grid(row=2, pady=10, padx=10, sticky="e")
            apellido_entry = tk.Entry(ventana_entrada)
            apellido_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

            # Botones con estilo ttk
            style = ttk.Style()
            style.configure("TButton", font=("Helvetica", 10))

            boton_anadir = ttk.Button(ventana_entrada, text="Añadir", command=lambda: insertProdMat(nombre_entry.get(), apellido_entry.get()))
            boton_anadir.grid(row=3, column=0, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")

            boton_ver_tabla = ttk.Button(ventana_entrada, text="Ver Tabla Productos", command=lambda: mostrar_tabla_postgres("productosterminados"))
            boton_ver_tabla.grid(row=3, column=2, columnspan=1, pady=(10,0), padx=10, sticky="nsew")

            boton_anadir3 = ttk.Button(ventana_entrada, text="Ver Tabla Materia Prima", command=lambda: mostrar_tabla_postgres("materiaprima"))
            boton_anadir3.grid(row=3, column=1, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")    
        def crear_ventana_borrar():
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("Borrar Registros")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            tk.Label(ventana_entrada, text="ID Producto:", font=("Helvetica", 10)).grid(row=1, pady=(10, 0), padx=10, sticky="e")
            nombre_entry = tk.Entry(ventana_entrada)
            nombre_entry.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="w")

            tk.Label(ventana_entrada, text="ID Materia Prima:", font=("Helvetica", 10)).grid(row=2, pady=10, padx=10, sticky="e")
            apellido_entry = tk.Entry(ventana_entrada)
            apellido_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

            # Botones con estilo ttk
            style = ttk.Style()
            style.configure("TButton", font=("Helvetica", 10))

            boton_anadir = ttk.Button(ventana_entrada, text="Borrar", command=lambda: deleteProdMat(nombre_entry.get(), apellido_entry.get()))
            boton_anadir.grid(row=3, column=0, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")

            boton_ver_tabla = ttk.Button(ventana_entrada, text="Ver Tabla Productos", command=lambda: mostrar_tabla_postgres("productosterminados"))
            boton_ver_tabla.grid(row=3, column=2, columnspan=1, pady=(10,0), padx=10, sticky="nsew")

            boton_anadir3 = ttk.Button(ventana_entrada, text="Ver Tabla Materia Prima", command=lambda: mostrar_tabla_postgres("materiaprima"))
            boton_anadir3.grid(row=3, column=1, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")
        def crear_ventana_update():
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("Borrar Registros")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            tk.Label(ventana_entrada, text="ID Producto :", font=("Helvetica", 10)).grid(row=1, pady=(10, 0), padx=10, sticky="e")
            nombre_entry = tk.Entry(ventana_entrada)
            nombre_entry.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="w")

            tk.Label(ventana_entrada, text="ID Materia Prima: ", font=("Helvetica", 10)).grid(row=2, pady=10, padx=10, sticky="e")
            apellido_entry = tk.Entry(ventana_entrada)
            apellido_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

            tk.Label(ventana_entrada, text="ID Producto Nuevo: ", font=("Helvetica", 10)).grid(row=3, pady=(10, 0), padx=10, sticky="e")
            nombre_entry1 = tk.Entry(ventana_entrada)
            nombre_entry1.grid(row=3, column=1, pady=(10, 0), padx=10, sticky="w")

            tk.Label(ventana_entrada, text="ID Materia Prima Nueva: ", font=("Helvetica", 10)).grid(row=4, pady=10, padx=10, sticky="e")
            apellido_entry1 = tk.Entry(ventana_entrada)
            apellido_entry1.grid(row=4, column=1, pady=10, padx=10, sticky="w")

            # Botones con estilo ttk
            style = ttk.Style()
            style.configure("TButton", font=("Helvetica", 10))

            boton_anadir = ttk.Button(ventana_entrada, text="Actualizar", command=lambda: updateProdMat(nombre_entry.get(), apellido_entry.get(),nombre_entry1.get(),apellido_entry1.get()))
            boton_anadir.grid(row=5, column=0, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")

            boton_ver_tabla = ttk.Button(ventana_entrada, text="Ver Tabla Productos", command=lambda: mostrar_tabla_postgres("productosterminados"))
            boton_ver_tabla.grid(row=5, column=2, columnspan=1, pady=(10,0), padx=10, sticky="nsew")

            boton_anadir3 = ttk.Button(ventana_entrada, text="Ver Tabla Materia Prima", command=lambda: mostrar_tabla_postgres("materiaprima"))
            boton_anadir3.grid(row=5, column=1, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_entrada, text="Insertar Relacion Producto a Materia Prima")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_borrar, text="Borrar Registro")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_update, text="Actualizar Registros")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        new_label = customtkinter.CTkLabel(self.sidebar_frame, text="\n\nVista de Clientes,\n\nEn caso de dejar campo en blanco \nen actualizar cliente se mantendran \nlos valores anteriores ")
        new_label.grid(row=6, column=0, padx=20, pady=(10, 600))

        self.tree = ttk.Treeview(self, show="headings")
        self.tree.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese la lista a consultar")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(text="Consultar",master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=lambda: self.mostrar_tabla_event("productomateria"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
    def mostrar_tabla_event(self,nombre_tabla):
        dbname = 'proyectofinaltest'
        user ='postgres'
        password = 'Mifamilifeliz7'
        host = 'localhost'
        port = 5432

        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        # Nombre de la tabla que deseas mostrar
        query = f"SELECT * FROM {nombre_tabla}"  
        cur.execute(query)

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cur.description]

        # Limpiar datos previos en el Treeview y actualizar los headings
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = column_names
        for col in column_names:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  

        # Ejecutar la consulta completa y agregar datos al Treeview
        query = f"SELECT * FROM {nombre_tabla};"
        cur.execute(query)
        for row in cur.fetchall():
            self.tree.insert("", "end", values=row)

        cur.close()
        conn.close()
    

        
if __name__ == "__main__":
    app = ProductosMateria()
    app.mainloop()