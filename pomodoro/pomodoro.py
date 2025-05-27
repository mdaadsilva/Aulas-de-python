import time
import os

# --- Configurações do Pomodoro ---
# Tempo de trabalho em segundos (25 minutos)
WORK_TIME = 25 * 60
# Tempo de pausa curta em segundos (5 minutos)
SHORT_BREAK_TIME = 5 * 60
# Tempo de pausa longa em segundos (15 minutos)
LONG_BREAK_TIME = 15 * 60
# Número de ciclos de trabalho antes de uma pausa longa
POMODORO_CYCLES_BEFORE_LONG_BREAK = 4

# --- Funções Auxiliares ---

def clear_console():
    """Limpa o console para uma exibição mais limpa."""
    # Para sistemas Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para sistemas Unix (Linux, macOS)
    else:
        _ = os.system('clear')

def format_time(seconds):
    """Formata o tempo em segundos para 'MM:SS'."""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"

def countdown(total_seconds, message):
    """
    Executa um contador regressivo e exibe o tempo restante no console.
    
    Args:
        total_seconds (int): O número total de segundos para a contagem regressiva.
        message (str): A mensagem a ser exibida acima do contador.
    """
    for remaining_time in range(total_seconds, -1, -1):
        clear_console()
        print("--- Aplicativo Pomodoro ---")
        print(f"\n{message}")
        print(f"Tempo restante: {format_time(remaining_time)}")
        time.sleep(1)
    
    clear_console()
    print("--- Aplicativo Pomodoro ---")
    print(f"\n{message}")
    print("Tempo restante: 00:00")
    print("\n--- Tempo Esgotado! ---")
    # Pequena pausa para o usuário ver a mensagem final
    time.sleep(3)

def pomodoro_app():
    """Função principal do aplicativo Pomodoro."""
    pomodoro_count = 0
    
    print("Bem-vindo ao Aplicativo Pomodoro!")
    print(f"Trabalho: {format_time(WORK_TIME)}")
    print(f"Pausa Curta: {format_time(SHORT_BREAK_TIME)}")
    print(f"Pausa Longa: {format_time(LONG_BREAK_TIME)} (a cada {POMODORO_CYCLES_BEFORE_LONG_BREAK} ciclos)\n")
    
    input("Pressione Enter para iniciar o primeiro ciclo de trabalho...")
    
    while True:
        pomodoro_count += 1
        print(f"\n--- Ciclo Pomodoro #{pomodoro_count} ---")
        
        # --- Ciclo de Trabalho ---
        countdown(WORK_TIME, "Foco no Trabalho!")
        print("\nÓtimo trabalho! Hora da pausa.")
        
        # --- Ciclo de Pausa ---
        if pomodoro_count % POMODORO_CYCLES_BEFORE_LONG_BREAK == 0:
            # Pausa longa
            countdown(LONG_BREAK_TIME, "Pausa Longa! Relaxe e recarregue.")
            print("\nFim da pausa longa. Pronto para mais ciclos!")
        else:
            # Pausa curta
            countdown(SHORT_BREAK_TIME, "Pausa Curta! Estique as pernas.")
            print("\nFim da pausa curta. De volta ao trabalho!")
            
        # Opção para continuar ou sair
        choice = input("\nPressione Enter para o próximo ciclo, ou 's' para sair: ").lower()
        if choice == 's':
            print("\nObrigado por usar o Aplicativo Pomodoro. Até a próxima!")
            break

# --- Execução do Aplicativo ---
if __name__ == "__main__":
    pomodoro_app()
