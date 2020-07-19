import json
from tqdm import tqdm
import argparse


def main():
    parser = argparse.ArgumentParser()
    
    # Required parameters
    parser.add_argument("--file_path", default='./wiki_tokenize.json', type=str, required=False, help="wiki file path")
    parser.add_argument("--output_path", default='./', type=str, required=False, help="output path") 

	with open(args.file_path) as file:
		data = json.load(file)

	res = ''
	for doc in tqdm(data):
		for sent_tokens in doc['tokens']:
			for ele in sent_tokens:
				res += ele[0] + ' '

		res += '\n'

	with open(args.output_path + 'wiki_word2vec_data.txt','w') as file:
		file.write(res)


if __name__ == '__main__':
	main()