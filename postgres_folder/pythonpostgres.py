import psycopg2
import psycopg2.extras
from datetime import datetime
from prettytable import PrettyTable
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

hostname = 'localhost'
database = 'proyectofinaltest'
username = 'postgres'
pwd = 'Mifamilifeliz7'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = 'Mifamilifeliz7',
            port = port_id)
    
    cur = conn.cursor()
    def mostrar_tabla_postgres(tabla):
    # Ejecutar una consulta para obtener datos de la tabla
        query = f"SELECT * FROM {tabla};"
        cur.execute(query)

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cur.description]
        # Crear una nueva ventana emergente
        ventana_emergente = tk.Toplevel()
        ventana_emergente.title(f"Tabla: {tabla}")
        # Crear un Treeview en la ventana emergente
        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names
        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)  

        # Ejecutar la consulta completa y agregar datos al Treeview
        query = f"SELECT * FROM {tabla};"
        cur.execute(query)
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
    def realizar_consulta_pedido():
        try:
            cur.execute('SELECT * FROM PEDIDO')
            print(cur.fetchall())
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def insertcliente(dni, nombre,apellido, telefono):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO cliente(dni,nombre,apellido,telefono)VALUES(%s,%s,%s,%s)'
            insert_value = (dni, nombre,apellido, telefono)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def deletecliente(dni):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM cliente WHERE dni = %s'
            delete_value = (dni,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def updateclient(dni1, newdn1, newname, newlastn, tel):
        try:
            cur = conn.cursor()
            update_script = '''
            UPDATE cliente 
            SET dni = COALESCE(NULLIF(%s, ''), dni),
                nombre = COALESCE(NULLIF(%s, ''), nombre),
                apellido = COALESCE(NULLIF(%s, ''), apellido),
                telefono = COALESCE(NULLIF(%s, ''), telefono)
            WHERE dni = %s
            '''
            cur.execute(update_script, (newdn1, newname, newlastn, tel, dni1))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def insertpedido(id, dni, articulo, medidas, fechaencargo, fechaentrega, abono, estado):
        try:
            # Crear un cursor
            cur = conn.cursor()
  
            query = """
            INSERT INTO pedido (id_pedido, dni, articuloencargado, medidaspersona, fechaencargo, fechaentrega, abono, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (id, dni, articulo, medidas, fechaencargo, fechaentrega, abono,estado))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def deletepedido(dni):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM pedido WHERE id_pedido = %s'
            delete_value = (dni,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def updatepedido(id_pedidoevaluar, newidpedido, new_dni, new_articuloencargado, new_medidaspersona, new_fechaencargo, new_fechaentrega, new_abono, new_estado):

        try:
            new_fechaencargo1 = datetime.strptime(new_fechaencargo, '%Y-%m-%d').date() if new_fechaencargo else None
            new_fechaentrega1 = datetime.strptime(new_fechaentrega, '%Y-%m-%d').date() if new_fechaentrega else None
            new_abono = int(new_abono) if new_abono else None

            cur = conn.cursor()
            update_script = '''
            UPDATE pedido
            SET id_pedido = COALESCE(%s, id_pedido),
                dni = COALESCE(%s, dni),
                articuloencargado = COALESCE(%s, articuloencargado),
                medidaspersona = COALESCE(%s, medidaspersona),
                fechaencargo = COALESCE(%s, fechaencargo),
                fechaentrega = COALESCE(%s, fechaentrega),
                abono = COALESCE(%s, abono),
                estado = COALESCE(%s, estado)
            WHERE
                id_pedido = %s;
            '''
            cur.execute(update_script, (newidpedido, new_dni, new_articuloencargado, new_medidaspersona, new_fechaencargo1,
                                        new_fechaentrega1, new_abono, new_estado, id_pedidoevaluar))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def insertproduct(id_productoterminado, id_uniforme, sexo,precioventa, descripcion, talla,cantidadexistencia):
        try:
            # Crear un cursor
            cur = conn.cursor()

            if not id_uniforme or not id_uniforme.strip():
                id_uniforme = None
  
            query = """
            INSERT INTO productosterminados (id_productoterminado, id_uniforme, sexo,precio_venta, descripcion, talla,cantidad_existencia)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (id_productoterminado, id_uniforme, sexo,precioventa, descripcion, talla,cantidadexistencia))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def deleteproduct(id_productoterminado):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM productosterminados WHERE id_productoterminado = %s'
            delete_value = (id_productoterminado,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def update_producto(id_buscar,id_productoterminado, id_uniforme, sexo,precio_venta, descripcion, talla,cantidad_existencia):
        try:
            precio_venta = int(precio_venta) if precio_venta else None
            cantidad_existencia = int(cantidad_existencia) if cantidad_existencia else None
            cur = conn.cursor()
            if not id_uniforme or not id_uniforme.strip():
                id_uniforme = None
            update_script = '''
                UPDATE productosterminados
                SET
                    id_productoterminado = COALESCE(%s, id_productoterminado),
                    id_uniforme = COALESCE(%s, id_uniforme),
                    sexo = COALESCE(%s, sexo),
                    precio_venta = COALESCE(%s, precio_venta),
                    descripcion = COALESCE(%s, descripcion),
                    talla = COALESCE(%s, talla),
                    cantidad_existencia = COALESCE(%s, cantidad_existencia)
                WHERE id_productoterminado = %s
            '''
            cur.execute(update_script,(id_productoterminado, id_uniforme, sexo,precio_venta, descripcion, talla,cantidad_existencia,id_buscar))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Muestra el error en una ventana emergente
            conn.rollback()
    def productoterminado(codigo,descripcion,talla,sexo,precioventa,cantidadexistencia):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO productoterminado(codigo,descripcion,talla,sexo,precioventa,cantidadexistencia)VALUES(%s,%s,%s,%s,%s,%s)'
            insert_value = (codigo,descripcion,talla,sexo,precioventa,cantidadexistencia)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
######################################################################
    def customConsult(consulta):

        cur = conn.cursor()
        insert_script = consulta
        cur.execute(consulta)
    def insertproveedor(nit, nombre,direccion, telefono):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO proveedor(nit, nombre,direccion, telefono)VALUES(%s,%s,%s,%s)'
            insert_value = (nit, nombre,direccion, telefono)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    def deleteproveedor(NIT):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM proveedor WHERE nit = %s'
            delete_value = (NIT,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    def updateproveedor(dni1, newdn1, newname, newlastn, tel):
        try:
            cur = conn.cursor()
            update_script = '''
            UPDATE proveedor 
            SET nit = COALESCE(NULLIF(%s, ''), nit),
                nombre = COALESCE(NULLIF(%s, ''), nombre),
                direccion = COALESCE(NULLIF(%s, ''), direccion),
                telefono = COALESCE(NULLIF(%s, ''), telefono)
            WHERE nit = %s
            '''
            cur.execute(update_script, (newdn1, newname, newlastn, tel, dni1))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
######################################################################
    def insertSchool(id,nombre,direccion,telefono):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO colegio(id_colegio,direccion,nombre,telefono)VALUES(%s,%s,%s,%s)'
            insert_value = (id,nombre,direccion,telefono)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def deleteSchool(id_colegio):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM colegio WHERE id_colegio = %s'
            delete_value = (id_colegio,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    def updateSchool(dni1, newdn1, newname, newlastn, tel):
        try:
            cur = conn.cursor()
            update_script = '''
            UPDATE colegio 
            SET id_colegio = COALESCE(NULLIF(%s, ''), id_colegio),
                direccion = COALESCE(NULLIF(%s, ''), direccion),
                nombre = COALESCE(NULLIF(%s, ''), nombre),
                telefono = COALESCE(NULLIF(%s, ''), telefono)
            WHERE id_colegio = %s
            '''
            cur.execute(update_script, (newdn1, newname, newlastn, tel, dni1))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
######################################################################
    def insertUniform(id_uniforme,id_colegio,tipo_uniforme,descripcion):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO uniforme(id_uniforme,id_colegio,tipo_uniforme,descripcion)VALUES(%s,%s,%s,%s)'
            insert_value = (id_uniforme,id_colegio,tipo_uniforme,descripcion)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    def deleteUniform(id_uniforme):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM uniforme WHERE id_uniforme = %s'
            delete_value = (id_uniforme,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def UpdateUniform(Id_uniforme_f,id_uniforme,id_colegio,tipo_uniforme,descripcion):
        try:
            cur = conn.cursor()
            update_script = '''
            UPDATE uniforme 
            SET id_uniforme = COALESCE(NULLIF(%s, ''), id_uniforme),
                id_colegio = COALESCE(NULLIF(%s, ''), id_colegio),
                tipo_uniforme = COALESCE(NULLIF(%s, ''), tipo_uniforme),
                descripcion = COALESCE(NULLIF(%s, ''), descripcion)
            WHERE id_uniforme = %s
            '''
            cur.execute(update_script, (id_uniforme,id_colegio,tipo_uniforme,descripcion,Id_uniforme_f))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
######################################################################
    def insertMateria(id_materiaprima,nit,tipo,descripcion,unidadmedida,productos):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO materiaprima(id_materiaprima,nit,tipo,descripcion,unidadmedida,productos)VALUES(%s,%s,%s,%s,%s,%s)'
            insert_value = (id_materiaprima,nit,tipo,descripcion,unidadmedida,productos)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def deleteMateria(id_materiaprima):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM materiaprima WHERE id_materiaprima = %s'
            delete_value = (id_materiaprima,)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()        
    def updateMateria(id_materia_f,id_materiaprima,nit,tipo,descripcion,unidadmedida,productos):
        try:
            cur = conn.cursor()
            update_script = '''
            UPDATE materiaprima 
            SET id_materiaprima = COALESCE(NULLIF(%s, ''), id_materiaprima),
                nit = COALESCE(NULLIF(%s, ''), nit),
                tipo = COALESCE(NULLIF(%s, ''), tipo),
                descripcion = COALESCE(NULLIF(%s, ''), descripcion),
                unidadmedida = COALESCE(NULLIF(%s, ''), unidadmedida),
                productos = COALESCE(NULLIF(%s, ''), productos)
            WHERE id_materiaprima = %s
            '''
            cur.execute(update_script, (id_materiaprima,nit,tipo,descripcion,unidadmedida,productos,id_materia_f))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
######################################################################
    def insertProdMat(id_productoterminado,id_materiaprima):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO productomateria(id_productoterminado,id_materiaprima)VALUES(%s,%s)'
            insert_value = (id_productoterminado,id_materiaprima)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def deleteProdMat(id_productoterminado,id_materiaprima):
        try:
            cur = conn.cursor()
            delete_cript = 'DELETE FROM productomateria WHERE id_productoterminado = %s AND id_materiaprima = %s'
            delete_value = (id_productoterminado,id_materiaprima)
            cur.execute(delete_cript, delete_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def updateProdMat(id_productoterminado,id_materiaprima,newid,newidm):
        try:
            cur = conn.cursor()
            update_script = '''
            UPDATE productomateria 
            SET id_productoterminado = COALESCE(NULLIF(%s, ''), id_productoterminado),
                id_materiaprima = COALESCE(NULLIF(%s, ''), id_materiaprima)
            WHERE id_productoterminado = %s AND id_materiaprima = %s
            '''
            cur.execute(update_script, (newid,newidm,id_productoterminado,id_materiaprima))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
######################################################################
    def verificar_credenciales(username, password):
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s",
                (username, password)
            )
            usuario = cursor.fetchone()
            return usuario  # Retorna None si no se encuentra el usuario
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
######################################################################
    def mostrarPedidosEnEspera():
        query = """
        SELECT 
            c.nombre AS nombre_cliente,
            p.*
        FROM
            pedido p
        JOIN
            cliente c ON p.DNI = c.DNI
        WHERE
            p.estado = 'En Espera'  
        ORDER BY
            p.fechaEntrega;
        """

        cur.execute(query)

        column_names = [desc[0] for desc in cur.description]

        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("PEDIDOS EN ESPERA")

        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cur.fetchall():
            tree.insert("", "end", values=row)
    def mostrarPedidosEnEsperaPorDNI(dni_cliente):
        # Ejecutar la consulta para obtener datos de los pedidos en espera para un cliente específico
        query = f"""
        SELECT
            c.DNI AS dni_cliente,
            c.Nombre AS nombre_cliente,
            p.id_pedido,
            p.fechaEncargo,
            p.fechaEntrega,
            pe.id_productoterminado
        FROM
            cliente c
        JOIN
            pedido p ON c.DNI = p.DNI
        JOIN
            productos_encargados pe ON pe.id_pedido = p.id_pedido
        WHERE
            c.DNI = '{dni_cliente}' AND p.estado = 'En Espera' 
        ORDER BY
            c.DNI, p.fechaEncargo;
            """

        cur.execute(query)

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cur.description]

        # Crear una nueva ventana emergente
        ventana_emergente = tk.Toplevel()
        ventana_emergente.title(f"Pedidos en Espera para DNI: {dni_cliente}")

        # Crear un Treeview en la ventana emergente
        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Agregar datos al Treeview
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
    def existenciaEncargados():
        query = """
        SELECT
            pt.id_productoterminado,
            pt.descripcion AS descripcion_producto,
            pt.cantidad_existencia - COUNT(p.id_productoterminado) AS cantidad_en_existencia
        FROM
            productosTerminados pt
        LEFT JOIN
            productos_encargados p ON pt.id_productoterminado = p.id_productoterminado 
        GROUP BY
            pt.id_productoterminado, pt.descripcion, pt.cantidad_existencia;
        """

        cur.execute(query)

        column_names = [desc[0] for desc in cur.description]

        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("cantidad en existencia descontando los que están encargados")

        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cur.fetchall():
            tree.insert("", "end", values=row)
    def seFabricanUniformes():
        query = """
        SELECT
            c.ID_colegio,
            c.nombre AS nombre_colegio,
            c.direccion,
            c.telefono
        FROM
            colegio c
        JOIN
            uniforme u ON c.ID_colegio = u.ID_colegio
        GROUP BY
            c.ID_colegio, c.nombre, c.direccion, c.telefono
        ORDER BY
            c.nombre;
        """

        cur.execute(query)

        column_names = [desc[0] for desc in cur.description]

        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("Se fabrican uniformes")

        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cur.fetchall():
            tree.insert("", "end", values=row)       
    def caracteristicasUniformes(colegio):
        query = f"""
        SELECT
            c.nombre AS nombre_colegio,
            u.tipo_uniforme,
            u.descripcion AS descripcion_uniforme
        FROM
            colegio c
        JOIN
            uniforme u ON c.ID_colegio = u.ID_colegio
        WHERE
        c.ID_colegio = '{colegio}';
        """

        cur.execute(query)

        column_names = [desc[0] for desc in cur.description]

        ventana_emergente = tk.Toplevel()
        ventana_emergente.title(f"Caracteristicas uniformde el colegio : {colegio}" )

        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cur.fetchall():
            tree.insert("", "end", values=row)   
    def total_ventas():
        query = """
            SELECT COUNT(id_factura),SUM(monto_total) from factura_venta
        """

        cur.execute(query)

        column_names = [desc[0] for desc in cur.description]

        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("PEDIDOS EN ESPERA")

        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cur.fetchall():
            tree.insert("", "end", values=row)
    def agregarprodu(id_pedido,id_productoterminado):
        try:
            cur = conn.cursor()
            insert_cript = 'INSERT INTO productos_encargados(id_productoterminado,id_pedido)VALUES(%s,%s)'
            insert_value = (id_productoterminado,id_pedido)
            cur.execute(insert_cript, insert_value)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            conn.rollback()
    def total_ventas_school():
        query = """
        SELECT SUM(f.monto_total) 
        FROM factura_venta f
        JOIN productos_encargados p ON f.id_pedido = p.id_pedido
        JOIN productosterminados pt ON p.id_productoterminado = pt.id_productoterminado
        WHERE id_uniforme is not null
        """

        cur.execute(query)

        column_names = [desc[0] for desc in cur.description]

        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("PEDIDOS EN ESPERA")

        tree = ttk.Treeview(ventana_emergente, columns=column_names, show="headings")
        tree.grid(row=0, column=0, padx=10, pady=10)
        tree.delete(*tree.get_children())
        tree["columns"] = column_names

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cur.fetchall():
            tree.insert("", "end", values=row)

except Exception as error:
    print(error)
    

 
