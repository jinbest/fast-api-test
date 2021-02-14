#Running Project

python -m venv .venv
source .venv/Scripts/activate
pip install fastapi
pip install uvicorn
uvicorn main:app --reload

