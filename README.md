# Microservicio Flask: Factorial y Paridad

Pequeño microservicio en **Flask** que recibe un número por URL y devuelve JSON con:
- `numero` recibido
- `factorial` del número
- `etiqueta` `"par"` o `"impar"` según el número

## Ejecutar en local

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# Visita: http://127.0.0.1:8000/numero/5
```

Salida de ejemplo:

```json
{"numero": 5, "factorial": 120, "etiqueta": "impar"}
```

Ruta:
- `GET /numero/<int:n>`


##  Análisis: ¿cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa?

Si el microservicio debe conectarse con un **History Service** que guarda los cálculos, se pueden hacer algunos ajustes sencillos:

1. **Integración vía HTTP o mensajería:**  
   Después de calcular el resultado, el microservicio enviaría los datos (`número`, `factorial`, `etiqueta`) al servicio de historial.

2. **Desacoplamiento y resiliencia:**  
   Para no afectar la respuesta al usuario, el envío debe hacerse en segundo plano y con reintentos automáticos en caso de fallo.

3. **Seguridad y consistencia:**  
   Usar autenticación entre servicios (por ejemplo, **API Key** o **JWT**) y mantener un formato *JSON* estable para los eventos enviados.

4. **Cambios mínimos al código:**  
   - Añadir la librería `requests`.  
   - Configurar la URL y credenciales del History Service en variables de entorno.  
   - Incluir una pequeña función que envíe los datos en background.  


---

## Estructura del repo

```
.
├── app.py
├── Dockerfile
├── README.md
└── requirements.txt
```
