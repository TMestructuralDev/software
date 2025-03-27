from kivymd.uix.screen import MDScreen
from widgets.date_picker import DatePicker  
from widgets.time_picker import TimePicker
from utils.validacion import ValidacionFormulario
from utils.calculos import Calculos
from kivy.properties import StringProperty 

class NotaGruasScreen(MDScreen):
    
    cliente = StringProperty("")
    telefono = StringProperty("")
    fecha = StringProperty("")
    empresa = StringProperty("")
    ubicacion = StringProperty("")
    equipo = StringProperty("")
    operador = StringProperty("")
    ayudante = StringProperty("")
    trabajo_realizado = StringProperty("")
    hora_salida = StringProperty("")
    hora_llegada = StringProperty("")
    hora_termino = StringProperty("")
    hora_regreso = StringProperty("")
    costo_hora = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_picker = DatePicker()
        self.time_picker = TimePicker()
        self.validacion_formulario = ValidacionFormulario()

    def open_date_picker(self, caller):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.date_picker.show_date_picker(caller)
        
    def open_time_picker(self, caller):
        """Llama al DatePicker y pasa el campo de texto que lo activó."""
        self.time_picker.show_time_picker(caller)
        
    def enviar_datos(self):
        """Recopila todos los datos desde el formulario y los envía al backend."""
        self.validacion_formulario.enviar_datos() # Llamamos a la función enviar_datos()

    def enviar_datos(self):
        """Recopila todos los datos desde el formulario y los envía al backend."""
        # Recopilamos los datos directamente de los campos del formulario
        datos = {
            "cliente": self.ids.cliente.text.strip(),
            "telefono": self.ids.telefono.text.strip(),
            "fecha": self.ids.fecha.text.strip(),
            "empresa": self.ids.empresa.text.strip(),
            "ubicacion": self.ids.ubicacion.text.strip(),
            "equipo": self.ids.equipo.text.strip(),
            "operador": self.ids.operador.text.strip(),
            "ayudante": self.ids.ayudante.text.strip(),
            "trabajo_realizado": self.ids.trabajo_realizado.text.strip(),
            "hora_salida": self.ids.hora_salida.text.strip(),
            "hora_llegada": self.ids.hora_llegada.text.strip(),
            "hora_termino": self.ids.hora_termino.text.strip(),
            "hora_regreso": self.ids.hora_regreso.text.strip(),
            "costo_hora": self.ids.costo_hora.text.strip(),
        }

        # Realizar cálculos
        total_horas = Calculos.calcular_total_horas(datos["hora_salida"], datos["hora_regreso"])
        if total_horas is None:
            self.ids.error.text = "[color=ff0000]Error en formato de hora[/color]"
            return

        total_sin_iva = Calculos.calcular_total_sin_iva(total_horas, datos["costo_hora"])
        if total_sin_iva is None:
            self.ids.error.text = "[color=ff0000]Error en costo por hora[/color]"
            return

        total_con_iva = Calculos.calcular_total_con_iva(total_sin_iva)
        
        # Mostrar los resultados en la consola
        print(f"Total de horas: {total_horas}")
        print(f"Total sin IVA: {total_sin_iva}")
        print(f"Total con IVA: {total_con_iva}")

        # Agregar los cálculos al diccionario de datos
        datos["total_horas"] = total_horas
        datos["total_sin_iva"] = total_sin_iva
        datos["total_con_iva"] = total_con_iva

        # Validar datos antes de enviarlos
        mensaje_error = self.validacion_formulario.enviar_datos(datos)
        if mensaje_error:
            self.ids.error.text = f"[color=ff0000]{mensaje_error}[/color]"
        else:
            self.ids.error.text = "[color=00ff00]Datos enviados correctamente[/color]"
            
            
        # Limpiar el formulario
        self.limpiar_formulario()

        # Redirigir a la pantalla "home_screen"
        self.manager.current = "home_screen"
        

    def limpiar_formulario(self):
        """Limpia todos los campos del formulario."""
        for campo in ["cliente", "telefono", "fecha", "empresa", "ubicacion", 
                    "equipo", "operador", "ayudante", "trabajo_realizado", 
                    "hora_salida", "hora_llegada", "hora_termino", "hora_regreso", "costo_hora"]:
            self.ids[campo].text = ""

        self.ids.error.text = ""