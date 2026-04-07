from fastapi import FastAPI
from env import SupportTicketEnv
from models import Action
from tasks import TaskGrader

app = FastAPI(title="SupportAgent OpenEnv")
env = SupportTicketEnv()
grader = TaskGrader()

@app.post("/reset")
def reset_env():
    return env.reset()

@app.post("/step")
def step_env(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)