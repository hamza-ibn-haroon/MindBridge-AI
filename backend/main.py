from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.mood_router import router as mood_router
from api.insights import router as insights_router
from api.recommendations_router import router as recommendations_router
from api.health import router as health_router


app = FastAPI(
    title="MindBridge API",
    description="Intent-based conversational support backend",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(
    health_router,
    prefix="/api/health",
    tags=["Health"],
)

app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"],
)

app.include_router(
    mood_router,
    prefix="/api/mood",
    tags=["Mood Analysis"],
)

app.include_router(
    insights_router,
    prefix="/api/insights",
    tags=["Insights"],
)

app.include_router(
    recommendations_router,
    prefix="/api/recommendations",
    tags=["Recommendations"],
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
async def root():

    return {
        "success": True,
        "message": "MindBridge API is running",
        "version": "1.0.0",
        "llm": False,
        "database": False,
        "status": "online",
    }


# ============================================================
# API INFORMATION
# ============================================================

@app.get("/api")
async def api_info():

    return {
        "service": "MindBridge API",
        "version": "1.0.0",
        "status": "online",
        "endpoints": {
            "health": "/api/health/",
            "chat": "/api/chat/message",
            "mood": "/api/mood/analyze",
            "insights": "/api/insights/analyze",
            "recommendations": "/api/recommendations/get",
            "docs": "/docs",
        }
    }