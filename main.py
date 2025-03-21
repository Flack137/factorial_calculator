from typing import Union
from fastapi import FastAPI, Body, HTTPException, Depends
from pydantic import BaseModel, constr, conint
from typing import List, Dict
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Path, HTTPException, Query, Body, Depends, Form
from pydantic import BaseModel, ValidationError
from typing import List, Annotated, Optional
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

