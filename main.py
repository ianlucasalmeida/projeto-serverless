import os
import subprocess
import threading
import time
from app.web_app import start_web_app
from app.storage_manager import setup_directories

def start_docker_services():
    """Inicia os containers Docker"""
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("✅ Serviços Docker iniciados com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao iniciar Docker: {e}")
        print("⚠️ Continuando sem Docker...")
    except FileNotFoundError:
        print("❌ Docker-compose não encontrado. Certifique-se de que o Docker está instalado.")
        print("⚠️ Continuando sem Docker...")

def monitor_system():
    """Monitora a saúde do sistema"""
    while True:
        try:
            # Verificar status dos containers
            docker_ps = subprocess.run(["docker", "ps"], capture_output=True, text=True)
            print("Containers em execução:")
            print(docker_ps.stdout)
            
            # Verificar uso de recursos
            subprocess.run(["docker", "stats", "--no-stream"])
        except Exception as e:
            print(f"⚠️ Erro no monitoramento: {str(e)}")
        
        time.sleep(30)

if __name__ == "__main__":
    print("🛠️ Configurando diretórios...")
    setup_directories()
    
    print("🐳 Iniciando serviços Docker...")
    docker_thread = threading.Thread(target=start_docker_services, daemon=True)
    docker_thread.start()
    # Dando um tempo para o docker iniciar antes do monitoramento
    time.sleep(5)
    
    print("👁️ Iniciando monitoramento do sistema...")
    monitor_thread = threading.Thread(target=monitor_system, daemon=True)
    monitor_thread.start()
    
    print("🚀 Iniciando aplicação web...")
    start_web_app()