import pandas as pd

# ① Excelを読み込む
df = pd.read_excel("data/data.xlsx")

# ② キャスト名を指定
cast_name = "うみS"

# ③ キャストで絞る
result = df[df["キャスト名"] == cast_name]

# ④ 必要な列だけにする
result = result[["受領金"]]

# ⑤ 結果を表示
print(result)
