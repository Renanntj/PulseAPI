from fastapi import FastAPI
from routers.principal_router import router
from routers.perfil_router import router_user
from routers.post_router import router_posts
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(router_user)
app.include_router(router_posts)

@app.get("/")
def home():
    return {"status": "PulseAPI online", "v": "1.0.0"}