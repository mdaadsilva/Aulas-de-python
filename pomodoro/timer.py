"""Classe principal do Timer Pomodoro"""
import time
import os
from typing import Callable
from .constants import (
    TEMPO_TRABALHO, TEMPO_PAUSA_CURTA, TEMPO_PAUSA_LONGA,
    CICLOS_ANTES_PAUSA_LONGA, MENSAGENS, TITULO, SEPARADOR
)

class PomodoroTimer:
    def __init__(self):
        """Inicializa o timer Pomodoro"""
        self.ciclos_completados = 0
        self.pausado = False

    def limpar_console(self) -> None:
        """Limpa o console para uma exibição mais limpa."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def formatar_tempo(self, segundos: int) -> str:
        """
        Formata o tempo em segundos para 'MM:SS'.
        
        Args:
            segundos: Tempo em segundos
            
        Returns:
            String formatada no padrão MM:SS
        """
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        return f"{minutos:02d}:{segundos_restantes:02d}"

    def contagem_regressiva(self, total_segundos: int, mensagem: str) -> None:
        """
        Executa uma contagem regressiva exibindo o tempo restante.
        
        Args:
            total_segundos: Duração total em segundos
            mensagem: Mensagem a ser exibida durante a contagem
        """
        for tempo_restante in range(total_segundos, -1, -1):
            if self.pausado:
                return
                
            self.limpar_console()
            print(TITULO)
            print(f"\n{mensagem}")
            print(f"Tempo restante: {self.formatar_tempo(tempo_restante)}")
            time.sleep(1)
        
        self.limpar_console()
        print(TITULO)
        print(f"\n{mensagem}")
        print("Tempo restante: 00:00")
        print("\n--- Tempo Esgotado! ---")
        time.sleep(3)

    def executar_ciclo_trabalho(self) -> None:
        """Executa um ciclo de trabalho"""
        self.ciclos_completados += 1
        print(f"\n--- Ciclo Pomodoro #{self.ciclos_completados} ---")
        self.contagem_regressiva(TEMPO_TRABALHO, MENSAGENS["trabalho"])
        print("\nÓtimo trabalho! Hora da pausa.")

    def executar_pausa(self) -> None:
        """Executa uma pausa (curta ou longa)"""
        if self.ciclos_completados % CICLOS_ANTES_PAUSA_LONGA == 0:
            # Pausa longa
            self.contagem_regressiva(TEMPO_PAUSA_LONGA, MENSAGENS["pausa_longa"])
            print(MENSAGENS["fim_pausa_longa"])
        else:
            # Pausa curta
            self.contagem_regressiva(TEMPO_PAUSA_CURTA, MENSAGENS["pausa_curta"])
            print(MENSAGENS["fim_pausa_curta"])

    def iniciar(self) -> None:
        """Inicia o timer Pomodoro"""
        print(MENSAGENS["boas_vindas"])
        print(f"Trabalho: {self.formatar_tempo(TEMPO_TRABALHO)}")
        print(f"Pausa Curta: {self.formatar_tempo(TEMPO_PAUSA_CURTA)}")
        print(f"Pausa Longa: {self.formatar_tempo(TEMPO_PAUSA_LONGA)} (a cada {CICLOS_ANTES_PAUSA_LONGA} ciclos)\n")
        
        input(MENSAGENS["inicio"])
        
        while not self.pausado:
            self.executar_ciclo_trabalho()
            if self.pausado:
                break
                
            self.executar_pausa()
            if self.pausado:
                break
                
            escolha = input(MENSAGENS["proximo_ciclo"]).lower()
            if escolha == 's':
                print(f"\n{MENSAGENS['despedida']}")
                break

    def pausar(self) -> None:
        """Pausa o timer"""
        self.pausado = True 