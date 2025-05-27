"""Constantes utilizadas no aplicativo Pomodoro"""

# Tempos em segundos
TEMPO_TRABALHO = 25 * 60  # 25 minutos
TEMPO_PAUSA_CURTA = 5 * 60  # 5 minutos
TEMPO_PAUSA_LONGA = 15 * 60  # 15 minutos

# Configurações do ciclo
CICLOS_ANTES_PAUSA_LONGA = 4

# Mensagens do sistema
MENSAGENS = {
    "trabalho": "Foco no Trabalho!",
    "pausa_curta": "Pausa Curta! Estique as pernas.",
    "pausa_longa": "Pausa Longa! Relaxe e recarregue.",
    "fim_pausa_curta": "Fim da pausa curta. De volta ao trabalho!",
    "fim_pausa_longa": "Fim da pausa longa. Pronto para mais ciclos!",
    "boas_vindas": "Bem-vindo ao Aplicativo Pomodoro!",
    "inicio": "Pressione Enter para iniciar o primeiro ciclo de trabalho...",
    "proximo_ciclo": "Pressione Enter para o próximo ciclo, ou 's' para sair: ",
    "despedida": "Obrigado por usar o Aplicativo Pomodoro. Até a próxima!"
}

# Formatação
TITULO = "--- Aplicativo Pomodoro ---"
SEPARADOR = "-" * len(TITULO) 