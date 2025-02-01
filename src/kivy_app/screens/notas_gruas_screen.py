from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
import requests


class NotaGruasScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Título
        title = MDLabel(text="Crear Nota de Grúas", halign="center", theme_text_color="Primary")
        layout.add_widget(title)

        # Formulario para la nota de grúas
        form = GridLayout(cols=2, spacing=10, size_hint_y=None, height=800)
        form.bind(minimum_height=form.setter('height'))

        # Campos de formulario
        self.cliente_input = MDTextField(hint_text="Cliente")
        self.telefono_input = MDTextField(hint_text="Teléfono")
        self.empresa_input = MDTextField(hint_text="Empresa")
        self.ubicacion_input = MDTextField(hint_text="Ubicación")
        self.equipo_input = MDTextField(hint_text="Equipo")
        self.operador_input = MDTextField(hint_text="Operador")
        self.ayudante_input = MDTextField(hint_text="Ayudante")
        self.trabajo_realizado_input = MDTextField(hint_text="Trabajo Realizado")

        # Campos de fecha y hora usando MDTextField
        self.fecha_input = MDTextField(hint_text="Fecha", readonly=True)
        self.fecha_input.bind(on_focus=self.show_date_picker)

        self.hora_salida_input = MDTextField(hint_text="Hora de salida", readonly=True)
        self.hora_salida_input.bind(on_focus=self.show_time_picker)

        self.hora_llegada_input = MDTextField(hint_text="Hora de llegada", readonly=True)
        self.hora_llegada_input.bind(on_focus=self.show_time_picker)

        self.hora_termino_input = MDTextField(hint_text="Hora de término", readonly=True)
        self.hora_termino_input.bind(on_focus=self.show_time_picker)

        self.hora_regreso_input = MDTextField(hint_text="Hora de regreso", readonly=True)
        self.hora_regreso_input.bind(on_focus=self.show_time_picker)

        # Campos de costos
        self.horas_trabajo_input = MDTextField(hint_text="Horas de Trabajo")
        self.costo_hora_input = MDTextField(hint_text="Costo por Hora")
        self.costo_maniobra_input = MDTextField(hint_text="Costo de Maniobra")
        self.costo_maniobra_iva_input = MDTextField(hint_text="Costo Maniobra con IVA")

        # Añadir los campos al formulario
        for widget in [
            self.cliente_input, self.telefono_input, self.empresa_input, self.ubicacion_input,
            self.equipo_input, self.operador_input, self.ayudante_input, self.trabajo_realizado_input,
            self.fecha_input, self.hora_salida_input, self.hora_llegada_input,
            self.hora_termino_input, self.hora_regreso_input, self.horas_trabajo_input,
            self.costo_hora_input, self.costo_maniobra_input, self.costo_maniobra_iva_input
        ]:
            form.add_widget(widget)

        layout.add_widget(form)

        # Botón de enviar
        send_button = MDRaisedButton(text="Enviar Nota", size_hint=(None, None), size=("200dp", "50dp"))
        send_button.bind(on_release=self.send_nota)
        layout.add_widget(send_button)

        # Añadir el layout a la pantalla
        self.add_widget(layout)

    def show_date_picker(self, instance, value):
        """Abre el selector de fecha cuando el campo es enfocado."""
        if value:
            date_picker = MDDatePicker()
            date_picker.bind(on_save=self.set_date)
            date_picker.open()

    def set_date(self, instance, value, date_range):
        """Establece la fecha seleccionada en el campo."""
        self.fecha_input.text = str(value)

    def show_time_picker(self, instance, value):
        """Abre el selector de hora cuando el campo es enfocado."""
        if value:
            time_picker = MDTimePicker()
            time_picker.bind(time=self.set_time)
            time_picker.open()
            self.selected_time_input = instance  # Guardamos qué campo llamó al selector

    def set_time(self, instance, value):
        """Establece la hora seleccionada en el campo correcto."""
        if self.selected_time_input:
            self.selected_time_input.text = str(value)

    def send_nota(self, instance):
        """Envía la información de la nota a la API."""
        try:
            data = {
                "cliente": self.cliente_input.text,
                "telefono": self.telefono_input.text,
                "empresa": self.empresa_input.text,
                "ubicacion": self.ubicacion_input.text,
                "equipo": self.equipo_input.text,
                "operador": self.operador_input.text,
                "ayudante": self.ayudante_input.text,
                "trabajo_realizado": self.trabajo_realizado_input.text,
                "fecha": self.fecha_input.text,
                "hora_salida": self.hora_salida_input.text,
                "hora_llegada": self.hora_llegada_input.text,
                "hora_termino": self.hora_termino_input.text,
                "hora_regreso": self.hora_regreso_input.text,
                "horas_trabajo": float(self.horas_trabajo_input.text) if self.horas_trabajo_input.text else 0,
                "costo_hora": int(self.costo_hora_input.text) if self.costo_hora_input.text else 0,
                "costo_maniobra": float(self.costo_maniobra_input.text) if self.costo_maniobra_input.text else 0,
                "costo_maniobra_iva": float(self.costo_maniobra_iva_input.text) if self.costo_maniobra_iva_input.text else 0,
            }

            API_URL = "http://127.0.0.1:8000/api/nota/"
            response = requests.post(API_URL, json=data)

            if response.status_code == 201:
                print("Nota creada con éxito.")
            else:
                print("Error al crear la nota.")

        except Exception as e:
            print(f"Error: {e}")