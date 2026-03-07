from fastapi import FastAPI
from routers.principal_router import router
from routers.perfil_router import router_user



app = FastAPI()

app.include_router(router)
app.include_router(router_user)

