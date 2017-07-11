from marshmallow_enum import EnumField

from pf import ma
from .models import User, UserLevel, UserStatus


class UserSchema(ma.ModelSchema):
    class Meta:
        table = User
        fields = ("id", "email", "username", "status", "level", "created_time", "last_login_date")

    status = EnumField(UserStatus)
    level = EnumField(UserLevel)
