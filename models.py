"""
This file defines the database models
"""

from .common import *
from pydal.validators import *
import os
folder=os.path.dirname(__file__)
#auth = Auth(db)
db.define_table('info',
                Field('users_id', db.auth_user, writable=False, readable=False),
                Field('sex', requires=IS_IN_SET(('Male', 'Female'), zero='Choose')),
                Field('dob', 'date'),
                Field('relationship_status', requires=IS_IN_SET(('Single', 'Divorced', 'Widow', 'Widower'), zero='Choose'),),
                Field('seeking', requires=IS_IN_SET(('Marriage', 'Open frienship', 'Love'), zero='Choose'),),
                Field('religion', requires=IS_IN_SET(('Islam','Christainity','Budhism','Eckankar','Jehovah Witness', 'Olumba Olumba Obu'),\
                                        zero='Your Current Belief')),
                Field('locations', label='Location'),
                Field('img', 'upload', uploadfolder='%s/static/members/pics'%folder, label='Profile Pic'),
                Field('bio', 'text'),
                auth.signature)
                
db.define_table('f_request',
                Field('f_member', db.auth_user),
                Field('t_member', db.auth_user),
                Field('status', options=("accepted", "rejected"))
                )
                
db.define_table('f_love',
                 Field('f_member', db.auth_user),
                Field('t_member', db.auth_user),
                )
db.commit()
