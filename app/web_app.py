from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from .image_processor import process_image
from .storage_manager import UPLOAD_FOLDER, PROCESSED_FOLDER, save_file, get_processed_file_path

# Verifica se o módulo de vídeo pode ser importado
try:
    from .video_processor import process_video, extract_video_frame
    VIDEO_ENABLED = True
except ImportError as e:
    print(f"⚠️ Aviso: Módulo de vídeo desativado - {str(e)}")
    VIDEO_ENABLED = False

app = Flask(__name__)

def start_web_app():
    app.run(host='0.0.0.0', port=5000, debug=False)

@app.route('/')
def index():
    return render_template('index.html', video_enabled=VIDEO_ENABLED)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    operation = request.form.get('operation')
    minute = request.form.get('minute', type=int)
    
    if file.filename == '':
        return redirect(url_for('index'))
    
    try:
        # Salvar arquivo original
        original_path = save_file(file, UPLOAD_FOLDER)
        filename = file.filename
        
        # Processar de acordo com o tipo
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            processed_filename = process_image(original_path, operation)
        elif filename.lower().endswith(('.mp4', '.avi', '.mov')):
            if not VIDEO_ENABLED:
                return "Processamento de vídeo desativado no servidor", 400
            if operation == 'extract_frame':
                processed_filename = extract_video_frame(original_path, minute)
            else:
                processed_filename = process_video(original_path, operation)
        else:
            return "Tipo de arquivo não suportado", 400
        
        return render_template('result.html', 
                              filename=processed_filename,
                              operation=operation)
    
    except Exception as e:
        return f"Erro no processamento: {str(e)}", 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(get_processed_file_path(filename), as_attachment=True)

if __name__ == '__main__':
    start_web_app()