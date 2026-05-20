Dashboard APS — Atención Primaria de Salud

Sistema de análisis estadístico avanzado para derivaciones y tiempos de espera en Atención Primaria de Salud (APS), desarrollado con Streamlit y orientado a departamentos de salud municipal, CESFAM y gestión sanitaria.

Descripción

Este proyecto permite analizar datos de derivaciones al nivel secundario de atención mediante un dashboard interactivo, moderno y orientado a auditoría clínica y gestión sanitaria.

El sistema calcula indicadores estadísticos avanzados exclusivamente sobre pacientes efectivamente derivados, separando correctamente el universo total de registros de los casos derivados para evitar sesgos metodológicos en los tiempos de espera.

Incluye:

KPIs ejecutivos
Estadísticas descriptivas avanzadas
Percentiles y dispersión
Ranking por CESFAM
Análisis por especialidad
Evolución temporal
Alertas automáticas
Exportación PDF y CSV
Visualizaciones interactivas
Diseño institucional profesional
Características principales
Análisis estadístico avanzado
Media, mediana y desviación estándar
Percentiles P10, P25, P50, P75, P90 y P95
Coeficiente de variación
Rango e IQR
Índice compuesto de riesgo
Visualizaciones
Histogramas
Boxplots
Violin plots
Gauge indicators
Series temporales
Rankings comparativos
Gestión sanitaria
Identificación de cuellos de botella
Comparación entre establecimientos
Auditoría de tiempos de espera
Evaluación de presión asistencial
Alertas automáticas de riesgo
Exportación
PDF institucional automatizado
Exportación CSV
Impresión optimizada
Reportes descargables
Tecnologías utilizadas
Python
Streamlit
Pandas
NumPy
Plotly
ReportLab
Estructura esperada de datos

El sistema acepta archivos CSV o Excel (.xlsx) con al menos las siguientes columnas:

Columna	Obligatoria	Descripción
Establecimiento	Sí	Nombre del CESFAM o centro
Derivado_Secundario	Sí	Indica si fue derivado (“Sí”)
Dias_Espera	Sí	Tiempo de espera
Especialidad	No	Especialidad médica
Año	No	Año del registro
Mes	No	Mes del registro
Instalación
1. Clonar repositorio
git clone https://github.com/tuusuario/dashboard-aps.git
cd dashboard-aps
2. Crear entorno virtual
python -m venv venv
3. Activar entorno virtual
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
4. Instalar dependencias
pip install -r requirements.txt
Dependencias principales
streamlit
pandas
numpy
plotly
openpyxl
reportlab
Ejecución local
streamlit run app.py

La aplicación quedará disponible en:

http://localhost:8501
Funcionalidades del dashboard
Indicadores clave
Total de registros
Total de derivaciones
Espera media
Percentil 90
Riesgo sistémico
Alertas automáticas

El sistema detecta automáticamente:

P90 crítico
Alta variabilidad
Exceso de derivaciones
Riesgo operativo elevado
Ranking de establecimientos

Permite comparar:

Espera media
Variabilidad
Cantidad de derivaciones
Riesgo relativo
Análisis temporal

Visualiza:

Tendencias históricas
Variabilidad temporal
Evolución del sistema
