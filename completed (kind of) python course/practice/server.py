# FastAPI Server
import base64
import hmac
import hashlib
import json

from typing import Optional

from fastapi import FastAPI, Form, Cookie, Body
from fastapi.responses import Response

app = FastAPI()

SECRET_KEY = "e99d3d45c8b2d720777e18d63914b2aeb3e77afe4ed0b2b13225d03d32fe0caa"
PASSWORD_SALT = "6fb66a06df9a374b241b633fbe4ebdbb7c84010fc7feb4c5926752be9aa8fbf6"

def sign_data(data: str) -> str:
    """Returns signed data"""
    return hmac.new(
        SECRET_KEY.encode(),
        msg=data.encode(),
        digestmod=hashlib.sha256
    ).hexdigest().upper()

def get_username_from_signed_string(username_signed: str) -> Optional[str]:
    username_base64, sign = username_signed.split(".")
    username = base64.b64decode(username_base64.encode()).decode()
    valid_sign = sign_data(username)
    if hmac.compare_digest(valid_sign, sign):
        return username


def verify_password(username: str,password: str) -> bool:
    password_hash = hashlib.sha256( (password + PASSWORD_SALT).encode())\
        .hexdigest().lower()
    stored_password_hash = users[username]["password"]
    return password_hash == stored_password_hash
users = {
    "theoprinzfonharscheich@hotmail.com": {
        "name": "Theo",
        "password": "5136bad06a892b37164db45c9f2090ccbff84e3674ed8cf47259ba85eec68dc5",
        "balance": 123_456
    },

    "man0'the_sea@gmail.com": {
        "name": "Argo",
        "password": "a0e7883d0952cb6a96426d390be317029d52f1fe50f035d0a793bb4af9f3fac2",
        "balance": 987_654
    }
}


@app.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open('templates/login.html', 'r') as f:
        login_page = f.read()
    if not username:
        return Response(login_page, media_type="text/html")
    valid_username = get_username_from_signed_string(username)
    if not valid_username:
        response = Response(login_page, media_type="text/html")
        response.delete_cookie(key="username")
        return response
    try:
        user = users[valid_username]
    except KeyError:
        response = Response(login_page, media_type="text/html")
        response.delete_cookie(key="username")
        return response
    return Response(
        f"Hi {users[valid_username]['name']}!<br />"
        f"You have {users[valid_username]['balance']} on your balance.",
        media_type="text/html")

@app.post("/login")
def process_login_page(data: dict = Body(...)):
    username = data["username"]
    password = data["password"]
    print(username,password)
    user = users.get(username)
    if not user or not verify_password(username, password):
        return Response(
            json.dumps({
                "success": False,
                "message": "Oops! Seems like I don't know you."
            }),
             media_type="application/json")
    
    response = Response(
        json.dumps({
            "success": True,
            "message": f"Welcome, {user['name']}!<br />You have {user['balance']} on your balance." 
        }), 
    media_type="application/json")

    username_signed = base64.b64encode(username.encode()).decode() + "." + \
        sign_data(username)
    response.set_cookie(key="username", value=username_signed)
    return response
