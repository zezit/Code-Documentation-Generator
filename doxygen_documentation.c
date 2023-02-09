

/** 
 * @brief add two ints
 * 
 * Esta função adiciona dois inteiros e retorna o resultado.
 * 
 * @param a Primeiro inteiro a ser adicionado
 * @param b Segundo inteiro a ser adicionado
 * 
 * @return A soma dos dois inteiros
 */
int add(int a, int b){
    return a + b;
}


/*!
 * \brief Subtrai dois inteiros
 * 
 * Esta função subtrai dois inteiros e retorna o resultado.
 * 
 * \param a Primeiro inteiro
 * \param b Segundo inteiro
 * 
 * \return Resultado da subtração
 */
int subtract(int a, int b)
{
    return a - b;
}


/** 
 * @brief Esta função executa a adição e a subtração de dois números inteiros
 * 
 * Esta função recebe dois inteiros, a e b, e imprime a soma e a diferença deles no console.
 * 
 * @param a Primeiro inteiro
 * @param b Segundo inteiro
 * 
 * @return 0
 */
int main()
{
    int a = 10, b = 5;
    printf("%d + %d = %d\n", a, b, add(a, b));
    printf("%d - %d = %d\n", a, b, subtract(a, b));
    return 0;
}