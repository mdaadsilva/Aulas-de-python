#crie uma calculadora completa

class Calculadora:
    """Classe que implementa operações básicas de uma calculadora."""
    
    @staticmethod
    def soma(x: float, y: float) -> float:
        return x + y
    
    @staticmethod
    def subtracao(x: float, y: float) -> float:
        return x - y
    
    @staticmethod
    def multiplicacao(x: float, y: float) -> float:
        return x * y
    
    @staticmethod
    def divisao(x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Não é possível dividir por zero!")
        return x / y
    
    @staticmethod
    def potencia(x: float, y: float) -> float:
        return x ** y


def obter_numero(mensagem: str) -> float:
    """Função para obter e validar entrada numérica do usuário."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido!")


def exibir_menu() -> None:
    """Exibe o menu de operações disponíveis."""
    print("\n=== Calculadora ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("0. Sair")


def main():
    """Função principal que executa a calculadora."""
    calculadora = Calculadora()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma operação (0-5): ")
        
        if opcao == "0":
            print("Obrigado por usar a calculadora!")
            break
            
        if opcao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida! Tente novamente.")
            continue
            
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
        
        try:
            if opcao == "1":
                resultado = calculadora.soma(num1, num2)
                operacao = "soma"
            elif opcao == "2":
                resultado = calculadora.subtracao(num1, num2)
                operacao = "subtração"
            elif opcao == "3":
                resultado = calculadora.multiplicacao(num1, num2)
                operacao = "multiplicação"
            elif opcao == "4":
                resultado = calculadora.divisao(num1, num2)
                operacao = "divisão"
            else:
                resultado = calculadora.potencia(num1, num2)
                operacao = "potência"
                
            print(f"\nA {operacao} entre {num1} e {num2} é: {resultado}")
            
        except ValueError as erro:
            print(f"Erro: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    main()

