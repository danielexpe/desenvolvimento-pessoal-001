from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, objetivos, personagens, pontos_fortes, habilidades, atividades
from app.database.session import engine
from app.models import base

# Create all tables
base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Apoio ao Foco em Objetivos Pessoais",
    description="API para gerenciar objetivos pessoais com personagens inspiradores e habilidades",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(objetivos.router, prefix="/objetivos", tags=["objetivos"])
app.include_router(personagens.router, tags=["personagens"])
app.include_router(pontos_fortes.router, tags=["pontos_fortes"])
app.include_router(habilidades.router, tags=["habilidades"])
app.include_router(atividades.router, tags=["atividades"])

@app.get("/", tags=["root"])
async def read_root():
    return {
        "message": "Bem-vindo ao Sistema de Apoio ao Foco em Objetivos Pessoais",
        "api_version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}