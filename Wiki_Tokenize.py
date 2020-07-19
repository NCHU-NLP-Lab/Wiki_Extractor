import json
from udicOpenData.dictionary import *
from udicOpenData.stopwords import *
import jieba.posseg as pseg
import jieba
import re
from tqdm import tqdm
import pickle
from pathlib import Path, PurePath
import argparse


STOPWORD_PKL = pickle.load(open(str(PurePath(Path(__file__).resolve().parent, 'stopwords.pkl')), 'rb'))
STOPWORD_EN_PKL = pickle.load(open(str(PurePath(Path(__file__).resolve().parent, 'stopwords-en.pkl')), 'rb'))

def is_chinese(keyword):
    for uchar in keyword:
        if '\u4e00' <= uchar <= '\u9fff':
            continue
        else:
            return False
    return True

def is_english(keyword):
    if not is_chinese(keyword) and keyword.isalpha():
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    
    # Required parameters
    parser.add_argument("--file_path", default='./wiki.json', type=str, required=False, help="wiki file path")
    parser.add_argument("--output_path", default='./', type=str, required=False, help="output path")    
    args = parser.parse_args()

    with open(args.file_path) as file:
        data = json.load(file)

    res = []

    for i, ele in enumerate(tqdm(data)):
        articles = ele['articles'].strip()
        doc_tokens = []
        sent_tokens = []
        for token in pseg.cut(articles):
            if token.word in ['，','。','；']:
                if len(sent_tokens) != 0:
                    doc_tokens.append(sent_tokens)
                sent_tokens = []
            elif (token.word not in STOPWORD_PKL 
                and (is_chinese(token.word) or (is_english(token.word) and len(token.word) >= 2)) 
                and token.word not in ['\xa0', '\xc2'] 
                and not token.word.isdigit()):
                sent_tokens.append(tuple(token))

        res.append({'id' : i, 'title' : ele['title'], 'tokens' : doc_tokens})
        if i % 10000 == 0:
            print("以處理完成篇數：", i)
            
    print("處理完成總篇數：", len(res))

    json.dump(res,open(args.output_path + 'wiki_tokenize.json','w'))


if __name__ == '__main__':
    main()

        
                
