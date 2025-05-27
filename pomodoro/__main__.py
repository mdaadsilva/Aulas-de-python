"""Ponto de entrada do aplicativo Pomodoro"""
from .timer import PomodoroTimer

def main():
    """Função principal do aplicativo"""
    timer = PomodoroTimer()
    try:
        timer.iniciar()
    except KeyboardInterrupt:
        print("\nAplicativo encerrado pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {str(e)}")
    finally:
        timer.pausar()

if __name__ == "__main__":
    main() 