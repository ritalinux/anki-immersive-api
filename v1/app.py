from fastapi import FastAPI
from fastapi_utils import Api

def create_app():
    app = FastAPI()
    api = Api(app)

    myapi = MyApi()
    api.add_resource(myapi, "/uri", )

    @app.get('/')
    def home():
        return {'hello': 'world'}

    return app