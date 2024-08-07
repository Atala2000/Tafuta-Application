# config.py
import uuid
import os
import dotenv
import datetime

dotenv.load_dotenv()

# Configuration variables for the blueprint
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
USERS_ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=1)
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@localhost:33061/test"
