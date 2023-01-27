'''
utility modules, classes, functions,
methods, variables etc
'''

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_passwd(password: str):
    """ hash a password"""
    return pwd_context.hash(password)