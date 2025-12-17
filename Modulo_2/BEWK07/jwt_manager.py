import jwt
from cryptography.hazmat.primitives import serialization

class JWTManagerRSA:
    def __init__(self, private_key_path='private_key.pem', 
                public_key_path='public_key.pem', algorithm='RS256'):
        self.algorithm = algorithm
        
        # load private key
        with open(private_key_path, 'rb') as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None  
            )
        
        # Load Public Key 
        with open(public_key_path, 'rb') as f:
            self.public_key = serialization.load_pem_public_key(f.read())
    
    def encode(self, data):
        try:
            encoded = jwt.encode(
                payload=data, 
                key=self.private_key,
                algorithm=self.algorithm
            )
            return encoded
        except Exception as e:
            print(f"[JWT RSA] Encode error: {e}")
            return None
    
    def decode(self, token):
        try:
            decoded = jwt.decode(
                jwt=token,
                key=self.public_key,
                algorithms=[self.algorithm]
            )
            return decoded
        except jwt.ExpiredSignatureError:
            print("[JWT RSA] Token expirado")
            return None
        except jwt.InvalidTokenError as e:
            print(f"[JWT RSA] Token inválido: {e}")
            return None
        except Exception as e:
            print(f"[JWT RSA] Decode error: {type(e).__name__}: {e}")
            return None