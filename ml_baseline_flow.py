# CSVファイルを扱うためのライブラリをインポート
import pandas as pd

# ex2.csvの情報をdf変数に格納する
df = pd.read_csv("ex2.csv")

# 上位３つを表示
print("ーーー上位３件のみ表示ーーー")
print(df.head(3))

print("ーーーデータの形を表示ーーー")
print(df.shape)


print("ーーー正解列（target）にはどんな値がある？ーーー")
print(df["target"].unique())

print("ーーーそれぞれの個数は何個？ーーー")
print(df["target"].value_counts())

print("ーーー欠損値はある？ーーー")
print(df.isnull().any(axis=0))

print("ーーーそれぞれの個数は？ーーー")
print(df.isnull().sum())

print("ーーー欠損値を同じカラムの中央値で補填し、その結果を表示ーーー")
df["x1"] = df["x1"].fillna(df["x1"].median())
df["x2"] = df["x2"].fillna(df["x2"].median())
print(df.isnull().any(axis=0))

# 特徴量と正解データに分ける
feature = df[['x0','x1','x2','x3']]
answer = df["target"]

# 機械学習のスタート
from sklearn.model_selection import train_test_split
from sklearn import tree

# 訓練データ（８０％）とテストデータ（２０％）を乱数０スタートで分割
x_train, x_test, y_train, y_test=train_test_split(feature, answer,
                                                  test_size=0.2, random_state=0)

# 決定木モデルの作成（最大の深さは３、スタート乱数ステートメントは０）
model = tree.DecisionTreeClassifier(max_depth = 3, random_state = 0)
# 訓練データによるモデルの学習
model.fit(x_train, y_train)

print("ーーー作成した決定木モデルの正解率は？ーーー")
print(model.score(x_test, y_test))

# 決定木モデルの予測
practice = [[1.56, 0.23, -1.1, -2.8]]
practice_df = pd.DataFrame(practice, columns = x_train.columns)
print("ーーー予測ーーー")
print(model.predict(practice_df))
