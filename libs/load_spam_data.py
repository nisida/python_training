""" span.cvsを読み込み """

import os
import sys
import csv
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
#from typing import List
#from gensim.corpora.dictionary import Dictionary
import numpy as np

def load_spam_data(file_path):
    
    """ span.csvを読み込み, token id, label id を返す
    Args:
        file_path (str): span.csvのパス
    Returns:
        id_train : 訓練用データのid
        label_id : 訓練用データのラベル
        id_test : テスト用データのid
        label_test : テスト用データのラベル
    """

    LABEL     = 'label'
    MESSAGE   = 'message'

    print(pd.__version__)

    df = pd.read_csv(file_path, encoding='latin-1', header=None, names = [LABEL, MESSAGE, 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])

    print("-------------")
    print("hum count   = ", sum([ x == "ham" for x in df[LABEL].values]))
    print("supam count = ", sum([ x == "spam" for x in df[LABEL].values]))
    print("-------------")

    # ノイズを取り除く
    clean_str = [x.replace('?', '') for x in df[MESSAGE]]
    clean_str = [x.replace('!', '') for x in clean_str]
    clean_str = [x.replace(',', '') for x in clean_str]
    clean_str = [x.replace('.', '') for x in clean_str]
    lower_msg = [x.lower() for x in clean_str] 
    
    # 文書のtokenを作成する
    all_tokens = [x.split() for x in lower_msg]
    max_token_len = max([len(x) for x in all_tokens])
    print("max_token_len = ", max_token_len)
    # stop wordsを取り除く
    stopwords = nltk.corpus.stopwords.words('english')
    all_tokens = [[x for x in words if x not in stopwords] for words in all_tokens]
    #print(all_tokens[100])
    #print("keys # = ", len(all_tokens))

    # all_tokensのコーパスを作成する
    cop_dict = {'nishida': 0}
    for token in all_tokens:
        for word in token:
            if word not in cop_dict:
                cop_dict[word] = max(cop_dict.values()) + 1            
    #print("cop_dict # = ", cop_dict)

    # all_tokensの中の単語を、cop_dictの単語IDに置き換える
    all_token_ids = []
    for token in all_tokens:
        token_ids = []
        for word in token:
            token_ids.append(cop_dict[word])
        all_token_ids.append(token_ids)
    print(all_token_ids[100])

    # hamとspamのラベルを数値に置き換える hum : 0 , spam : 1
    id_label = []
    for label in df[LABEL]:
        if label == "ham":
            id_label.append(0)
        else:
            id_label.append(1)

    #print("id_label # = ", id_label[100])
    #print("df[LABEL].values 100 = ", df[LABEL].values[100])
    
    tr_id, tr_label = all_token_ids[0: int(len(all_token_ids) * 0.8)], id_label[0: int(len(id_label) * 0.8)]
    t_id, t_label   = all_token_ids[int(len(all_token_ids) * 0.8) + 1:], id_label[int(len(id_label) * 0.8) + 1:]
    
    # 8:2 に比率で分割する
    return tr_id, tr_label, t_id, t_label