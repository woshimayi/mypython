'''
*************************************: 
FilePath     : \zh-to-en-replace\llm_trans.py
version      : 
Author       : dof
Date         : 2025-04-30 13:38:24
LastEditors  : dof
LastEditTime : 2025-05-06 19:20:32
Descripttion :  
compile      :  
**************************************: 
'''
'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: llm_trans.py
@time: 2025/04/30 13:38
@desc: 
'''
import os
import torch
import gc
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# 禁用 CUDA 相关警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 设置 TensorFlow 日志级别
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # 禁用 CUDA

# 指定模型存储路径
MODEL_PATH = r"E:/facebook/nllb-200-distilled-600M"  # 本地模型目录

# 全局变量存储模型和分词器
model = None
tokenizer = None

def load_model():
    """
    从本地加载模型和分词器
    """
    global model, tokenizer
    
    try:
        # 清理内存
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        print("正在从本地加载模型...")
        
        # 检查模型文件是否存在
        if not os.path.exists(os.path.join(MODEL_PATH, "config.json")):
            raise FileNotFoundError(f"模型配置文件不存在: {MODEL_PATH}")
            
        # 从本地加载模型和分词器
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH, local_files_only=True)
        
        # 将模型移动到 CPU
        model = model.to("cpu")
        print("模型加载完成")
        
    except Exception as e:
        print(f"模型加载失败: {str(e)}")
        raise

def translate_text(text, source_lang="zho_Hans", target_lang="eng_Latn"):
    """
    使用 NLLB 模型进行翻译
    
    Args:
        text (str): 要翻译的文本
        source_lang (str): 源语言代码，默认中文简体
        target_lang (str): 目标语言代码，默认英语
    
    Returns:
        str: 翻译后的文本
    """
    global model, tokenizer
    
    try:
        # 如果模型未加载，则加载模型
        if model is None or tokenizer is None:
            load_model()
        
        # 准备输入
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        
        # 生成翻译
        with torch.no_grad():  # 禁用梯度计算
            translated_tokens = model.generate(
                **inputs,
                forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_lang),
                max_length=256,
                num_beams=5,  # 使用束搜索
                early_stopping=True,  # 启用早停
                do_sample=True,  # 启用采样
                temperature=0.7,  # 控制采样的随机性
                top_k=50,  # 限制候选词数量
                top_p=0.95  # 使用核采样
            )
        
        # 解码输出
        translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        
        # 如果翻译结果为空，返回 None
        if not translation.strip():
            print(f"警告: 翻译结果为空 - 输入文本: {text}")
            return None
            
        return translation
        
    except Exception as e:
        print(f"翻译失败: {str(e)}")
        print(f"输入文本: {text}")
        print(f"模型状态: {model is not None}")
        print(f"分词器状态: {tokenizer is not None}")
        return None

def translate_word(zh_word):
    """
    翻译单个中文单词到英文
    
    Args:
        zh_word (str): 中文单词
    
    Returns:
        str: 英文翻译
    """
    # 添加输入验证
    if not zh_word or not isinstance(zh_word, str):
        print(f"无效的输入: {zh_word}")
        return None
        
    # 去除首尾空白字符
    zh_word = zh_word.strip()
    
    # 如果输入为空，返回 None
    if not zh_word:
        print("输入文本为空")
        return None
        
    return translate_text(zh_word)

if __name__ == '__main__':
    try:
        # 测试翻译
        test_words = [
            "你好",
            "世界",
            "人工智能",
            "网关",
            "账号错误"
        ]
        
        print("翻译测试:")
        print("-" * 30)
        for word in test_words:
            print(f"正在翻译: {word}")
            translation = translate_word(word)
            if translation:
                print(f"中文: {word}")
                print(f"英文: {translation}")
                print("-" * 30)
            else:
                print(f"翻译失败: {word}")
                print("-" * 30)
                
    except Exception as e:
        print(f"程序执行出错: {str(e)}")
    finally:
        # 清理内存
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
