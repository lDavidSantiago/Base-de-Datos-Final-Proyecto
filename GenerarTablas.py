import tkinter as tk
from tkinter import ttk
import psycopg2
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class showinfo(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{800}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tienda de Ropa", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Crear una instancia de CTkLabel con sidebar_frame como el padre
        new_label = customtkinter.CTkLabel(self.sidebar_frame, text="\n\nTablas a Consultar:\n\n-Cliente\n\n-Colegio\n\nFactura\n\n-MateriaPrima\n\n-Pedido\n\n-Proveedor\n\n-Uniforme")
        # Llamar al método grid en la instancia de CTkLabel para colocarla en sidebar_frame
        new_label.grid(row=6, column=0, padx=20, pady=(10, 600))
       
        
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese la lista a consultar")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(text="Consultar",master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=lambda: self.mostrar_tabla_event(self.entry.get()))
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
    app = showinfo()
    app.mainloop()
