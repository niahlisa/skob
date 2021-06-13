from flask import abort, request

from authz import db
from authz.model import User
from authz.schema import UserSchema


class UserController:
    def create_user():
        if request.content_type != "application/json":
            abort(415)
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())  # validate request data.
        except:
            abort(400)
        if not data["username"] or not data["password"]:
            abort(400)

        user = User.query.filter_by(username=data["username"]).first()
        if user is not None:
            abort(409)
        user = User(username=data["username"], password=data["password"])
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return {"user": user_schema.dump(user)}, 201

    def get_users():
        pass

    def get_user(user_id):
        pass

    def update_user(user_id):
        pass

    def delete_user(user_id):
        pass
