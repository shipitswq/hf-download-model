#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试下载的模型是否可以正确加载的Python程序
"""

import argparse
import os
from transformers import AutoModel, AutoTokenizer


def test_model(model_path):
    """
    测试下载的模型是否可以正确加载
    
    Args:
        model_path (str): 模型路径
    """
    print(f"正在测试模型: {model_path}")
    
    try:
        # 加载模型
        print("正在加载模型...")
        model = AutoModel.from_pretrained(model_path)
        print("模型加载成功")
        
        # 加载分词器
        print("正在加载分词器...")
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        print("分词器加载成功")
        
        # 简单测试
        print("正在进行简单测试...")
        text = "这是一个测试句子。"
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        print(f"模型输出形状: {outputs.last_hidden_state.shape}")
        print("模型测试完成，一切正常！")
        
    except Exception as e:
        print(f"测试过程中出现错误: {str(e)}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="测试下载的模型是否可以正确加载")
    parser.add_argument(
        "model_path", 
        help="模型路径，例如: ./downloaded_models/prajjwal1/bert-tiny"
    )
    
    args = parser.parse_args()
    
    # 测试模型
    success = test_model(args.model_path)
    
    if not success:
        exit(1)


if __name__ == "__main__":
    main()
