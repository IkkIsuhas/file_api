from sqlmodel import SQLModel, create_engine, Session

url = "postgresql://postgres:Admin@localhost:5432/fastapi"

engine = create_engine(url,echo=True)

def get_session():
    with Session(engine) as session:
        yield session 