# -*- coding: utf-8 -*-
"""Cópia de Visanalytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qWsKoheeZfdiuMw2uvh23Ed18Og6fT9g

### Importação das bibliotecas necessárias

Inserir aqui a descrição das bibliotecas utilizadas.

### Conhecendo o dataset
"""

!pip3 install pycaret

import pandas as pd
import numpy as np

from pycaret.classification import *
from pycaret.datasets import get_data

df = pd.read_csv('/content/Dataset_Treino.csv')

df.shape

df.info()

pd.set_option('display.max_columns', None)
df.head()

"""### Tratamento de dados

#### Destrinchando a coluna Recursos
"""

df['Recursos'].value_counts()

df['Recursos'].nunique()

df['Recursos'].isnull().value_counts()

df['Recursos'].fillna('Indefinido', inplace=True)

recursos = []

for i in df['Recursos']:
  parte = i.split('/')
  if parte not in recursos:
    recursos.append(parte)

print(recursos)

recursos_unicos = set()

for lista in recursos:
  recursos_unicos.update(lista)

recursos_unicos = list(recursos_unicos)

print(recursos_unicos)

for i in recursos_unicos:
  print(i)

atributos = ['Tablet próprio', 'Internet wifi', 'Celular compartilhado com outro familiar', 'Internet 4G', 'Computador', 'Indefinido', 'Tablet compartilhado', 'Celular próprio']

for atributo in atributos:
  df[atributo] = df['Recursos'].apply(lambda x: 1 if atributo in x else 0)

df.head(10)

df.drop('Recursos', axis=1, inplace=True)

df.columns

"""#### Tratamento de dados nulos"""

df.isnull().sum()

df = df.dropna()

"""### Pré-processamento"""

df_features = df.drop('ID_Aluno', axis=1)

for column in df_features.columns:
    unique_values = df_features[column].unique()
    print(f"Valores únicos na coluna '{column}': \n")
    for valor in unique_values:
        print(valor)
    print('\n')

"""#### Label Encoding em colunas de classificação binária

Colunas binárias: Tipo_escola, Trabalhando, Estudando, Disponibilidade_Tutoria, 'Disponibilidade_3_Meses'
"""

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()

binary_columns = ['Tipo_escola', 'Trabalhando', 'Estudando', 'Disponibilidade_Tutoria', 'Disponibilidade_3_Meses']

df[binary_columns] = df[binary_columns].apply(lambda column: le.fit_transform(column))

df

"""#### Label Encoding em colunas categóricas ordinais"""

# ordinary_columns = ['Escolaridade']

# df[ordinary_columns] = df[ordinary_columns].apply(lambda column: le.fit_transform(column))

# df

renda_mapping = {
  'Até 1 salário mínimo (até R$1.100)': 1,
  'Entre 1 e 2 salários mínimos (R$1.100 – R$2.200)': 2,
  'Entre 2 e 3 salários mínimos (R$2.200 – R$3.300)': 3,
  'Entre 3 e 4 salários mínimos (R$3.300 – R$4.400)': 4,
  'Entre 4 e 5 salários mínimos (R$4.400 – R$5.500)': 5,
  'Mais que 5 salários mínimos (mais que R$5.500)': 6
}

escolaridade_mapping = {
  'Cursando o 3º ano do Ensino Médio': 0,
  'Ensino Médio concluído e não estudando': 1,
  'Cursando o Ensino Superior': 2,
  'Ensino Superior concluído': 3,
  'Ensino Médio concluído': 4
}

concluiu_ead_mapping = {
  'Nunca realizei um curso a distância': 0,
  'Ainda não concluí um curso a distância': 1,
  'Sim e fiz parcialmente pelo computador e parcialmente pelo celular': 2,
  'SIm e fiz totalmente pelo celular': 3,
  'Sim e fiz totalmente pelo computador': 4
}

aprender_ead_mapping = {
  'Quase nada': 0,
  'Não sei dizer': 1,
  'Eu prefiro cursos presenciais': 2,
  'Muito eu tenho uma rotina definida para participar de cursos a distância': 3
}

horario_estudando_mapping = {
  'Já concluí': 0,
  'Manhã': 1,
  'Tarde': 2,
  'Noite': 3,
  'Integral': 4
}

df['Escolaridade'] = df['Escolaridade'].map(escolaridade_mapping)
df['Renda_Familiar'] = df['Renda_Familiar'].map(renda_mapping)
df['Concluiu_EAD'] = df['Concluiu_EAD'].map(concluiu_ead_mapping)
df['Aprender_EAD'] = df['Aprender_EAD'].map(aprender_ead_mapping)
df['Horario_Estudando'] = df['Horario_Estudando'].map(horario_estudando_mapping)

