from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel
from typing import Annotated
from os import getenv

import phonenumbers as ph
import pwdlib
import db

class AccountManager:
    class RegistrationPayload(BaseModel): 
        phone: Annotated[str, Form()] = "+0 000 000 00 00"
        pin: Annotated[str, Form()] = "0000"

    # phone, 
    def __init__(self):
        self.pwd_hash = pwdlib.PasswordHash.recommended()
        self.router = APIRouter()
        self.router.add_api_route("/api/auth/register", self.register_account, methods=['POST'])
    
    def validate_register(payload: RegistrationPayload):
        if len(payload.pin) < 4: raise HTTPException(400, "Invalid pin format, minimum 4 digits")
        try:
            number_check = ph.parse(payload.phone, "KZ")
            if not ph.is_valid_number(number_check): 
                raise HTTPException(400, "Invalid phone format")
        except ph.NumberParseException: raise HTTPException(400, "Invalid phone format")

    async def register_account(self, payload: RegistrationPayload):
        AccountManager.validate_register(payload)
        
        async with db.SqliteDB(getenv('BANK_DB')) as sql:
            hashed = self.pwd_hash.hash(payload.phone)

    
    async def get_account_data(self):
        pass
