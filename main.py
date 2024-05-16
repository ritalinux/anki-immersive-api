from v1.app import app_v1

from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.include_router(app_v1)

@app.get('/')
def home():
    return {'hello': 'world'}

if __name__ == '__main__':
    uvicorn.run(app)



