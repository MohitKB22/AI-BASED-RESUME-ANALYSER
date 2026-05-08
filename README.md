**AI-Based Resume Analyser**

<div align="center">

> Built with **FastAPI + Groq Llama 3.3 70B + scikit-learn ML** — fully free, no paid APIs required.

The project automates resume screening by combining a trained **TF-IDF + Logistic Regression ML model** for instant skill matching with **Groq's Llama 3.3 70B LLM** for deep analysis. It extracts skills from your resume, compares them against a job description, predicts suitable roles, generates a personalized 4-week learning roadmap, suggests real-world projects to build, rewrites weak resume bullet points for ATS compatibility, and produces tailored interview questions — all in under 30 seconds.

</div>

---

## 📸 What It Does

> Upload resume → Paste job description → Get full AI-powered career dashboard

| Feature | Description |
|---|---|
| 🎯 Match Score | AI-computed % match between your resume and the job description |
| 🧩 Skill Gap | Matched vs missing skills highlighted instantly |
| 📅 4-Week Roadmap | Personalized learning plan to close skill gaps |
| 🚀 Project Ideas | Real-world projects to strengthen your portfolio |
| ✍️ Resume Rewrites | Before/after bullet improvements with ATS optimization |
| 🎤 Interview Prep | Technical, HR, and System Design questions with hints |

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **LLM** | Groq · Llama 3.3 70B | Deep career analysis, roadmap, interview questions |
| **ML** | scikit-learn · TF-IDF + Logistic Regression | Role prediction, match scoring |
| **Backend** | FastAPI · Python 3.11+ | REST API, PDF processing |
| **PDF Parsing** | pdfplumber | Resume text extraction |
| **Frontend** | Vanilla HTML/CSS/JS | Standalone dashboard UI — no Node.js needed |
| **Testing** | pytest · 33 tests | Unit, integration, E2E |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or 3.12 recommended
- Free Groq API key → [console.groq.com](https://console.groq.com)

### 1. Clone the repo
```bash
git clone https://github.com/MohitKB22/AI-BASED-RESUME-ANALYSER.git
cd AI-BASED-RESUME-ANALYSER
```

### 2. Set up backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your Groq API key
Create `backend/.env`:
```
GROQ_API_KEY=gsk_your_key_here
```
Get a free key at [console.groq.com](https://console.groq.com) — no credit card required.

### 4. Train the ML model
```bash
python3 train_model.py
```

### 5. Run tests
```bash
python3 -m pytest tests/test_all.py -v
# Expected: 33 passed
```

### 6. Start the backend
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 7. Open the frontend
```bash
open ../frontend/index.html
```

✅ Backend → `http://localhost:8000`  
✅ API Docs → `http://localhost:8000/docs`  
✅ Frontend → open `frontend/index.html` in Chrome

---

## 🤖 ML Model Details

The system uses a **two-stage analysis pipeline**:

**Stage 1 — ML Pre-Analysis (instant, no API call)**
- TF-IDF vectorizer extracts features from resume + job description
- Cosine similarity computes match score
- Logistic Regression classifier predicts top 3 suitable roles

**Stage 2 — LLM Deep Analysis (Groq Llama 3.3 70B)**
- Generates 4-week personalized learning roadmap
- Suggests 3 real-world portfolio projects
- Rewrites weak resume bullet points with measurable impact
- Creates role-specific interview questions with answer hints

| Metric | Value |
|---|---|
| Algorithm | TF-IDF + Logistic Regression |
| Training Samples | 40 |
| Test Accuracy | 100% |
| CV Accuracy (3-fold) | 77.3% |
| Roles Detected | Backend, Frontend, Data Scientist, DevOps, Data Analyst, Full Stack, Mobile, Cybersecurity |

---

## 🧪 Tests

```bash
cd backend
python3 -m pytest tests/test_all.py -v
```

| Test Suite | Tests | Coverage |
|---|---|---|
| Resume Parser | 5 | PDF extraction, text cleaning |
| ML Matcher | 13 | Skill gap, scoring, role prediction |
| API Routes | 10 | Validation, error handling, edge cases |
| Model Accuracy | 3 | Held-out accuracy, score consistency |
| End-to-End | 2 | Full pipeline with mocked LLM |
| **Total** | **33** | **All passing ✅** |

---

## 🌐 Deployment

### Backend → [Render.com](https://render.com) (Free)
1. Push `backend/` to GitHub
2. New Web Service on Render
3. Build command: `pip install -r requirements.txt && python train_model.py`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add env var: `GROQ_API_KEY`

### Frontend → [Netlify Drop](https://app.netlify.com/drop) (Free, 30 seconds)
1. Update `const API = 'https://your-backend.onrender.com'` in `index.html`
2. Drag `frontend/index.html` to Netlify Drop
3. Done — live URL instantly

---

## 📄 License

Distributed under the AGPL-3.0 License. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">
  <p>If this project helped you, please give it a ⭐ on GitHub!</p>
</div>

