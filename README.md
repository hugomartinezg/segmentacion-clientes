# Proyecto de Segmentación de Clientes

Este proyecto realiza una segmentación de clientes basada en sus patrones de compra utilizando clustering (KMeans). La aplicación está construida con Flask y permite clasificar nuevos usuarios en uno de tres segmentos.

## Segmentos

1. **Compradores Frecuentes Premium**
2. **Ocasionales Económicos**
3. **Regulares Balanceados**

## Uso

### Clasificación de un nuevo usuario

Enviar una solicitud POST a `/clasificar` con el siguiente formato JSON:

```json
{
  "frecuencia_compra": 5,
  "monto_promedio": 2000
}
```

### Respuesta esperada

```json
{
  "cluster": 1,
  "segmento": "Regulares Balanceados"
}
```

## Archivos

- `app.py`: Código de la aplicación Flask.
- `datos_con_segmento.csv`: Base de datos utilizada y actualizable.
- `requirements.txt`: Dependencias necesarias.

## Instrucciones

```bash
pip install -r requirements.txt
python app.py
```

La API estará disponible en `http://127.0.0.1:5000/`.