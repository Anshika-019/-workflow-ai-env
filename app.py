from fastapi import FastAPI
import threading
import time

from inference import run

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

def start():
    time.sleep(2)
    run()

# background run
threading.Thread(target=start).start()