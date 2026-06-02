#  Dashboard APS — Atención Primaria de Salud
<img width="1521" height="778" alt="Captura de pantalla 2026-05-20 153316" src="https://github.com/user-attachments/assets/ef1509db-260b-42ff-9538-84867c8f3ab9" />



Sistema de análisis estadístico avanzado para derivaciones y tiempos de espera en Atención Primaria de Salud (APS), desarrollado con Streamlit y orientado a departamentos de salud municipal, CESFAM y gestión sanitaria.

---

#  Descripción

Este proyecto permite analizar datos de derivaciones al nivel secundario de atención mediante un dashboard interactivo, moderno y orientado a auditoría clínica y gestión sanitaria.

El sistema calcula indicadores estadísticos avanzados exclusivamente sobre pacientes efectivamente derivados, separando correctamente el universo total de registros de los casos derivados para evitar sesgos metodológicos en los tiempos de espera.

---

#  Incluye

- KPIs ejecutivos
- Estadísticas descriptivas avanzadas
- Percentiles y dispersión
- Ranking por CESFAM
- Análisis por especialidad
- Evolución temporal
- Alertas automáticas
- Exportación PDF y CSV
- Visualizaciones interactivas
- Diseño institucional profesional

---

#  Características principales

##  Análisis estadístico avanzado

- Media, mediana y desviación estándar
- Percentiles P10, P25, P50, P75, P90 y P95
- Coeficiente de variación
- Rango e IQR
- Índice compuesto de riesgo

##  Visualizaciones

- Histogramas
- Boxplots
- Violin plots
- Gauge indicators
- Series temporales
- Rankings comparativos

##  Gestión sanitaria

- Identificación de cuellos de botella
- Comparación entre establecimientos
- Auditoría de tiempos de espera
- Evaluación de presión asistencial
- Alertas automáticas de riesgo

##  Exportación

- PDF institucional automatizado
- Exportación CSV
- Impresión optimizada
- Reportes descargables

---

#  Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- ReportLab

---

#  Estructura esperada de datos

El sistema acepta archivos CSV o Excel (`.xlsx`) con al menos las siguientes columnas:

| Columna | Obligatoria | Descripción |
|---|---|---|
| Establecimiento | Sí | Nombre del CESFAM o centro |
| Derivado_Secundario | Sí | Indica si fue derivado (“Sí”) |
| Dias_Espera | Sí | Tiempo de espera |
| Especialidad | No | Especialidad médica |
| Año | No | Año del registro |
| Mes | No | Mes del registro |

---
#  Mockup 
[Ver demo interactiva](https://www.figma.com/make/yp9DMq5RJkdMxHkvFVdM56/Interactive-GitHub-Dashboard?code-node-id=0-9&p=f&t=oAoezMkz0rbAcRbN-0&fullscreen=1)

#  Instalación

##  Clonar repositorio

```bash
git clone https://github.com/tuusuario/dashboard-aps.git
cd dashboard-aps
```

##  Crear entorno virtual

```bash
python -m venv venv
```

##  Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

##  Instalar dependencias

```bash
pip install -r requirements.txt
```

---

#  Dependencias principales

```txt
streamlit
pandas
numpy
plotly
openpyxl
reportlab
```

---

#  Ejecución local

```bash
streamlit run app.py
```

La aplicación quedará disponible en:

```txt
http://localhost:8501
```

---

#  Funcionalidades del dashboard

##  Indicadores clave

- Total de registros
- Total de derivaciones
- Espera media
- Percentil 90
- Riesgo sistémico

##  Alertas automáticas

El sistema detecta automáticamente:

- P90 crítico
- Alta variabilidad
- Exceso de derivaciones
- Riesgo operativo elevado

##  Ranking de establecimientos

Permite comparar:

- Espera media
- Variabilidad
- Cantidad de derivaciones
- Riesgo relativo

##  Análisis temporal

Visualiza:

- Tendencias históricas
- Variabilidad temporal
- Evolución del sistema

---

#  Metodología estadística

Todos los indicadores de tiempos de espera se calculan exclusivamente sobre pacientes derivados al nivel secundario:

```python
df_der = df[df["Derivado_Secundario"] == "Sí"]
```

Esto evita distorsiones estadísticas producidas por incluir pacientes no derivados en análisis de espera.

---

#  Exportación PDF

El sistema genera informes institucionales automáticos con:

- Estadísticas descriptivas
- Rankings
- Interpretación estadística
- Tablas profesionales
- Formato imprimible

---

#  Mejoras futuras

- Integración SQL
- Login institucional
- Predicción de listas de espera
- Benchmark automático entre CESFAM
- Machine Learning predictivo
- API REST
- Dashboard multiusuario

---

#  Autor

Proyecto desarrollado para análisis y gestión de derivaciones APS mediante herramientas modernas de análisis estadístico y visualización de datos.
que sea mas sintetizado , esta muy largo
#  Dashboard APS — Atención Primaria de Salud

![Dashboard](assets/dashboard_main.png)

Sistema de análisis estadístico para derivaciones y tiempos de espera en APS, desarrollado con Streamlit y orientado a gestión sanitaria y auditoría clínica.

---

##  Funcionalidades

- KPIs ejecutivos
- Estadísticas descriptivas avanzadas
- Percentiles y análisis de dispersión
- Ranking por CESFAM
- Análisis por especialidad
- Evolución temporal
- Alertas automáticas
- Exportación PDF y CSV
- Visualizaciones interactivas

---

##  Tecnologías

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- ReportLab

---

##  Dataset esperado

| Columna | Descripción |
|---|---|
| Establecimiento | CESFAM o centro |
| Derivado_Secundario | Sí / No |
| Dias_Espera | Tiempo de espera |
| Especialidad | Especialidad médica |
| Año | Año registro |
| Mes | Mes registro |

---

##  Instalación

```bash
git clone https://github.com/TU_USUARIO/aps-referral-analytics-dashboard.git
cd aps-referral-analytics-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## <img width="1521" height="778" alt="Captura de pantalla 2026-05-20 153316" src="https://github.com/user-attachments/assets/471a368e-e83f-4e44-b0cb-92bb7c65bbc2" />
 Características analíticas

- Media, mediana y desviación estándar
- Percentiles P10–P95
- Coeficiente de variación
- Índice compuesto de riesgo
- Boxplots, histogramas y series temporales

---

## 📄 Exportación

- Informe PDF institucional
- Exportación CSV
- Impresión optimizada

---

##  Metodología

Todos los análisis de tiempos de espera se calculan exclusivamente sobre pacientes efectivamente derivados al nivel secundario:

```python
df_der = df[df["Derivado_Secundario"] == "Sí"]
```

---

##  Autor: Camilo Rozas 

Proyecto desarrollado para análisis estadístico y visualización avanzada de derivaciones APS.
