from main import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    # feilds to expose
    class Meta: 
        ordered = True
        fields = ('id', 
                  'name', 
                  'email', 
                  'password', # for loading incoming passwords only
                  'password_hash',
                  'role', # for loading incoming role names only
                  'user_role',
                  'created_tickets',
                  'assigned_tickets', 
                  'created_comments' )
        load_only = ('password', 'role')
    
    # relations
    password = fields.String()
    
    user_role = fields.Nested('RoleSchema', only=['role_name'])

    created_tickets  = fields.List(fields.Nested('TicketSchema', 
                                                 exclude=['created_by_user'] ))
    
    assigned_tickets = fields.List(fields.Nested('TicketSchema', 
                                                 exclude=['assigned_to_user']))
    
    created_comments = fields.List(fields.Nested('CommentSchema', 
                                                 exclude=['user']))
    # for hiding feilds contextualy 
    # @post_dump(pass_many=True)

user_schema  = UserSchema(exclude=['password_hash'])
users_schema = UserSchema(many=True, exclude=['password_hash'   ])


    