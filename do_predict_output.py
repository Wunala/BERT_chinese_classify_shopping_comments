from predict import predicts
import pandas as pd

# 导入原始文本数据
df = pd.read_csv('data/test.csv', sep='\t', header=None)
# 创建空的Dataframe对象
result = pd.DataFrame(columns=['label', 'x_text'])
# 遍历文本并进行预测
for i in range(len(df)):
    dic = predicts([df[1][i]])
    result.loc[i] = [list(dic.values())[0][0], list(dic.keys())[0]]

# 保存到csv文件
result.to_csv('test_sentiment_results.csv')
