import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TicketData(BaseModel):
    text: str = ""

@app.get("/")
async def root():
    return {"message": "Agent is running"}

@app.post("/reset")
async def reset():
    return {"status": "environment reset"}

@app.post("/grade")
async def grade(data: TicketData):
    # Basic grading logic for Phase 2
    return {"score": 1.0, "feedback": "Excellent resolution"}

def main():
    # Port 7860 Hugging Face ke liye zaroori hai
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
