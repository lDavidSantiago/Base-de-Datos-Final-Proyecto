import tkinter as tk
from tkinter import ttk
import psycopg2
import customtkinter
from postgres_folder.pythonpostgres import *
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
from datetime import datetime

class Pedidos(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1280}x{780}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Pedidos", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        def crear_ventana_entrada():
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("Entrada de datos")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            id_pedido_label = tk.Label(ventana_entrada, text="id_pedido")
            id_pedido_label.grid(row=0, column=0)
            id_pedido_entry = tk.Entry(ventana_entrada)
            id_pedido_entry.grid(row=0, column=1)

            dni_label = tk.Label(ventana_entrada, text="dni")
            dni_label.grid(row=1, column=0)
            dni_entry = tk.Entry(ventana_entrada)
            dni_entry.grid(row=1, column=1)

            articuloencargado_label = tk.Label(ventana_entrada, text="articuloencargado")
            articuloencargado_label.grid(row=2, column=0)
            articuloencargado_entry = tk.Entry(ventana_entrada)
            articuloencargado_entry.grid(row=2, column=1)

            medidaspersona_label = tk.Label(ventana_entrada, text="medidaspersona")
            medidaspersona_label.grid(row=3, column=0)
            medidaspersona_entry = tk.Entry(ventana_entrada)
            medidaspersona_entry.grid(row=3, column=1)

            fechaencargo_label = tk.Label(ventana_entrada, text="fechaencargo")
            fechaencargo_label.grid(row=4, column=0)
            fechaencargo_entry = tk.Entry(ventana_entrada)
            fechaencargo_entry.grid(row=4, column=1)

            fechaentrega_label = tk.Label(ventana_entrada, text="fechaentrega")
            fechaentrega_label.grid(row=5, column=0)
            fechaentrega_entry = tk.Entry(ventana_entrada)
            fechaentrega_entry.grid(row=5, column=1)

            abono_label = tk.Label(ventana_entrada, text="abono")
            abono_label.grid(row=6, column=0)
            abono_entry = tk.Entry(ventana_entrada)
            abono_entry.grid(row=6, column=1)

  
            estado_label = tk.Label(ventana_entrada, text="estado")
            estado_label.grid(row=8, column=0)
            estado_entry = tk.Entry(ventana_entrada)
            estado_entry.grid(row=8, column=1)

            enviar_button = tk.Button(ventana_entrada, text="Enviar", command=lambda: insertpedido(id_pedido_entry.get(), dni_entry.get(), articuloencargado_entry.get(), medidaspersona_entry.get(), fechaencargo_entry.get(), fechaentrega_entry.get(), abono_entry.get(), estado_entry.get()))
            enviar_button.grid(row=9, column=1)
        def crear_ventana_borrar():
            ventana_borrar = tk.Toplevel()
            ventana_borrar.title("Borrar datos")

            # Obtén las dimensiones de la pantalla
            anchura_pantalla = ventana_borrar.winfo_screenwidth()
            altura_pantalla = ventana_borrar.winfo_screenheight()

            # Calcula la posición x e y para centrar la ventana
            x = (anchura_pantalla / 2) - (ventana_borrar.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_borrar.winfo_reqheight() / 2)

            # Posiciona la ventana en el centro de la pantalla
            ventana_borrar.geometry("+%d+%d" % (x, y))
            id_entry = tk.Entry(ventana_borrar)
            id_entry.grid(row=0, column=1)
            tk.Label(ventana_borrar, text="ID").grid(row=0)
            boton_borrar = tk.Button(ventana_borrar, text="Borrar", command=lambda: deletepedido(id_entry.get()))            
            boton_borrar.grid(row=1, column=0, columnspan=2)

            self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_borrar, text="Borrar Pedido")
            self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        def crear_ventana_update():
            new_window = tk.Toplevel()
            new_window.title("Nueva Entrada")
            # Crear los widgets Label y Entry uno por uno\
            label0 = tk.Label(new_window, text="Id Pedido a Actualizar")
            entry0 = tk.Entry(new_window)
            label0.grid(row=1, column=0)
            entry0.grid(row=1, column=1)
            label1 = tk.Label(new_window, text="ID Pedido")
            entry1 = tk.Entry(new_window)
            label1.grid(row=2, column=0)
            entry1.grid(row=2, column=1)

            label2 = tk.Label(new_window, text="DNI")
            entry2 = tk.Entry(new_window)
            label2.grid(row=3, column=0)
            entry2.grid(row=3, column=1)
            label3 = tk.Label(new_window, text="Articulo Encargado")
            entry3 = tk.Entry(new_window)
            label3.grid(row=4, column=0)
            entry3.grid(row=4, column=1)

            label4 = tk.Label(new_window, text="Medidas Persona")
            entry4 = tk.Entry(new_window)
            label4.grid(row=5, column=0)
            entry4.grid(row=5, column=1)

            label5 = tk.Label(new_window, text="Fecha Encargo")
            entryencargo = tk.Entry(new_window)
            label5.grid(row=6, column=0)
            entryencargo.grid(row=6, column=1)
            
            label6 = tk.Label(new_window, text="Fecha Entrega")
            entryentrega = tk.Entry(new_window)
            label6.grid(row=7, column=0)
            entryentrega.grid(row=7, column=1)

            label7 = tk.Label(new_window, text="Abono")
            entry7 = tk.Entry(new_window)
            label7.grid(row=8, column=0)
            entry7.grid(row=8, column=1)


            label9 = tk.Label(new_window, text="Estado")
            entry9 = tk.Entry(new_window)
            label9.grid(row=10, column=0)
            entry9.grid(row=10, column=1)

            # Añadir un botón que diga "Actualizar"
            update_button = tk.Button(new_window, text="Actualizar", command=lambda: updatepedido(entry0.get(),entry1.get(), entry2.get(), entry3.get(), entry4.get(), entryencargo.get(), entryentrega.get(), entry7.get(),  entry9.get()))
            update_button.grid(row=11, column=1)  # Colocar el botón debajo de las entradas
        def agregarprod():
            
            ventana_entrada = tk.Toplevel()
            ventana_entrada.title("Entrada de datos")

            anchura_pantalla = ventana_entrada.winfo_screenwidth()
            altura_pantalla = ventana_entrada.winfo_screenheight()

            x = (anchura_pantalla / 2) - (ventana_entrada.winfo_reqwidth() / 2)
            y = (altura_pantalla / 2) - (ventana_entrada.winfo_reqheight() / 2)

            ventana_entrada.geometry("+%d+%d" % (x, y))

            tk.Label(ventana_entrada, text="ID Pedido", font=("Helvetica", 10)).grid(row=1, pady=(10, 0), padx=10, sticky="e")
            nombre_entry = tk.Entry(ventana_entrada)
            nombre_entry.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="w")

            tk.Label(ventana_entrada, text="ID Producto Terminado", font=("Helvetica", 10)).grid(row=2, pady=10, padx=10, sticky="e")
            apellido_entry = tk.Entry(ventana_entrada)
            apellido_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

            boton_anadir = ttk.Button(ventana_entrada, text="Añadir", command=lambda: agregarprodu(nombre_entry.get(), apellido_entry.get()))
            boton_anadir.grid(row=3, column=0, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")

            boton_ver_tabla = ttk.Button(ventana_entrada, text="Ver Tabla Relacion Productos con Pedido", command=lambda: mostrar_tabla_postgres("productos_encargados"))
            boton_ver_tabla.grid(row=3, column=2, columnspan=1, pady=(10,0), padx=10, sticky="nsew")

            boton_anadir3 = ttk.Button(ventana_entrada, text="Ver Tabla Productos Terminados", command=lambda: mostrar_tabla_postgres("productosterminados"))
            boton_anadir3.grid(row=3, column=1, columnspan=1, pady=(10, 0), padx=10, sticky="nsew")   
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_entrada, text="Insertar Pedido")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_borrar, text="Borrar Pedido")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=crear_ventana_update, text="Actualizar Pedido")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=agregarprod, text="Agregar Producto a Pedido")
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        new_label = customtkinter.CTkLabel(self.sidebar_frame, text="\n\nVista de Clientes,\n\nEn caso de dejar campo en blanco \nen actualizar cliente se mantendran \nlos valores anteriores ")
        new_label.grid(row=7, column=0, padx=20, pady=(10, 600))

        self.tree = ttk.Treeview(self, show="headings")
        self.tree.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese la lista a consultar")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(text="Consultar",master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=lambda: self.mostrar_tabla_event("pedido"))
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
    app = Pedidos()
    app.mainloop()