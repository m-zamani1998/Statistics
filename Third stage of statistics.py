import pandas as pd
import json

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def filter_data(df):
    mean_age = df['age'].mean()
    filtered = df[(df['age'] < mean_age) & (df['income'] > 600)]

    filtered = filtered[['name', 'income']].reset_index(drop=True)
    filtered.index += 1  # شروع شمارش از 1

    print("افرادی که سن‌شون کمتر از میانگین و درآمدشون بیشتر از ۶۰۰ هست:")
    print(filtered)

if __name__ == "__main__":
    df = load_data(r"F:\Machine Learning\Summarizing\Information.txt")
    filter_data(df)
