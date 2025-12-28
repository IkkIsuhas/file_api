from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import get_session, engine
from llm import generate_notes
from model import Note, SQLModel
from schema import chatResponse, chatRequest

app = FastAPI()
SQLModel.metadata.create_all(engine)

@app.post("/notes",response_model=chatResponse)
async def create_note(request:chatRequest,session: Session = Depends(get_session)):
    ai_text = await generate_notes(request.prompt)
    note = Note(prompt=request.prompt,note=ai_text)

    session.add(note)
    session.commit()
    session.refresh(note)

    return note

@app.get("/notes")
def all_notes(session:Session = Depends(get_session)):
    note = session.exec(select(Note)).all()
    return note