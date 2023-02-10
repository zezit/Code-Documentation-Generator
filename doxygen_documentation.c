

/**
 * @brief Função para adicionar dois números
 * 
 * Esta função recebe dois números inteiros como entrada e retorna a soma deles.
 * 
 * @param a Primeiro número inteiro
 * @param b Segundo número inteiro
 * 
 * @return A soma dos parâmetros a e b
 */
int add(int a, int b) { // Recebe dois inteiros a e b e devolve a soma entre eles
    return a + b;
}




/**
 * @brief   Função para realizar a subtração de 2 inteiros
 * 
 * A função realiza o cálculo 'a - b' e retorna o resultado
 * 
 * @param a   Primeiro número para realizar a operação (int)
 * @param b   Segundo número para realizar a operação (int) 
 * 
 * @return  O resultado da operação 'a - b' (int)
 */
int subtract(int a, int b) {
    return a - b;
}



/**
 * Esta função faz duas chamadas para outras duas funções, add() e subtract().
 *
 * @param int a Primeiro número.
 * @param int b Segundo número.
 * @return O resultado da soma e subtração.
 */ 
int main() {
    int a = 10, b = 5;
    printf("%d + %d = %d\n", a, b, add(a, b)); // Chama a função de soma
    printf("%d - %d = %d\n", a, b, subtract(a, b)); // Chama a função de subtração
    return 0;
}