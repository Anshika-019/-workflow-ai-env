from fastapi import FastAPI
import threading
import time

from env.workflow_env import WorkflowEnv
from inference import run

app = FastAPI()
env = WorkflowEnv()

@app.get("/")
def home():
    return {"status": "running"}

def start():
    time.sleep(2)
    run()

@app.post("/reset")
def reset():
    env = WorkflowEnv()
    obs = env.reset()
    return obs.model_dump()

def main():
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)