df

"""#### Target Encoding em colunas de classificação múltipla"""

municipio_mean_encoded = df.groupby('Municipio')['Abandono_curso'].mean().reset_index()

municipio_mean_encoded.rename(columns={'Abandono_curso': 'Municipios_codificados'}, inplace=True)

df = df.merge(municipio_mean_encoded, on='Municipio', how='left')

estado_mean_encoded = df.groupby('Estado')['Abandono_curso'].mean().reset_index()

estado_mean_encoded.rename(columns={'Abandono_curso': 'Estados_codificados'}, inplace=True)

df = df.merge(estado_mean_encoded, on='Estado', how='left')

estado_mean_encoded = df.groupby('Conheceu_PROA')['Abandono_curso'].mean().reset_index()

estado_mean_encoded.rename(columns={'Abandono_curso': 'Conheceu_PROA_codificado'}, inplace=True)

df = df.merge(estado_mean_encoded, on='Conheceu_PROA', how='left')

df.head(3)

"""#### Descartando colunas redundantes, desnecessárias ou irrelevantes"""

df.columns

descarte = ['ID_Aluno', 'Estado', 'Municipio', 'Conheceu_PROA', 'Data_Inscrição', 'Dias_Espera_Aprovacao', 'Dias_Espera_Inicio', 'Indefinido']

df = df.drop(columns = descarte, axis=1)
df.head()

"""#### Normalização de dados"""

df.columns

df.dtypes

df['Pessoas_Casa'] = df['Pessoas_Casa'].replace('Mais que 10', 11).astype(int)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
df[colunas_numericas] = scaler.fit_transform(df[colunas_numericas])

df

"""#### Reordenando as colunas do dataset"""

df.columns

ordem = ['Abandono_curso', 'Idade', 'Tipo_escola', 'Escolaridade', 'Trabalhando',
       'Estudando', 'Concluiu_EAD', 'Aprender_EAD', 'Disponibilidade_Tutoria',
       'Disponibilidade_3_Meses', 'Pessoas_Casa', 'Renda_Familiar',
       'Horario_Estudando', 'Tablet próprio',
       'Internet wifi', 'Celular compartilhado com outro familiar',
       'Internet 4G', 'Computador', 'Tablet compartilhado',
       'Celular próprio', 'Estados_codificados',
       'Conheceu_PROA_codificado']

df = df[ordem]

df

"""#### Balanceamento dos dados

"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
df['Abandono_curso'].value_counts().plot(kind='bar')
plt.title('Distribuição das Classes da Variável Target')
plt.xlabel('Classe')
plt.ylabel('Contagem')
plt.show()

contagem_classes = df['Abandono_curso'].value_counts()
print(contagem_classes)

from imblearn.over_sampling import SMOTE

X = df.drop('Abandono_curso', axis=1)
y = df['Abandono_curso']

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

df = pd.DataFrame(X_resampled, columns=X.columns)
df['Abandono_curso'] = y_resampled

contagem_classes = df['Abandono_curso'].value_counts()
print(contagem_classes)

ordem = ['Abandono_curso', 'Idade', 'Tipo_escola', 'Escolaridade', 'Trabalhando',
       'Estudando', 'Concluiu_EAD', 'Aprender_EAD', 'Disponibilidade_Tutoria',
       'Disponibilidade_3_Meses', 'Pessoas_Casa', 'Renda_Familiar',
       'Horario_Estudando', 'Tablet próprio',
       'Internet wifi', 'Celular compartilhado com outro familiar',
       'Internet 4G', 'Computador', 'Tablet compartilhado',
       'Celular próprio', 'Estados_codificados',
       'Conheceu_PROA_codificado']

df = df[ordem]

correlation_matrix = df.corr()

plt.figure(figsize=(36, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Matriz de Correlação")
plt.show()

df.columns

descarte = ['Idade', 'Tipo_escola', 'Trabalhando',
       'Estudando', 'Aprender_EAD', 'Disponibilidade_Tutoria',
       'Disponibilidade_3_Meses', 'Pessoas_Casa',
       'Horario_Estudando', 'Tablet próprio',
       'Celular compartilhado com outro familiar', 'Internet 4G',
       'Tablet compartilhado', 'Celular próprio']

df = df.drop(columns = descarte, axis=1)
df.head()

"""### Testando modelos"""

setup(data=df, target='Abandono_curso')

best_model = compare_models()

import pickle
import lightgbm as lgb

save_model(best_model, 'modelo_pycaret.pkl')

"""------------------------------------------------------------------------------------------

"""

df.to_csv('dataset.csv')