#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
从Hugging Face下载模型的Python程序
"""

import argparse
import os
from transformers import AutoModel, AutoTokenizer


def download_model(model_name, save_directory):
    """
    从Hugging Face下载模型和分词器
    
    Args:
        model_name (str): Hugging Face模型名称
        save_directory (str): 保存模型的目录
    """
    # 为每个模型创建单独的子目录
    model_save_directory = os.path.join(save_directory, model_name)
    print(f"正在下载模型: {model_name}")
    
    try:
        # 创建保存目录
        os.makedirs(model_save_directory, exist_ok=True)
        
        # 下载模型
        model = AutoModel.from_pretrained(model_name)
        print("模型下载完成")
        
        # 下载分词器
        print("正在下载分词器...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print("分词器下载完成")
        
        # 保存模型和分词器
        print(f"正在保存模型到: {model_save_directory}")
        model.save_pretrained(model_save_directory)
        tokenizer.save_pretrained(model_save_directory)
        print("模型和分词器保存完成")
        
    except Exception as e:
        print(f"下载过程中出现错误: {str(e)}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="从Hugging Face下载模型")
    parser.add_argument(
        "model_name", 
        help="Hugging Face模型名称，例如: bert-base-uncased"
    )
    parser.add_argument(
        "-d", "--directory", 
        default="./downloaded_models", 
        help="保存模型的目录 (默认: ./downloaded_models)"
    )
    
    args = parser.parse_args()
    
    # 下载模型
    success = download_model(args.model_name, args.directory)
    
    if success:
        print(f"模型已成功下载到: {os.path.abspath(args.directory)}/{args.model_name}")
    else:
        print("模型下载失败")


if __name__ == "__main__":
    main()
