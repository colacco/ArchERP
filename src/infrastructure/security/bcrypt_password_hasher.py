import bcrypt

from src.application.ports.password_hasher import PasswordHasher

class BcryptPasswordHasher(PasswordHasher):
    def hash(self, plain: str) -> str:
        plain_bytes: bytes = plain.encode("utf-8")
        salt: bytes = bcrypt.gensalt() 
        hashed: bytes = bcrypt.hashpw(plain_bytes, salt)
        
        return hashed.decode("utf-8")

    def verify(self, plain: str, hashed: str) -> bool:
        plain_bytes: bytes = plain.encode("utf-8")
        hashed_bytes: bytes = hashed.encode("utf-8")

        return bcrypt.checkpw(plain_bytes, hashed_bytes)