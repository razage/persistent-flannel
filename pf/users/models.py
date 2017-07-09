from datetime import datetime
from enum import Enum, IntEnum

from sqlalchemy_utils import ChoiceType, EmailType, PasswordType

from pf import db
from pf.models import BaseModel


class UserStatus(Enum):
    INACTIVE = 0
    ACTIVE = 1
    BANNED = 2


class UserLevel(IntEnum):
    STANDARD = 0
    MOD = 1
    ADMIN = 2
    SUPERADMIN = 3


class User(BaseModel):
    __tablename__ = "users"

    email = db.Column(EmailType(length=255), unique=True, nullable=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(PasswordType(max_length=255, schemes=['argon2']))
    status = db.Column(ChoiceType(UserStatus, impl=db.Integer))
    level = db.Column(ChoiceType(UserLevel, impl=db.Integer))
    created_time = db.Column(db.DateTime(timezone=False), default=datetime.utcnow)
    last_login_date = db.Column(db.DateTime(timezone=False), default=None, nullable=True)

    def __init__(self, username, password, email=None):
        self.username = username
        self.password_hash = password
        self.email = email
        self.status = UserStatus.ACTIVE  # if I add email verification later, this will change.
        self.level = UserLevel.STANDARD

    @classmethod
    def by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user

    @property
    def is_mod(self):
        return self.level >= UserLevel.MOD

    @property
    def is_admin(self):
        return self.level >= UserLevel.ADMIN
