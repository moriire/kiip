"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""
#from py4web include action, redirect, Session, DAL, URL
from contextlib import closing
import shutil
from py4web import *
from yatl.helpers import *
from .common import *
#from py4web.utils.form import  Form
from.import flpays
  


@authenticated.callback()
def like(f_id, t_id):
    db.f_love.insert(f_member=f_id,t_member=t_id)
    
@authenticated.callback()
def m_request(f_id, t_id):
    db.f_request.insert(f_member=f_id,t_member=t_id)
    
@unauthenticated()
@action('index')
@action.uses('index.html')
def index():
    user=auth.get_user()['id']
    if user:
        if not db(db.info.users_id==user).count():
           redirect(URL('complete_profile'))
        else: redirect(URL('home'))
    redirect(URL('index', hash='#'))
    return dict()
    
@authenticated()
@action('info')
@action.uses(auth, 'faq.html')
def complete_profile():
    form=Form(db.info)
    if form.accepted: redirect(URL('home'))
    return dict(form=form)

@authenticated()
@action('home')
@action.uses(auth, 'home.html')
def home():
    members=db(db.auth_user.id==db.info.users_id).select()
    db.info.users_id.default=auth.user_id
    form=Form(db.info)
    userID=auth.get_user()
    return dict(members=members, userID=userID, form=form, like=like)
    
@authenticated()
@action('payment/<userID>')
@action.uses(auth, 'pay.html')
def pay(userID):
    pay=flpays.Transaction('google.com')
    plink=pay.s_charge(1000, email='ibmabdulsalam@gmail.com')
    user=auth.get_user()
    aus=db(db.auth_user.id==userID).select().first()
    return dict(plink=plink, userID=userID, aus=aus, m_request=m_request)
    
    
@authenticated()
@action('wall/<userID>')
@action.uses(auth, 'wall.html')
def wall(userID):
    user=auth.get_user()
    aus=db(db.auth_user.id==userID).select().first()
    #fname = '{username} - {first_name} {last_name}'.format(**user)
    member=db(db.info.users_id==userID).select().first() or redirect(URL('home'))
    return dict(member=member, userID=userID, aus=aus, m_request=m_request)
    
    
@authenticated()
@action('search')
@action.uses(auth, 'home.html')
def search():
    members=db(db.auth_user.id==db.info.users_id).select()
    form=Form(db.info)
    return dict(members=members, form=form)

@authenticated()
@action('status')
@action.uses(auth, 'home.html')
def success():
    members=db(db.auth_user.id==db.info.users_id).select()
    form=Form(db.info)
    return dict(members=members, form=form)
    
from . import app 
@authenticated()
@action('room')
@action.uses(auth, 'room.html')
def chat():
    members=db(db.auth_user.id==db.info.users_id).select()
    form=Form(db.info)
    #main=main()
    return dict(members=members, form=form)
    
