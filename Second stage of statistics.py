import pandas as pd
import json

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def analysis(df):
    ali_count = df[df['name'] == 'Ali']['name'].count()
    print("تعداد افراد با نام Ali:", ali_count)

    median_income = df['income'].median()
    num_median_income = df[df['income'] == median_income]['income'].count()
    print("تعداد افرادی که درآمدشون دقیقا برابر میانه‌ است:", num_median_income)

    mode_age = df['age'].mode()[0]
    mode_age_count = df[df['age'] == mode_age]['age'].count()

    print(f"سن پرتکرارتر: {mode_age} – تعداد تکرار: {mode_age_count}")

if __name__ == "__main__":
    df = load_data(r"F:\Machine Learning\Summarizing\Information.txt")
    analysis(df)
 