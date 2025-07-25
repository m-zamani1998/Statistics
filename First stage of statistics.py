import pandas as pd
import json

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def show_res (df):
    print("میانگین سن:", df['age'].mean())
    print("میانگین درآمد:", df['income'].mean())
    print("میانه سن:", df['age'].median())
    print("میانه درآمد:", df['income'].median())
    print("نمای سن:", df['age'].mode()[0])
    print("نمای درآمد:", df['income'].mode()[0])

    if df['income'].mean() > df['income'].median():
        print("میانگین از میانه بیشتر است")
    else:
        print("میانه از میانگین بیشتر است یا برابر")

if __name__ == "__main__":
    df = load_data(r"F:\Machine Learning\Summarizing\Information.txt")
    show_res(df)
