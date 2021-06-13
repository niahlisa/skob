from authz import api
from authz.resource.user import UserResource

api.add_resource(UserResource, "/users", method=["GET", "POST"], endpoint="users")

api.add_resource(
    UserResource, "/users/<user_id>", method=["GET", "PATCH", "DELETE"], endpoint="user"
)
