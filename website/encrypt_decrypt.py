from django.core import signing

def encrypt_id(pk):
    return signing.dumps(pk)

def decrypt_id(encrypted_pk):
    return signing.loads(encrypted_pk)