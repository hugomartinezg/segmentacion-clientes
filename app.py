from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# Cargar base de datos y entrenar modelo
data = pd.read_csv("datos_con_segmento.csv")
X = data[['frecuencia_compra', 'monto_promedio']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Asignar nombres a los clusters
cluster_monto_mean = data.groupby('cluster')['monto_promedio'].mean().sort_values(ascending=False)
group_labels = ['Compradores Frecuentes Premium', 'Ocasionales Económicos', 'Regulares Balanceados']
cluster_name_map = {cluster: group_labels[i] for i, cluster in enumerate(cluster_monto_mean.index)}

# Crear app
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/clasificar', methods=['POST'])
def clasificar_usuario():
    input_data = request.get_json()
    freq = input_data.get('frecuencia_compra')
    monto = input_data.get('monto_promedio')

    if freq is None or monto is None:
        return jsonify({'error': 'Faltan variables: frecuencia_compra y monto_promedio'}), 400

    input_scaled = scaler.transform([[freq, monto]])
    cluster = kmeans.predict(input_scaled)[0]
    segmento = cluster_name_map[cluster]

    return jsonify({'cluster': int(cluster), 'segmento': segmento})


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)