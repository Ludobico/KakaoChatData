import os
import json
import pandas as pd

def LlamaActorDataset():
    cur_path = os.path.abspath(os.path.curdir)
    csv_path = os.path.join(cur_path, 'KakaoData.csv')

    df = pd.read_csv(csv_path)

    text_list = []

    for index, row in df.iterrows():
        items = {}
        items['user_input'] = row['req']
        items['completion'] = row['res']

        text_list.append(items)
    
    with open('LllamaJsonData.json', 'w', encoding='UTF-8') as f:
        json.dump(text_list, f,ensure_ascii=False)



if __name__ == "__main__":
    LlamaActorDataset()