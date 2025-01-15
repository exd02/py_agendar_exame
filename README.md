#### Disciplinas em comum entre TODOS os cursos
01 - Português  
02 - Matemática  
03 - Física  
04 - Biologia  
05 - Química  
06 - Geografia  
07 - História  
08 - Ed. Física  
09 - Sociologia  
10 - Filosofia  
11 - Inglês  

#### Disciplinas em comum entre ALGUNS cursos
80 - Lab Ciencias Exatas  
81 - Arte

#### Agro
12 - Geodesia  
13 - Agricultura  
14 - Introducao aos estudos e praticas em agro   

#### Informática
16 - Banco de Dados  
17 - Programacao Web  
19 - Montagem e Manutenção  
20 - Introdução a Algoritmos  

#### Alimentos
21 - Instal. e Equipamentos de Alimentos  
22 - Química e Bioquímica de Alimentos  
23 - Micro Geral de Ali. e Anal. Microbiológica  
24 - Práticas Agroindustriais  

Ideia:
- Achar os horários livres em comum entre todas as disciplinas (HLC)
- Completar os horários livres com as *Disciplinas em comum entre TODOS os cursos*
  - Se todos HLCs forem usados e ainda tiver mais disciplinas, será necessário aplicar separadamente para cada curso as disciplinas restantes
  - Usar coloração de grafos para achar quais matérias podem ser aplicadas simultaneamente
    - O Vértice é a disciplina
    - As arestas serão as disciplinas que um aluno irá fazer a prova (se formará um grafo completo entre essas disciplinas, pois elas não podem ser feitas simultaneamente)
- Caso ainda HLCs disponíveis, fazer a mesma coisa com as *Disciplinas em comum entre ALGUNS cursos*
- Após isso, aplicar individualmente para cada curso suas matérias exclusivas

OBS.: Restrição(ões):
- Max de provas que um aluno pode fazer em um dia é 3
