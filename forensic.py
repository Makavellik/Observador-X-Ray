import time
import statistics
from typing import Dict, List
from enum import Enum
import hashlib
import math
import random
import httpx
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

# ==========================================================
# CONFIG
# ==========================================================

TIMEOUT = 8.0
SAMPLES = 4
USER_AGENT = (
    "Mozilla/5.0 "
    "(compatible; XRay; "
    "rv=0.0; like Gecko) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36 "
    "[arch=intent-inference;"
    "mode=adaptive;"
    "stimuli=conditional,negotiation,range,cache-variance;"
    "profiling=temporal,structural,behavioral;"
    "noise=ultra-low;"
    "entropy=balanced;"
    "role=observer;"
    "ethics=passive-safe;"
    "rfc=7231|9110]"
)

def build_xray_request(seed: int):
    rng = random.Random(seed)  # 🔒 RNG aislado (sin huella global)

    # 🧠 Timing humano (activo, no ruidoso)
    cognitive_delay = rng.uniform(0.08, 0.35)
    time.sleep(cognitive_delay)

    headers = {
        # 🧬 Identidad principal (no se toca)
        "User-Agent": USER_AGENT,

        # 🌐 Navegación realista
        "Accept": rng.choice([
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "text/html,application/json;q=0.9,*/*;q=0.7"
        ]),
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": rng.choice([
            "en-US,en;q=0.9",
            "es-ES,es;q=0.9,en;q=0.8",
            "en-GB,en;q=0.8"
        ]),

        # 🧠 Estímulos arquitectónicos reales
        "Cache-Control": rng.choice([
            "no-cache",
            "max-age=0",
            "no-store"
        ]),
        "Pragma": rng.choice(["no-cache", ""]),

        # 🧩 Señales humanas suaves
        "DNT": rng.choice(["0", "1"]),
        "Upgrade-Insecure-Requests": "1",
    }

    # 🧪 Client Hints coherentes con Chrome-like
    if "Chrome/" in USER_AGENT:
        headers.update({
            "Sec-CH-UA": '"Chromium";v="120", "Not(A:Brand";v="24"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": rng.choice([
                '"Windows"',
                '"Linux"',
                '"macOS"'
            ])
        })

    # 🧼 Conexión solo si aporta naturalidad
    if rng.random() > 0.55:
        headers["Connection"] = "keep-alive"

    # 📐 Metadata interna (no enviada)
    meta = {
        "delay": round(cognitive_delay, 3),
        "entropy_profile": "balanced",
        "stimuli_mode": "adaptive-conditional",
        "fingerprint_risk": "low",
        "observer_role": True,
    }

    return headers, meta

# ==========================================================
# MODELOS
# ==========================================================

class FindingClass(str, Enum):
    HYGIENE = "hygiene"
    ARCHITECTURAL = "architectural"
    SECURITY = "security-impact"
    HARDENING = "hardening"

class Finding:
    def __init__(self, name: str, detail: str, cls: FindingClass, confidence: float):
        self.name = name
        self.detail = detail
        self.classification = cls
        self.confidence = confidence

    def as_dict(self):
        return self.__dict__

# ==========================================================
# MOTOR X-RAY
# ==========================================================
  
