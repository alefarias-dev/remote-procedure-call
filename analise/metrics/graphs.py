import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# carrega datasets
ds_l = pd.read_csv('grpc_metrics_localhost.csv')
ds_r = pd.read_csv('grpc_metrics_192.168.0.109.csv')
ds_rpyc = pd.read_csv('rpyc_metrics_localhost_2.csv')
ds_rpyc_r = pd.read_csv('rpyc_metrics_192.168.0.109.csv')


def remove_outliers(ds, min, max):
    mins = ds.quantile([min])
    maxs = ds.quantile([max])
    for col in ds.columns:
        ds = ds[ds.loc[:,col] > mins[col].values[0]]
        ds = ds[ds.loc[:,col] < maxs[col].values[0]]
    return ds


# remocao de outliers
ds_l      = remove_outliers(ds_l, .02, .98)
ds_r      = remove_outliers(ds_r, .02, .98)
ds_rpyc   = remove_outliers(ds_rpyc, .02, .98)
ds_rpyc_r = remove_outliers(ds_rpyc_r, .02, .98)

# boxplot
ax = ds_r.iloc[:,:-1].plot.box(figsize=(12,6), title="Tempos por função (grpc remoto)")
ax.set_ylabel("Tempo em segundos")
plt.xticks(rotation=45)
ax.set_xlabel("Função")


# barplot mean
fig, ax = plt.subplots(figsize=(12,6))
error_config = {'ecolor': '0.3'}

ds = ds_rpyc_r
for i, col in enumerate(ds_r.columns):
    if col == 'euclidean_arg': continue
    ax.barh(i, ds[col].mean(), color=cm.Pastel2(i), xerr=ds[col].std(), error_kw=error_config)
    ax.text(ds[col].mean()*.3, i, str(round(ds[col].mean(),8)))
    
ax.set_yticklabels(ds_r.columns[:-1])
ax.set_yticks(np.arange(len(ds_r.columns)) + .2)
ax.set_title('Tempo médio por função (rpyc remoto)')
ax.set_xlabel("Tempo em segundos")
ax.set_ylabel("Função")

# scatter for latency
fig, ax = plt.subplots(figsize=(12,6))
ax.scatter(x=np.arange(len(ds_rpyc)), y=ds_rpyc['int_arg'], label='local', color='green', marker='o')
ax.scatter(x=np.arange(len(ds_rpyc_r)), y=ds_rpyc_r['int_arg'], label='remoto', color='orange', marker='o')
ax.set_title('RPyC: comparativo de oscilação de latência remoto vs local (int_arg)')
ax.set_ylabel("Tempo em segundos")
ax.set_xlabel("Iteração de teste")
ax.legend()

# comparativo
fig, ax = plt.subplots(figsize=(12,6))
error_config = {'ecolor': '0.3'}
bar_w = .35

ds_1 = ds_l
ds_2 = ds_rpyc
for i, col in enumerate(ds_l.columns):
    if col != 'euclidean_arg': continue
    ax.barh(i, ds_1[col].mean(), bar_w, color=cm.Pastel2(i))
    ax.text(0.00002, i, 'grpc: '+str(round(ds_1[col].mean(),8)))
    
    ax.barh(i+bar_w, ds_2[col].mean(), bar_w, color=cm.Pastel2(i))
    ax.text(0.00002, i+bar_w, 'rpyc: '+str(round(ds_2[col].mean(),8)))

ax.set_yticklabels([ds_l.columns[8]])
# ax.set_yticks(np.arange(len(ds_l.columns))+.2)
ax.set_title('Comparativo euclidean tempo médio (execução local)')
ax.set_xlabel("Tempo em segundos")
ax.set_ylabel("Função")