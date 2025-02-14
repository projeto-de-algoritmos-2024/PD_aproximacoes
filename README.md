# Aproximações

**Número da Lista**: 26<br>
**Conteúdo da Disciplina**: Programação Dinâmica <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/1008436 | Ryan Augusto Brandão Salles |
| 22/1008481 |   Víctor Moreira Almeida    |

## Sobre 
O projeto visa comparar de forma razoavelmente simples algoritmos de aproximação para
problemas cujo ótimo é obtido por padrões de programação dinâmica.

[link para o relatório no overleaf](https://www.overleaf.com/read/fvdhzpmtybxf#0b1e2b)

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python<br>
### Scripts de teste de função
Basta python para rodar os scripts.

  1. Clone o projeto
  2. Rode os scripts desejados para testagem. Resultados devem diferir em velocidade por razões do hardware, especialmente a CPU.
  3. Se assim desejar, realize um pull para o relatório com os dados da testagem realizada.

### Relatório
Será necessário utilizar um compilador de documentos tex online ou local. Recomenda-se o overleaf

  1. Clone o projeto
  2. Rode o script .tex na pasta doc ou alternativamente carregue no overleaf e compile.

O resultado será um pdf com o relatório.

Alternativamente, basta utilizar o pdf pré-compilado na pasta doc ou entrar no link do projeto!

## Uso 
Esse é um projeto simples. Basta rodar o script na pasta src para obter os dados 
de processamento. O script de testagem de algoritmos funciona utilizando um único número
para gerar os casos de teste, que são listas de itens pseudo-aleatoriamente gerados 
utilizando a biblioteca random.

Para ler sobre os resultados, acesse a pasta doc.

## Outros 

JullietCharlieIndiaIndiaHotelNovember :) - Locvst 

Caso deseje ou julgue necessário, favor sugerir formas de expandir o trabalho.
Ademais, com 1mi itens, o algoritmo ótimo do knapsack quebra ao utilizar demasiada memória. 
O greed permanece intactoe gera resultados factíveis ao longo da execução. Greed is indeed GOOD :>>>

Mas, seriamente, cautela ao utilizar números muito grandes na testagem. Há o risco (mínimo) de causar kernel panic
e crashar o seu sistema. Idealmente, o script será incapaz de alocar ou mexer na seção de memória do OS, mas certamente
deixará seu computador razoavelmente lento.





