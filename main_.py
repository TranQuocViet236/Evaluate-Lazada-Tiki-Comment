import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LogisticRegression
import torch
import transformers
from transformers import BertModel, BertTokenizer
import joblib
from main import load_data, standardize_data

def load_bert(data, labels):
    model = BertModel.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    #encode lines
    for index in range(len(data)):
        data[index] = tokenizer.encode(data[index], add_special_tokens= True)

    #get length max of tokenized
    max_len = 0
    for value in pd.DataFrame(data).values:
        if len(value) > max_len:
            max_len = len(value)
    print('max len: ', max_len)


    return tokenizer, data

if __name__ == "__main__":
    df = load_data('data_crawler.csv')
    print(df.shape)
    data = np.array(df.data)
    for idx in range(len(data)):
        data[idx] = standardize_data(data[idx])
    # print(data.shape)
    # print(data)
    labels = np.array(df.labels)
    print(labels)

    tokenizer, tokenized_data = load_bert(data, labels)

    print('encode ', tokenized_data[1])

    print('decode', tokenizer.decode(tokenized_data[1]))
    print(pd.DataFrame(tokenized_data).values)