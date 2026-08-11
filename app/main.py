from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title='My Tasks Backend')
    return app

app = create_app()

@app.get("/")
def ping():
    return {"msg" : "pong"}