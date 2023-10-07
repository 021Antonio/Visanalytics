# Visanalytics

## Oque temos de dados

### Colunas

como base temos 21 colunas sendo elas, 14 elas **Talvez** importantes. 

```
ID_Aluno                    
Idade                       
Tipo_escola                 
Escolaridade                
Estado                      
Municipio                  
Trabalhando                 
Estudando
Aprender_EAD                
Recursos
Pessoas_Casa                
Renda_Familiar
Horario_Estudando
Abandono_curso
```

As colunas "Data_Inscrição",
"Dias_Espera_Aprovacao" e "Dias_Espera_Inicio" podem nao represntar nada, ja que o objetivo é encontrar um possivel motivo de desistencia e essas colunas representam o estado do aluno antes de entrar no curso.

### Dados

Ao total, temos 21 colunas e 3738 linhas. Temos 22 dados nulos(
    
    Municipio                  11
    Estudando                   5
    Concluiu_EAD                2
    Recursos                    4
    
)

#### Cada coluna

```
ID_Aluno                 ...

Idade = Alunos de 16 a 24 anos

Tipo_escola = publica ou bolsa de estudos

Escolaridade = Cursando 3 ano, Ensino medio completo e nao estudando, cursando superior, superior concluido, ensino medio completo

Estado                   ...

Municipio                ...

Trabalhando = Sim ou Não

Estudando = Sim ou Não

Concluiu_EAD = Sim e fez pelo telefone, nao concluiu, nunca fez, sim e fez pelo telefone e pelo computador, sim e fiz pelo computador

Aprender_EAD = Apreudeu, prefere curso a distancia, nao sabe dizer, "Quase nada"

Recursos = ##Muita informação##

Disponibilidade_Tutoria = Sim ou Não

Disponibilidade_3_Meses = Sim ou Não

Pessoas_Casa = entre 1 a 10 pessoas ou mais de 10 pessoas

Renda_Familiar = entre 1 ate 5 salaros minimos 

Conheceu_PROA = ##redes sociais##

Horario_Estudando = manha, tarde, noite, integral , ja conclui

Data_Inscrição            ...

Dias_Espera_Aprovacao     ...

Dias_Espera_Inicio        ...

Abandono_curso = 1 ou 0 () Sim ou não. 
```
<h3>Coluna recursos</h3>
Essa coluna é uma coisa bem importante, tem muita imformação que pode contribuir 

```
Computador/Celular próprio/Tablet próprio/Internet wifi/Internet 4G',
       'Computador', 'Celular próprio/Internet wifi',
       'Computador/Celular próprio',
       'Computador/Celular próprio/Internet wifi/Internet 4G',
       'Computador/Celular próprio/Internet wifi',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Tablet próprio/Internet wifi/Internet 4G',
       'Celular próprio/Internet wifi/Internet 4G',
       'Celular próprio/Tablet compartilhado/Internet wifi',
       'Computador/Internet wifi',
       'Celular compartilhado com outro familiar/Tablet próprio/Internet wifi',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Internet wifi/Internet 4G',
       'Computador/Celular próprio/Tablet próprio/Internet wifi',
       'Celular próprio', 'Celular próprio/Internet 4G',
       'Celular próprio/Tablet próprio/Internet wifi',
       'Computador/Celular próprio/Internet 4G',
       'Celular próprio/Celular compartilhado com outro familiar/Internet wifi',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Internet wifi',
       nan, 'Celular próprio/Tablet próprio',
       'Computador/Celular próprio/Tablet compartilhado',
       'Celular compartilhado com outro familiar/Internet wifi',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Tablet próprio/Tablet compartilhado/Internet wifi/Internet 4G',
       'Celular próprio/Tablet compartilhado',
       'Celular próprio/Celular compartilhado com outro familiar/Internet 4G',
       'Internet 4G',
       'Computador/Celular compartilhado com outro familiar',
       'Celular compartilhado com outro familiar',
       'Computador/Internet 4G',
       'Celular compartilhado com outro familiar/Internet wifi/Internet 4G',
       'Computador/Celular próprio/Tablet compartilhado/Internet wifi/Internet 4G',
       'Computador/Celular compartilhado com outro familiar/Internet 4G',
       'Celular próprio/Tablet compartilhado/Internet wifi/Internet 4G',
       'Computador/Celular compartilhado com outro familiar/Internet wifi',
       'Celular próprio/Tablet próprio/Tablet compartilhado/Internet wifi',
       'Celular próprio/Tablet próprio/Internet wifi/Internet 4G',
       'Tablet próprio/Internet wifi',
       'Computador/Internet wifi/Internet 4G',
       'Computador/Celular compartilhado com outro familiar/Internet wifi/Internet 4G',
       'Computador/Celular próprio/Tablet próprio/Tablet compartilhado/Internet 4G',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Tablet compartilhado/Internet wifi',
       'Computador/Celular próprio/Tablet próprio/Internet 4G',
       'Celular próprio/Celular compartilhado com outro familiar/Internet wifi/Internet 4G',
       'Celular próprio/Celular compartilhado com outro familiar',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Tablet próprio/Tablet compartilhado/Internet wifi',
       'Internet wifi',
       'Computador/Celular compartilhado com outro familiar/Tablet compartilhado/Internet wifi/Internet 4G',
       'Celular compartilhado com outro familiar/Internet 4G',
       'Computador/Celular próprio/Celular compartilhado com outro familiar/Internet 4G',
       'Computador/Celular próprio/Tablet próprio',
       'Computador/Celular próprio/Celular compartilhado com outro familiar',
       'Tablet próprio/Tablet compartilhado', 'Tablet próprio',
       'Computador/Celular próprio/Tablet compartilhado/Internet wifi'
```


<h1> Em contrução... </h1>
