from database.config import UserModel
from database.config.engine import SessionLocal
from modules.hashing.hashing import hash_password
from uuid import UUID

"""
This is where functions for the user table are defined.
Please use descriptive function names as seen.
"""

def create_user(username: str, password: str, email: str):
    session = SessionLocal()
    hashed_password = hash_password(password=password)
    new_user = UserModel(username=username, password=hashed_password, email=email)                                                          
    session.add(new_user)
    try:
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        session.rollback()
        print(f"Failed to add to DB: {e}")
        return None
    finally:
        session.close()


def update_user(
    id: UUID,
    username: str | None,
    email: str | None,
    password: str | None,
    first_name: str | None,
    last_name: str | None
    ):
    session = SessionLocal()
    try:
        user = session.query(UserModel).filter_by(id=id).first()
        if user is None:
            print(f"User with id {id} not found.")
            return False

        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = hash_password(password)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name

        session.commit()
        session.refresh(user)
        print(f"User with id {id} updated successfully.")
        return user

    except Exception as e:
        session.rollback()
        print(f"Error updating user: {e}")
        return False
    finally:
        session.close()


def get_user_by_id(unique_id: UUID):
    session = SessionLocal()
    try:
        return session.query(UserModel).filter_by(id=unique_id).first()
    finally:
        session.close()


def get_user_by_email(email: str):
    session = SessionLocal()
    try:
        return session.query(UserModel).filter_by(email=email).first()
    finally:
        session.close()


def get_user_by_username(username: str):
    session = SessionLocal()
    try:
        return session.query(UserModel).filter_by(username=username).first()
    finally:
        session.close()


def delete_user(unique_id: UUID):
    session = SessionLocal()
    try:
        user = session.query(UserModel).filter_by(id=unique_id).first()
        if user is None:
            print(f"User with id {unique_id} not found.")
            return False

        session.delete(user)
        session.commit()
        print(f"User with id {unique_id} deleted successfully.")
        return True

    except Exception as e:
        session.rollback()
        print(f"Failed to remove from DB: {e}")
        return False
    finally:
        session.close()
