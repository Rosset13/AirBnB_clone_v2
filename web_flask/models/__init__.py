from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage = DBStorage()  # Or FileStorage() depending on your setup
storage.reload()

