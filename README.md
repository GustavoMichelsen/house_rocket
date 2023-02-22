# House Rocket - An Imaginary Company

O objetivo deste projeto é gerar insights para compra de casas por uma empresa do ramo imobiliário.
Através da análise exploratória dos dados foi possível perceber quais os dados mais relevantes, filtrá-los e entregar uma ferramenta que realmente poderá ser utilizada pela empresa para aumentar seus lucros.
Clicando na imagem abaixo, você será redimensionado para o Dashboard.


<a href="https://gustavo-michelsen-house-rocket.streamlit.app/" target="_blank" class="image fit thumb"><img src="https://github.com/GustavoMichelsen/portifolio_projetos/blob/main/images/thumbs/01.jpg?raw=true" ></a></a>

## Detalhes do Projeto

### Questão de Negócio

##### O que se quer resolver?

- Trazer as melhores oportunidades de negócio.
- Uma lista com as melhores casas para compra → venda;
- Segunda lista com as melhores casas para compra → reforma → venda.

##### Qual a problema, a dor, a necessidade do time de negócio ?

- Encontrar as oportunidades mais lucrativas.

### Premissas de Negócio
##### O que foi assumindo para realizar o projeto?
- O valor de sqft_basement já está incluído no sqft_living;
- A empresa vende 100 casas ao ano;
- O lucro bruto da empresa atualmente é de 27% ao ano.

### Planejamento da Solução
##### Qual o plano utilizado para resolver o problema?
- Coleta dos dados do https://www.kaggle.com/;
- Retirados os outliers;
- Teste de hipóteses;
- Separadas as casas que são para reforma das que são para compra e venda;
- Construídas as tabelas;
- Construídos os mapas.
- Dividir as casas em 2 segmentos (compra e venda, renovação e venda)
- Compra e venda. Buscar casas em boas condições, categorizadas por m², preferencialmente com porão pelo menor valor possível;
- Reforma e venda. Encontrar casas em condições ruins, categorizadas por m², preferencialmente com porão, por pelo menos 35% do valor que ela será revendida.

### Os 5 principais Insights de dados
###### Há diferença entre os valores das casas dependendo da estação do ano(sazonalidade).
Resposta: Não. Quando analisada a variação de preços entre as estações, não há mudanças significativas de valores entre as casas similares.

###### Casas com porão tem o valor por m² mais caro.
Resposta: Sim. Casas com porão tem um valor 12,5% mais alto em comparação com casas sem porão.

###### Casas reformadas valem mais que casas mais novas.
Resposta: Sim. Casas que passaram por reforma tem um valor 28,6% maior do que as não reformadas.

###### Há diferença entre o preço do m² da casa.
Resposta: Sim. Existe uma correlação entre o preço e os tamanhos, havendo casas mais baratas, em mesmas condições e tamanho que outras.

###### Casa compradas baratas e reformadas dão mais lucro que apenas compra e venda.
Resposta: Sim. Existem casas que podem ser compradas a um valor baixo, reformadas e ainda darem um lucro maior que a compra e venda.

### Resultados financeiros para o negócio
A empresa pode ter um lucro bruto médio de 60% sobre as aplicações.

### Conclusão
Através da análise dos dados consegui alcançar um resultado positivo, trazendo como solução um dashboard interativo que auxiliará os gestores da empresa a tomarem decisões mais assertivas.

### Lições aprendidas
Como meu primeiro projeto de ciência de dados, ele foi desafiador por exigir tanto a aplicação do conhecimento aprendido durante o curso, quanto a aquisição de novos conhecimentos que melhoraram a qualidade da solução.

Pude ainda perceber na prática a complexidade de trazer para o usuário final uma solução assertiva que faça sentido para o negócio e que agregue ao conhecimento já existente na empresa.

Próximos passos
Para melhorar ainda mais o projeto, trazendo novas versões, percebo que seria necessário melhorar os filtros quanto a quantidade de quartos na casa, banheiros, qualidade da casa e separação por zipcode (vizinhança).

Em um segundo momento poderia fazer novos filtros que entregassem essa solução. E em uma terceira versão do projeto, aplicar um algoritmo de machine learning que faça a separação das casas conforme características parecidas.

A aplicação dessas melhorias melhoria a assertividade das escolhas e maximalizaria o lucro da empresa.

### Contatos
<p> Email: gtv.michelsen@gmail.com </p>
<p> Linkedin: <a href="https://www.linkedin.com/in/gustavo-michelsen-30946a223/"> Clique aqui!!! </a> </p> 
