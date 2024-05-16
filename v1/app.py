from v1.services.polyglot_services import router as polyglot_router

from fastapi import APIRouter


app_v1 = APIRouter(prefix='/v1')
app_v1.include_router(polyglot_router)
