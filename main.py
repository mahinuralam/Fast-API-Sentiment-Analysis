from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session, sessionmaker

import models
import schemas
from database import Base, engine
from utils import is_sentence, sentiment_analysis

Base.metadata.create_all(engine)

app = FastAPI()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        

@app.get('/')
def root():
    return "This is the Python and ML Task"

# The method take a sentence as input and anaylsis it then stores sentiment of the sentence along with the sentence.
@app.post('/analyze', response_model=schemas.Analyze, status_code=status.HTTP_201_CREATED)
def create_analyze(analyze: schemas.AnalyzeCreate, session: Session = Depends(get_session)):
    
    if not is_sentence(analyze.text):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Input text is not a valid sentence.")
    
    analyze = models.Analyze(text = analyze.text)
    analyze.sentiment = sentiment_analysis(analyze.text)
    session.add(analyze)
    session.commit()
    session.refresh(analyze)
    session.close()
    
    return analyze


@app.get('/analyze/{id}', response_model=schemas.Analyze)
def get_analyze(id: int, session: Session = Depends(get_session)):
    analyze = session.query(models.Analyze).get(id)
    session.close()
    
    if not analyze:
        raise HTTPException(status=404, detail=f"Analyze item with id {id} does not Exist")
    
    return analyze


@app.put('/analyze/{id}', response_model=schemas.Analyze)
def update_analyze(id: int, analyze: schemas.AnalyzeCreate, session: Session = Depends(get_session)):
    get_db_data = session.query(models.Analyze).get(id)
    
    if get_db_data:
        get_db_data.text = analyze.text
        get_db_data.sentiment = sentiment_analysis(analyze.text)
        session.commit()
        
    session.close()
    
    if not get_db_data:
        raise HTTPException(status=404, detail=f"Analyze item with id {id} does not Exist")
    
    return get_db_data


@app.delete('/analyze/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_analyze(id: int, session: Session = Depends(get_session)):
    analyze = session.query(models.Analyze).get(id)
    
    if analyze:
        session.delete(analyze)
        session.commit()
    session.close()
    
    if not analyze:
        raise HTTPException(status=404, detail=f"Analyze item with id {id} does not Exist")
    
    return None


@app.get('/analyze', response_model = List[schemas.Analyze])
def read_analyze_list(session: Session = Depends(get_session)):
    analyze_list = session.query(models.Analyze).all()
    session.close()
    return analyze_list