class XRayAnalyzer:
    def __init__(self, url: str):
        self.url = url
        self.findings: List[Finding] = []
        self.timings: List[float] = []
        self.headers_snapshots: List[Dict[str, str]] = []
        self.status_codes: List[int] = []

        # ---- EXTENSIONES INTERNAS ----
        self._timing_deltas: List[float] = []
        self._header_hashes: List[str] = []
        self._anomaly_counter: int = 0

        # ---- EXTENSIONES X-RAY ----
        self._header_entropy: List[float] = []
        self._state_transitions: List[str] = []
        self._retry_suspicions: int = 0

        # ---- EXTENSIONES QUIRÚRGICAS  ----
        self._response_size_profile: List[int] = []
        self._cache_signal: List[bool] = []
        self._timing_clusters: Dict[str, int] = {}
        self._stability_score: float = 0.0
        self._intent_vectors: Dict[str, float] = {}

        # ---- EXTENSIONES ATACANTE FORENSE ----
        self._header_order_fingerprint: List[str] = []
        self._compression_signal: List[bool] = []
        self._security_headers_score: float = 0.0
        self._backend_variance_index: float = 0.0
        self._execution_noise: List[float] = []

    # ===========================
    # CORE 
    # ===========================

    async def run(self):
        await self._timing_fingerprint()
        await self._header_consistency()
        self._analyze_variance()
        self._infer_architecture()
        return self._report()

    # ===========================
    # ACTIVE SAFE STIMULI 
    # ===========================
    async def _timing_fingerprint(self):
        async with httpx.AsyncClient(
            timeout=TIMEOUT,
            headers={"User-Agent": USER_AGENT},
            follow_redirects=True,
            verify=True
        ) as client:

            last_time = None
            last_status = None

            for _ in range(SAMPLES):
                t0 = time.perf_counter()
                try:
                    r = await client.get(self.url)
                    elapsed = (time.perf_counter() - t0) * 1000

                    self.timings.append(round(elapsed, 2))
                    self.status_codes.append(r.status_code)
                    self.headers_snapshots.append(dict(r.headers))
                    self._response_size_profile.append(len(r.content))

                    # ---- TRANSICIÓN DE ESTADO ----
                    if last_status is not None and r.status_code != last_status:
                        self._state_transitions.append(
                            f"{last_status}->{r.status_code}"
                        )
                    last_status = r.status_code

                    # ---- DELTA TEMPORAL ----
                    if last_time is not None:
                        delta = abs(elapsed - last_time)
                        self._timing_deltas.append(round(delta, 2))
                        self._execution_noise.append(delta)

                        if delta > 40:
                            self._anomaly_counter += 1
                        if delta > elapsed * 0.7:
                            self._retry_suspicions += 1
                    last_time = elapsed

                    # ---- FINGERPRINT DE HEADERS ----
                    header_hash = self._hash_headers(r.headers)
                    self._header_hashes.append(header_hash)

                    # ---- ENTROPÍA ----
                    self._header_entropy.append(self._entropy(header_hash))

                    # ---- ORDEN DE HEADERS (BACKEND CLUE) ----
                    self._header_order_fingerprint.append(
                        ",".join(r.headers.keys())
                    )

                    # ---- CACHE / COMPRESIÓN ----
                    self._cache_signal.append(
                        "x-cache" in r.headers or "age" in r.headers
                    )
                    self._compression_signal.append(
                        "content-encoding" in r.headers
                    )

                except Exception as e:
                    self.findings.append(Finding(
                        "request_error",
                        str(e),
                        FindingClass.ARCHITECTURAL,
                        0.6
                    ))

    # ===========================
    # HEADER FORENSICS (DEEP)
    # ===========================

    async def _header_consistency(self):
        if not self.headers_snapshots:
            return

        base = self.headers_snapshots[0]
        unstable = any(snap != base for snap in self.headers_snapshots[1:])

        if unstable:
            self.findings.append(Finding(
                "header_instability",
                "Headers mutan → ejecución condicional interna",
                FindingClass.SECURITY,
                0.85
            ))
        else:
            self.findings.append(Finding(
                "header_determinism",
                "Headers rígidos → pipeline normalizado",
                FindingClass.HARDENING,
                0.92
            ))

        # ---- SECURITY HEADERS SCORE ----
        security_headers = [
            "content-security-policy",
            "strict-transport-security",
            "x-frame-options",
            "x-content-type-options",
            "referrer-policy"
        ]
        present = sum(1 for h in security_headers if h in base)
        self._security_headers_score = present / len(security_headers)

        if self._security_headers_score < 0.4:
            self.findings.append(Finding(
                "security_headers_weak",
                "Postura defensiva baja a nivel cabecera",
                FindingClass.SECURITY,
                0.78
            ))

        # ---- ENTROPÍA GLOBAL ----
        if self._header_entropy:
            avg_entropy = statistics.mean(self._header_entropy)
            if avg_entropy > 3.6:
                self.findings.append(Finding(
                    "header_entropy_high",
                    "Alta entropía → AB testing / routing adaptativo",
                    FindingClass.ARCHITECTURAL,
                    0.8
                ))

        # ---- ORDEN DE HEADERS ----
        if len(set(self._header_order_fingerprint)) > 1:
            self.findings.append(Finding(
                "backend_variance_detected",
                "Orden de headers varía → múltiples backends",
                FindingClass.SECURITY,
                0.86
            ))

    # ===========================
    # TIMING BISTURÍ
    # ===========================

    def _analyze_variance(self):
        if len(self.timings) < 2:
            return

        mean = statistics.mean(self.timings)
        std = statistics.pstdev(self.timings)

        self._backend_variance_index = std / max(mean, 1)

        if std < 3:
            self.findings.append(Finding(
                "timing_flat",
                "Latencia normalizada → control agresivo",
                FindingClass.HARDENING,
                0.9
            ))

        if std > 25:
            self.findings.append(Finding(
                "timing_jitter_high",
                "Jitter elevado → ejecución no lineal",
                FindingClass.ARCHITECTURAL,
                0.8
            ))

        if self._retry_suspicions:
            self.findings.append(Finding(
                "silent_retry_pattern",
                "Reintentos internos detectados",
                FindingClass.SECURITY,
                0.85
            ))

        self._cluster_timings()

    # ===========================
    # ARQUITECTURA 
    # ===========================

    def _infer_architecture(self):
        headers = self.headers_snapshots[0] if self.headers_snapshots else {}

        if "cf-ray" in headers:
            self.findings.append(Finding(
                "cloudflare_edge",
                "Protección edge gestionada",
                FindingClass.HARDENING,
                0.95
            ))

        if all(code == self.status_codes[0] for code in self.status_codes):
            self.findings.append(Finding(
                "status_normalization",
                "Estados HTTP normalizados",
                FindingClass.HARDENING,
                0.84
            ))

        if self._anomaly_counter and len(set(self._header_hashes)) > 1:
            self.findings.append(Finding(
                "internal_branching",
                "Tiempo + headers → bifurcación interna",
                FindingClass.SECURITY,
                0.88
            ))

        if self._state_transitions:
            self.findings.append(Finding(
                "state_transitions",
                f"Estados detectados: {set(self._state_transitions)}",
                FindingClass.ARCHITECTURAL,
                0.8
            ))

        self._derive_intent_vectors()

    # ===========================
    # UTILIDADES QUIRÚRGICAS
    # ===========================

    def _hash_headers(self, headers: Dict[str, str]) -> str:
        raw = "|".join(f"{k}:{v}" for k, v in sorted(headers.items()))
        return hashlib.sha256(raw.encode()).hexdigest()

    def _entropy(self, data: str) -> float:
        freq = {c: data.count(c) for c in set(data)}
        length = len(data)
        return -sum((v / length) * math.log2(v / length) for v in freq.values())

    def _cluster_timings(self):
        for t in self.timings:
            bucket = f"{int(t//10)*10}-{int(t//10)*10+9}"
            self._timing_clusters[bucket] = self._timing_clusters.get(bucket, 0) + 1

    def _derive_intent_vectors(self):
        self._intent_vectors = {
            "defensive_control": self._security_headers_score,
            "adaptivity": float(len(set(self._header_hashes)) > 1),
            "execution_noise": min(1.0, statistics.mean(self._execution_noise) / 50)
            if self._execution_noise else 0.0,
            "backend_diversity": float(len(set(self._header_order_fingerprint)) > 1)
        }

    # ===========================
    # REPORT 
    # ===========================

    def _report(self):
        return {
            "url": self.url,
            "samples": len(self.timings),
            "timing_ms": self.timings,
            "status_codes": self.status_codes,
            "findings": [f.as_dict() for f in self.findings]
        }





