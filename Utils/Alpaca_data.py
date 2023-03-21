import os
import json
import pandas as pd

def AlpacaDataset():
    cur_path = os.path.abspath(os.path.curdir)
    csv_path = os.path.join(cur_path, 'KakaoData.csv')

    df = pd.read_csv(csv_path)

    text_list = []

    for index, row in df.iterrows():
        items = {}
        items['instruction'] = row['req']
        items['input'] = ""
        items['output'] = row['res']

        text_list.append(items)
    
    with open('alpaca_data.json', 'w', encoding='UTF-8') as f:
        json.dump(text_list, f,ensure_ascii=False, indent=4)
    
    print("json 파일 변환 완료")



if __name__ == "__main__":
    AlpacaDataset()