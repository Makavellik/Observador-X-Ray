<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=140&section=header&text=OBSERVADOR%20X-RAY&fontSize=52&fontColor=00FFD5&animation=twinkle&color=0,10,20,30,40,60" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=20&pause=1000&color=00FFD5&center=true&vCenter=true&width=720&lines=OBSERVING+HTTP+SIGNALS...;CORRELATING+TIMING+AND+HEADERS...;BACKEND+INFERENCE+IN+PROGRESS...;FORENSIC+MODE+ACTIVE" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=17&pause=900&color=FFAA00&center=true&vCenter=true&width=760&lines=LATENCY+PROFILING+ENGAGED...;HEADER+ENTROPY+MEASURED...;STATE+TRANSITIONS+DETECTED...;ARCHITECTURAL+SIGNALS+LOCKED" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Roboto+Mono&size=18&pause=1100&color=FF33FF&center=true&vCenter=true&width=700&lines=SURGICAL+TIMING+ANALYSIS...;NOISE+LEVEL%3A+ULTRA-LOW...;ETHICAL+FORENSICS+ONLY...;READY+FOR+INTERPRETATION" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FORENSIC--ENGINE-PASSIVE%20INTELLIGENCE-00ffd5?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ANALYSIS-SURGICAL%20TIMING-ff006e?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ETHICS-PASSIVE%20SAFE-7c4dff?style=for-the-badge" />
</p>

<p align="center">
🧠 Observabilidad profunda · ⏱️ Timing quirúrgico · 🧬 Entropía · 🛡️ Ética forense
</p>


---

## ✨ ¿Qué es esto?

**Observador X‑RAY** es un motor de análisis **forense web** diseñado para **observar** (no atacar) el comportamiento de un endpoint HTTP(S) mediante **estímulos seguros**, **mediciones temporales**, y **correlación de cabeceras**.

No busca vulnerar sistemas. Busca **entenderlos**.

> Piensa en X‑RAY como un **estetoscopio** para arquitecturas web: escucha latencias, observa cabeceras y deduce cómo late el backend.

---

## 🧭 ¿Para qué sirve?

* 🔍 **Perfilado arquitectónico** (edge, cache, balanceo, backend diversity)
* ⏱️ **Análisis de timing** (jitter, normalización, reintentos silenciosos)
* 🧬 **Forense de headers** (entropía, orden, estabilidad)
* 🛡️ **Evaluación defensiva pasiva** (postura de hardening)
* 🧪 **Investigación y aprendizaje** (blue team, red team ético, bug bounty)

---

## 🚫 ¿Para qué NO es?

* ❌ No es un scanner de vulnerabilidades
* ❌ No explota CVEs
* ❌ No hace fuzzing agresivo
* ❌ No evade WAFs
* ❌ No genera carga ni DoS

**X‑RAY observa, no agrede.**

---

## 🧠 Filosofía del diseño

* **Ruido ultra bajo**
* **Estímulos humanos realistas**
* **Inferencia > fuerza bruta**
* **Ética primero**
* **Resultados interpretables**

Cada request está pensada como una **pregunta sutil** al sistema.

---

## 🧩 Componentes clave

### 🔬 Motor X‑RAY (`XRayAnalyzer`)

* Timing fingerprinting
* Header hashing + entropía
* Detección de variación backend
* Inferencia de intención defensiva

### 🌐 API (FastAPI)

* `POST /api/analyze` → análisis JSON
* `GET /` → UI web

### 🧠 UI

* Interfaz simple para ejecutar análisis
* Hardening de headers en frontend

---

## 📦 Requisitos

* Python **3.9+**
* Sistema operativo: Linux / macOS / Windows

---

## ⚙️ Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/Makavellik/observador-xray.git
cd observador-xray

# 2. Crea entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# 3. Instala dependencias
pip install -r requirements.txt
```

**Dependencias principales:**

* fastapi
* httpx
* jinja2
* uvicorn

---

## 🚀 Ejecución

```bash
python -m uvicorn forensic:app --reload
```

Luego abre:

👉 [http://localhost:8000](http://localhost:8000)

---

## 🧪 Uso vía API

```http
POST /api/analyze
Content-Type: application/x-www-form-urlencoded

url=https://example.com
```

### 📤 Respuesta

```json
{
  "url": "https://example.com",
  "findings": [
    {
      "name": "header_instability",
      "detail": "Headers mutan → ejecución condicional interna",
      "classification": "security-impact",
      "confidence": 0.85
    }
  ],
  "timeline": [
    {"sample": 1, "status": 200, "time_ms": 123.4}
  ]
}
```

---

## 🧠 Cómo interpretar los resultados

### 📌 `classification`

* `hygiene` → buenas prácticas
* `architectural` → pistas de diseño interno
* `security-impact` → controles defensivos
* `hardening` → robustez estructural

### 📊 `confidence`

Valor entre **0 y 1** que indica la fuerza de la inferencia.

---

## 🛡️ Seguridad y ética

* ✔️ Requests limitados y espaciados
* ✔️ Sin payloads maliciosos
* ✔️ Sin evasión
* ✔️ Sin fingerprinting invasivo

**Usa X‑RAY solo en sistemas que:

* sean tuyos
* tengas permiso
* o con fines educativos**

---

## 🧬 Casos de uso reales

* Blue Team: entender superficie defensiva
* Bug Bounty: mapear arquitectura antes de testear
* DevOps: validar estabilidad y caching
* Investigación: fingerprinting defensivo

---

## 🧠 Roadmap (ideas)

* Visualización de clusters de timing
* Exportación a JSONL / CSV
* Modo comparación (antes vs después)
* Plugin para Tor / Onion (pasivo)

---

## 🧑‍🚀 Info del Autor

Creado con bisturí, lupa y respeto por la red.

**Modo:** observador
**Rol:** forense
**Ética:** primero

---

<div align="center">

✨ *"No todo análisis necesita ruido. A veces solo escuchar es suficiente."* ✨
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=110&section=header&text=By%20Makaveliw&fontSize=42&fontColor=FF0055&animation=fadeIn&color=10,0,20,40,60" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=18&pause=1000&color=FF0055&center=true&vCenter=true&width=600&lines=FORENSIC+OBSERVER;ARCHITECTURE+READER;SIGNAL+INTERPRETER;CODE+WITH+ETHICS" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AUTHOR-BYMakaveli-ff0055?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ROLE-FORENSIC%20OBSERVER-00ffd5?style=for-the-badge" />
</p>

<p align="center">
✨ « Escuchar primero. Inferir después. Respetar siempre. » ✨
</p>


</div>
