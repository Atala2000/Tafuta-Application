# config.py
import uuid
import os
import dotenv

dotenv.load_dotenv()

# Configuration variables for the blueprint
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
USERS_ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
JWT_SECRET_KEY = str(uuid.uuid4())
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@localhost:33061/test"