# ==========================================================
# FASTAPI APP
# ==========================================================

app = FastAPI(title="Observador X-RAY")

@app.post("/api/analyze")
async def analyze(url: str = Form(...)):
    analyzer = XRayAnalyzer(url)
    result = await analyzer.run()

    return JSONResponse({
        "url": result["url"],
        "findings": result["findings"],
        "timeline": [
            {
                "sample": i + 1,
                "status": result["status_codes"][i],
                "time_ms": result["timing_ms"][i]
            }
            for i in range(len(result["timing_ms"]))
        ]
    })


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", response_class=HTMLResponse)
def ui(request: Request):
    
    try:
        # Validación mínima pasiva del objeto request
        if request is None:
            raise RuntimeError("request inválido")

        response = templates.TemplateResponse(
            "index.html",
            {"request": request}
        )

        # --- Hardening de headers ---
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Permissions-Policy"] = (
            "geolocation=(), microphone=(), camera=()"
        )

        # CSP suave: protege sin bloquear estilos/scripts inline existentes
        response.headers["Content-Security-Policy"] = (
            "default-src 'self' 'unsafe-inline' 'unsafe-eval'; "
            "img-src 'self' data:; "
            "style-src 'self' 'unsafe-inline'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval'"
        )

        return response

    except Exception:
        # Fallback silencioso
        return HTMLResponse(
            content="",
            status_code=204
        )