from hashids import Hashids
import environ

env = environ.Env()
environ.Env.read_env()


def get_hashid_instance():
    salt = env('SALT')  # Substitua com seu próprio sal secreto
    min_length = 14  # Defina o comprimento mínimo para os hashes
    return Hashids(salt=salt, min_length=min_length)

def encode_id(pk):
    hashids = get_hashid_instance()
    return hashids.encode(pk)

def decode_id(hashid):
    hashids = get_hashid_instance()
    decoded_data = hashids.decode(hashid)
    return decoded_data[0] if decoded_data else None

# Exemplo de uso

