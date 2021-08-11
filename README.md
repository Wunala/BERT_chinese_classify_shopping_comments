数据集为网络上已经标记好的数据集，数据集的内容为购物平台的评论。
数据集原有62774条评论，标记为：0或1。此外数据集中包含了所购商品的种类，此练习中并未使用这一特征。
由于自己的电脑是笔记本（MacBook Air M1），性能有限，使用全部的数据集会花非常多的时间，因此随机抽取了总共5000条评论进行练习，以节约时间。
运行train_valid_test_split.ipynb文件（用sklearn中的模块来进行数据集的分割）将5000条数据集分割为： train集3999条（80%）；dev集501条（10%）；test集500条（10%）。

## Fine-tune过程按照BERT官方指导文档来进行：
### 第一步：在run——classifier中创建自己的DataProcessor：MyProcessor， 以及在main字典中添加自己创建的Processor；在predict.py中作相应修改；
### 第二步：运行train.sh文件进行训练，指定的预训练模型为官方的chinese_L-12_H-768_A-12；训练完成的模型保存到一个自己创建的my_model文件夹；模型训练的评估结果见:eval_results.txt
### 第三步：对test集里的文本进行预测，运行do_predict_output.py文件，其中指定运行参数：--init_checkpoint=my_model \（更多的运行参数就是predict.sh中的）；或者运行predict.sh来运行predict.py文件；这里我为了生成一个新的文件于是写了一个do_predict_output.py文件来得到结果。
### 第四步：运行do_predict_output.py的结果是test_sentiment_results.csv文件。

### 最后，在F_score.ipynb文件中计算了f1_score为: 0.914




