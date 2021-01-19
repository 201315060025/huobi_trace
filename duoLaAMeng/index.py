# encoding: utf-8
"""
教程地址：https://www.jianshu.com/p/0db025ebf0a1
建议代码复制到jupyter 中运行
"""

# 导入包
import turicreate as tc

# 设置图片地址
img_folder = 'image'

# 加载图片
data = tc.image_analysis.load_images(img_folder, with_path=True)

# 输出图片
print(data)

# 图片打标记
data['label'] = data['path'].apply(lambda path: 'doraemon' if 'doraemon' in path else 'walle')

# 此时再次查看
print(data)


# 数据储存一下
data.save('doraemon-walle.sframe')

# 简单查看数据框
data.explore()


# TuriCreate把data数据框分为训练集合和测试集合（TuriCreate把80%的数据分给了训练集，把剩余20%的数据拿到一边，等待测试）
train_data, test_data = data.random_split(0.8, seed=2)


# 开始使用训练数据  训练出模型
model = tc.image_classifier.create(train_data, target='label')

# 使用训练出的模型 验证预测数据
predictions = model.predict(test_data)

# 模型评估
metrics = model.evaluate(test_data)
print(metrics['accuracy'])



# 使用模型测试未知
"""
封装以上方法

"""


def load_data(image_src):
    """加载测试数据"""
    data = tc.image_analysis.load_images(image_src, with_path=True)
    return data


def split_train_test_data(data):
    """分割 训练数据和测试数据"""
    data['label'] = data['path'].apply(lambda path: 'doraemon' if 'doraemon' in path else 'walle')

    # 也可以查看图片详情
    # data.explore()
    train_data, test_data = data.random_split(0.8, seed=2)
    return train_data, test_data


def generate_model(train_data):
    """生成模型"""
    model = tc.image_classifier.create(train_data, target='label')
    return model


def predict_data(model, test_data):
    """预测数据， 生成预测结果"""
    predictions = model.predict(test_data)
    # 返回预测结果
    return predictions


def check_predict_data(test_data, predict_result):
    """测试数据和预测结果对比"""
    test_data["pre_label"] = predictions
    return test_data[test_data["pre_label"] != test_data["label"]]


#     return test_data


img_src = "/home/cetc28/lixbi/test_data/demo-python-image-classification/image/test"
new_data = load_data(img_src)

