import requests

class ApiClient:
    @staticmethod
    def enviar_datos_cliente(datos):
        """Envía los datos del formulario al backend de Django."""
        url = "http://192.168.100.7:8000/api/notas_gruas/"  # URL de tu API en Django
        try:
            response = requests.post(url, json=datos)
            if response.status_code == 201:  # Si se creó correctamente
                print("Datos enviados con éxito.")
            else:
                print(f"Error al enviar los datos: {response.status_code}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")