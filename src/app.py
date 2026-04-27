"""
API do Sistema de Gestão da High School

Uma aplicação FastAPI bem simples que permite que estudantes vejam e se inscrevam
em atividades extracurriculares na Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API para visualizar e se inscrever em atividades extracurriculares")

# Monta o diretório de arquivos estáticos
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Banco de dados de atividades em memória
activities = {
    "Chess Club": {
        "description": "Aprenda estratégias e compita em torneios de xadrez",
        "schedule": "Sextas-feiras, 15h30 - 17h00",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Aprenda fundamentos de programação e construa projetos de software",
        "schedule": "Terças e quintas, 15h30 - 16h30",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Educação física e atividades esportivas",
        "schedule": "Segundas, quartas e sextas, 14h00 - 15h00",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
