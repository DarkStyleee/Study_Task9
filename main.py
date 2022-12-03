from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from db import get_db
from sqlalchemy.orm import Session

from models import TableCounter
import uvicorn


name = "Ussaev Felix"
app = FastAPI()


@app.get("/")
async def root(db: Session = Depends(get_db)): 
    return { "counter": db.query(TableCounter.id).order_by(TableCounter.id.desc()).first() }


@app.get("/stat")
async def stat(request: Request, db: Session = Depends(get_db)):
    counter = TableCounter(client_info=request.headers["user-agent"])
    db.add(counter)
    db.commit()
    db.refresh(counter)
    return { "counter": db.query(TableCounter.id).order_by(TableCounter.id.desc()).first() }


@app.get("/about")
async def about():
    return HTMLResponse(f"<h3>{ name }</h3>")


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)