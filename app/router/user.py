from bson.objectid import ObjectId
from fastapi import APIRouter, Depends

from app.database import User
from app.serializers.userserializers import user_response_entity

from .. import oauth2, schemas

router = APIRouter()


@router.get("/me", response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = user_response_entity(User.find_one({"_id": ObjectId(str(user_id))}))
    return {"status": "success", "user": user}
