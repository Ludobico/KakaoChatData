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
        items['instruction'] = str(row['req'])
        items['input'] = str("")
        items['output'] = str(row['res'])

        text_list.append(items)
    
    # / 치환
    # for i in range(len(text_list)):
    #     text_list[i]['instruction'] = text_list[i]['instruction'].replace('/', '\n')
    #     text_list[i]['output'] = text_list[i]['output'].replace('/', '\n')
    #     text_list[i]['input'] = text_list[i]['input'].replace('/', '\n')
    
    with open('alpaca_data_CRLF.json', 'w', encoding='UTF-8') as f:
        json.dump(text_list, f,ensure_ascii=False, indent=4)
    
    with open('alpaca_data_LF.json', 'w', encoding='UTF-8',newline='\n') as g:
        json.dump(text_list, g,ensure_ascii=False, indent=4)
    
    print("json 파일 변환 완료")



if __name__ == "__main__":
    AlpacaDataset()