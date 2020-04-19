#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[5]:


black_friday.head()


# In[6]:


black_friday.info()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[7]:


black_friday.shape


# In[95]:


def q1():
    return (537577, 12)    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[28]:


black_friday['Age'].value_counts()


# In[33]:


black_friday[black_friday['Age'] == '26-35'].groupby('Gender')['User_ID'].nunique()


# In[43]:


black_friday[black_friday['Age'] == '26-35'].groupby('Gender')['User_ID'].count()


# In[32]:


def q2():
    return 49348


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[16]:


black_friday['User_ID'].nunique()


# In[6]:


def q3():
    return 5891


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[40]:


black_friday.dtypes.nunique()


# In[41]:


def q4():
    return 3    


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[51]:


black_friday.isna().sum() / black_friday.shape[0]


# In[8]:


def q5():
    return 0.694410


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[52]:


black_friday.isna().sum()


# In[105]:


def q6():
    return 373299


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[59]:


black_friday[black_friday.notna()]['Product_Category_3'].mode()


# In[104]:


def q7():
    return 16.0    


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[51]:


mean = black_friday['Purchase'].mean()
std = black_friday['Purchase'].std()

black_friday['Purchase_Standardized'] = (black_friday['Purchase'] - mean) / std

black_friday['Purchase_Normalized'] = (black_friday['Purchase'] - black_friday['Purchase'].min()) / (black_friday['Purchase'].max() - black_friday['Purchase'].min())


# In[55]:


purchase_standarized_mean = black_friday['Purchase_Normalized'].mean()
print(f'Old mean: {mean}') 
print(f'New mean: {purchase_standarized_mean}')


# In[58]:


def q8():
    return 0.38479390362696736


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[102]:


purchase_normalized_filter = (black_friday['Purchase_Standardized'] > -1) & (black_friday['Purchase_Standardized'] <= 1)

len(black_friday[purchase_normalized_filter])


# In[12]:


def q9():
    return 348631


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[20]:


filter_isna = (black_friday['Product_Category_2'].isna()) & (black_friday['Product_Category_3'].notna())
black_friday[filter_isna]


# In[13]:


def q10():
    return True

