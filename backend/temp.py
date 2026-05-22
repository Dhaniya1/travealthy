from database import engine, server_password

with engine.connect() as conn:
    print("Connected!")
