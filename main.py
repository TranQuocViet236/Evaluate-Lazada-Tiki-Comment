import re
from underthesea import word_tokenize

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import torch
import transformers
from transformers import BertModel, BertTokenizer
import joblib


def load_data(csv_file_path):
    df = pd.read_csv(csv_file_path, delimiter="\t", header=None)
    return df


def standardize_data(row):
    # # remove special character
    # row = re.sub(r"[\.,\?]+$-", "", row)
    # Remove all . , " ... in sentences
    row = row.replace(",", "").replace(".", "") \
        .replace(";", "").replace("“", "") \
        .replace(":", "").replace("”", "") \
        .replace('"', "").replace("'", "") \
        .replace("!", "").replace("?", "") \
        .replace("-", "").replace("+", "")

    row = row.strip()

    return row


def tokenizer(row):
    word_arr = word_tokenize(row, format="text")
    return word_arr


if __name__ == "__main__":
    # row = "Quần siêu đẹp, giao? hàng nhanh."
    # row = standardize_data(row)
    # print(row)
    # word_arr = tokenizer(row)
    # print(word_arr)
    file_path = ".\data_crawler.csv"
    df = load_data(file_path)
    print(df)