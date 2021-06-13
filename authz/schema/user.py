from authz import ma
from authz.model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)  ##khundani##
    username = ma.auto_field()  ##ham bekhune ham benevise##
    password = ma.auto_field(load_only=True)  ##khoruji ndre ke | faqat minevise##
    role = ma.auto_field()
    register_at = ma.auto_field(dump_only=True)
    last_active_at = ma.auto_field(dump_only=True)
    last_failed_at = ma.auto_field(dump_only=True)
    status = ma.auto_field()
