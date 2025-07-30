# Hugging Face 模型下载器

这是一个简单的Python程序，用于从Hugging Face下载模型和分词器。

## 功能

- 从Hugging Face下载预训练模型
- 下载对应的分词器
- 将模型和分词器保存到本地目录

## 安装依赖

程序需要安装`transformers`和`torch`库。有两种方式安装依赖：

### 方式一：使用requirements.txt（推荐）

```bash
pip install -r requirements.txt
```

### 方式二：手动安装

```bash
pip install transformers torch
```

## 使用方法

### 基本用法

```bash
python download_model.py <model_name>
```

例如：
```bash
python download_model.py bert-base-uncased
```

### 指定保存目录

```bash
python download_model.py <model_name> -d <directory>
```

例如：
```bash
python download_model.py bert-base-uncased -d ./my_models
```

### 帮助信息

```bash
python download_model.py -h
```

## 示例

下载BERT模型：
```bash
python download_model.py bert-base-uncased
```

这将把模型下载到默认的`./downloaded_models`目录中。

## 注意事项

1. 首次下载模型时可能需要一些时间，具体取决于模型大小和网络速度。
2. 下载的模型将保存在指定目录中，可以离线使用。
3. 确保有足够的磁盘空间来存储模型（某些模型可能很大）。
