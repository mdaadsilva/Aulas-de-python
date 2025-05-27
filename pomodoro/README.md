# Aplicativo Pomodoro

Um aplicativo de linha de comando para gerenciamento de tempo usando a Técnica Pomodoro.

## Funcionalidades

- Timer para ciclos de trabalho (25 minutos)
- Pausas curtas (5 minutos)
- Pausas longas (15 minutos) a cada 4 ciclos
- Interface limpa e intuitiva
- Contagem regressiva em tempo real
- Mensagens motivacionais
- Possibilidade de encerrar a qualquer momento

## Como Usar

1. Instale o Python 3.6 ou superior
2. Execute o programa:
```bash
python -m pomodoro
```

## Estrutura do Projeto

```
pomodoro/
├── __init__.py      # Inicialização do pacote
├── __main__.py      # Ponto de entrada
├── timer.py         # Classe principal do timer
└── constants.py     # Constantes do sistema
```

## Comandos

- `Enter`: Inicia um novo ciclo
- `s`: Sai do aplicativo
- `Ctrl+C`: Interrompe o aplicativo a qualquer momento

## Sobre a Técnica Pomodoro

A Técnica Pomodoro é um método de gerenciamento de tempo desenvolvido por Francesco Cirillo no final dos anos 1980. O método usa um cronômetro para dividir o trabalho em intervalos, tradicionalmente de 25 minutos de duração, separados por pausas curtas. 