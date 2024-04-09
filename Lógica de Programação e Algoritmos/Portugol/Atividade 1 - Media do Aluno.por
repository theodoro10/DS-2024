programa
{
	
 funcao inicio(){
 real numero_1, numero_2, numero_3, numero_divisor, media
 

 escreva( "Digite o primeiro numero: ")
  leia(numero_1)

 
  escreva("Digite o segundo numero: ")
   leia(numero_2)

   
   escreva("Digite o terceiro numero: ")
   leia(numero_3)

   escreva("Digite o numero divisor: ")
   leia(numero_divisor)


   media = numero_1 + numero_2 + numero_3 
   media = media / numero_divisor 

   escreva("A soma dos números é: ", media)

  		se(media >= 7) {
  			escreva("\n Aluno Aprovado com Sucessol!")
 		}senao se(media >3) {
  			  escreva("\nAluno devera fazer Recuperação")
  		} senao{
  		escreva("Aluno reprovado :( ")
  }

   
	
   }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 8; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */