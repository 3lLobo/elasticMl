# %%
import eland as ed
import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

# Load dotenv
load_dotenv()
ELASTIC_PWD = os.getenv("ELASTIC_PWD", None)

es_host = 'https://mi4luna:9200'

es = Elasticsearch(
    es_host,
    http_auth=('elastic', ELASTIC_PWD),
    verify_certs=False,
)

# %%
df = ed.DataFrame(es, es_index_pattern="logs-*")

# %%
df.head()

# %%
df.columns


# %%
df.columns.tolist()[:11]

# %%
df.info()

# %%
from tqdm import trange

val_counts = dict()


for i in trange(len(df.columns)):
    #  print value counts
    try:
      name = df.columns.tolist()[i]
      counts = df[name].value_counts()
      val_counts[name] = counts
    except:
      pass


# %%
v_count = 0 
for k, v in val_counts.items():
    if len(v) > 3:
        v_count += 1
        print('\n', k, '\n', v, '\n')

print('Total columns with value counts: ', v_count)

# %%
import pickle as pkl

with open('colname_valcounts_dict.pkl', 'wb') as f:
    pkl.dump(val_counts, f)

