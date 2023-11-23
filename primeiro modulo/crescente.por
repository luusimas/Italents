programa {

  funcao inicio() {

    // Declaração das variáveis

    inteiro a , b , c
    inteiro auxiliar

   // Inserção de três números

  escreva("Digite o primeiro número: ")
  leia(a)
  escreva("Digite o segundo número: ")
  leia(b)
  escreva("Digite o terceiro número: ")
  leia(c)

  // Ordem crescente

  se (a > b){
   auxiliar = a
   a = b
   b = auxiliar
  }

   se (c < b){
    auxiliar = b
    b = c
    c = auxiliar
   }

    se (b < a){
      auxiliar = a
      a = b
      b = auxiliar
    }
    
  // Resultado
  escreva("Os números ordenados são: " + a, b, c)
  

  }
}