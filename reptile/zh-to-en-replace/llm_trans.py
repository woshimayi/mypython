'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: llm_trans.py
@time: 2025/04/30 13:38
@desc: 
'''
import torch
import os
from transformers import AutoProcessor, SeamlessM4Tv2Model

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # 禁用 GPU


# 指定模型名称
model_name = r"C:/Users/hg-work/Downloads/seamless-m4t-v2-large"

# 加载处理器和模型
# processor = AutoProcessor.from_pretrained(model_name)
model = SeamlessM4Tv2Model.from_pretrained(model_name)

# 将模型移动到 CPU (如果尚未在 CPU 上)
model = model.to("cpu")

# 输入文本和目标语言
text = "你好，世界！"
target_language = "eng"

# 准备输入
inputs = processor(text=text, src_lang="zho", tgt_lang=target_language, return_tensors="pt")

# 将输入移动到 CPU
inputs = inputs.to("cpu")

# 生成翻译
with torch.no_grad():
    outputs = model.generate(**inputs, max_length=256)

# 解码输出
translated_text = processor.decode(outputs[0], skip_special_tokens=True)

print(f"原始文本 (中文): {text}")
print(f"翻译后文本 (英文): {translated_text}")

if __name__ == '__main__':
    print('Hello world')
