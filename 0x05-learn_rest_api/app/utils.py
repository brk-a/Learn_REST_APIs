'''
utility modules, classes, functions,
methods, variables etc
'''

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_passwd(password: str):
    """ hash a password"""
    return pwd_context.hash(password)

def verify(plain_passwd, hashed_passwd):
    """ compare hashes during JWT auth"""
    return pwd_context.verify(plain_passwd, hashed_passwd)