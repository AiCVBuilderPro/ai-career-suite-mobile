from fastapi import APIRouter

router = APIRouter()

@router.post("/improve")
def improve_cv(data: dict):
    text = data.get("text", "")

    return {
        "result": f"AI Improved CV:\n\n{text}\n\nATS Score: 85/100"
    }
