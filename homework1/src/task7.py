import bcrypt

def hash_password(password: str) -> bytes:
    if not isinstance(password, str):
        raise TypeError("ERROR: Password must be a string!")
    if len(password) < 8:
        raise ValueError("ERROR: Password must be at least 8 characters!")
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def main():
    password="IM_A_PASSWORD!"
    print(f"BYCRYPT HASHED PASSWORD: {hash_password(password)}")

if __name__ == "__main__":
    main()