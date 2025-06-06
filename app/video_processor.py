import cv2
import os
import random
from .storage_manager import get_processed_path

def process_video(video_path, operation):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("Não foi possível abrir o vídeo")
    
    filename = os.path.basename(video_path)
    base_name, _ = os.path.splitext(filename)
    
    if operation == 'convert':
        output_name = f"converted_{base_name}.mp4"
        output_path = get_processed_path(output_name)
        
        # Obter as dimensões e FPS do vídeo original
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
        
        cap.release()
        out.release()
        return output_name
    
    raise ValueError("Operação inválida para vídeo")

def extract_video_frame(video_path, minute=None):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("Não foi possível abrir o vídeo")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_seconds = total_frames / fps
    
    # Calcular frame alvo
    if minute is None:
        target_second = random.uniform(0, duration_seconds)
    else:
        target_second = min(float(minute) * 60, duration_seconds)
    
    target_frame = int(target_second * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
    ret, frame = cap.read()
    
    if ret:
        base_name = os.path.basename(video_path)
        name_without_ext = os.path.splitext(base_name)[0]
        output_name = f"frame_{minute or 'random'}_{name_without_ext}.jpg"
        output_path = get_processed_path(output_name)
        cv2.imwrite(output_path, frame)
        return output_name
    
    cap.release()
    raise RuntimeError("Falha ao extrair frame do vídeo")