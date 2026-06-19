Enterfrom fastapi import FastAPI

app = FastAPI(title="AI Career Suite Mobile")

@app.get("/")
def home():
    return {"status": "Backend running 🚀"}

@app.get("/health")
def health():
    return {"ok": True}
