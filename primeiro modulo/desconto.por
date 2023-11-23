programa {

  funcao inicio() {

    // Declaração das variáveis

    real produto
    real desconto
    real final

    // Valor do produto

    escreva("Digite o valor do produto por favor: ")
    leia(produto)

    // Desconto (10% do produto)
  
    desconto = produto * 0.10

    // Valor final com o desconto

    final = produto - desconto

    // Resultado

    escreva("O valor final do produto com o desconto é de: ", final)
  }
}