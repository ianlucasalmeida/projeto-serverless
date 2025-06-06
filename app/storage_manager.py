import os

# Caminhos absolutos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'uploads')
PROCESSED_FOLDER = os.path.join(BASE_DIR, '..', 'processed')

def setup_directories():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    print(f"📁 Diretórios configurados: {UPLOAD_FOLDER}, {PROCESSED_FOLDER}")

def save_file(file, directory):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file.filename)
    file.save(file_path)
    return file_path

def get_processed_path(filename):
    return os.path.join(PROCESSED_FOLDER, filename)

def get_processed_file_path(filename):
    return os.path.join(PROCESSED_FOLDER, filename)