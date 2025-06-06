from PIL import Image
import os
from .storage_manager import get_processed_path

def process_image(image_path, operation):
    img = Image.open(image_path)
    filename = os.path.basename(image_path)
    processed_filename = ""
    
    if operation == 'grayscale':
        img = img.convert('L')
        processed_filename = f"gray_{filename}"
    elif operation == 'resize':
        # Redimensionar mantendo a proporção
        base_size = 300
        width_percent = (base_size / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((base_size, height_size), Image.Resampling.LANCZOS)
        processed_filename = f"resized_{filename}"
    else:
        raise ValueError("Operação inválida para imagem")
    
    output_path = get_processed_path(processed_filename)
    img.save(output_path)
    return processed_filename