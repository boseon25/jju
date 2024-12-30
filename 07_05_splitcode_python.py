# -*- coding: utf-8 -*-
"""07_05_SPLITCODE_PYTHON.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ecj-xVlg9z0qjOuMyYz_HLZvh_MvQGEC
"""

from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)

PYTHON_CODE = '''
# 오늘 날짜 12월26일이 생일인 유명인 8명을 나열해주세요. 생년월일을 표기해주세요.
import os
from langchain_teddynote.messages import stream_response # 스트리밍 출력
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from datetime import datetime

os.environ['OPENAI_API_KEY']='path/to/your/openai/api/key'

model = ChatOpenAI(
    model_name='gpt-4',
    max_tokens=2048,
    temperature=0.1,
)
print(datetime.now().strftime('%B %d'))

def get_today():
    return datetime.now().strftime('%B %d')

# template 정의
template = '오늘의 날짜는 {today} 입니다. 오늘이 생일인 유명일 {n}명을 나열해주세요. 생년월일을 표기해주세요.'

prompt = PromptTemplate(
    template=template,
    input_variables=['n'],
    partial_variables={
        'today': get_today(), # dictionary 형태로 partial_variables를 전달
    }
)

prompt.format(today=get_today(), n=8)

chain = prompt | model

print(chain.invoke({'today':get_today(), 'n':8}).content)
'''

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)

python_docs = python_splitter.create_documents([PYTHON_CODE])
python_docs

for doc in python_docs:
    print(doc.page_content)
    print("------------------")