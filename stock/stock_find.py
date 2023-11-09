#!/usr/bin/env python
# coding: utf-8

# In[23]:


import sys,os,re
import pandas as pd
import csv
import plotly.graph_objects as go

stockname = input()
os.chdir(f'C:/test/{stockname} 외국인매수추이')

stock_df = pd.DataFrame()

for file in os.listdir():
    if re.match(r'data_\d{4}_\d{8}.csv',file):
        # print(file)
        df = pd.read_csv(file,encoding='cp949',thousands=',')
        stock_df = pd.concat([stock_df,df])
    else: print(file)
        
# os.listdir()
stock_df = stock_df[['일자','외국인 합계']]
stock_df.set_index('일자',inplace=True)
stock_df.sort_index(inplace=True)

avg = stock_df['외국인 합계'].mean()
print(avg)
fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_df.index, y=stock_df['외국인 합계'], mode='lines', name='외국인 순매수량',yaxis='y1'))
fig.add_trace(go.Scatter(x=stock_df.index, y=[avg for i in range(len(stock_df.index))], mode='lines', name='평균', yaxis='y1'))


fig.update_layout(title_x = 0.5,title_y = 0.9,
                title_xanchor = 'center',title_yanchor = 'middle',
                  title=f'최근 5년 {stockname} 외국인 순매수량', 
                  xaxis_title='일자', yaxis_title='순매수량')
                #   yaxis2=dict(title='주가', overlaying='y', side='right'))
fig.show()

