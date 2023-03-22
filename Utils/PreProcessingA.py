import os
import json
import pandas as pd

class Chatbot:
    def __init__(self):
        self.cur_path = os.path.abspath(os.path.curdir)
        self.data_path = os.path.join(self.cur_path, 'data')
        self.exceptKakao = os.path.join(self.data_path, 'BAND')

        
    def step1(self):
        for folder in self.exceptKakao:
            if not os.path.exists(folder):
                print("대화 데이터셋이 존재하지 않습니다. AI hub에서 데이터셋을 다운로드 받으십시오.")
                return
            
            else:
                print("데이터셋 파일 확인 완료")
                print("위치 : {0}".format(folder))
        
        print(folder)
            
    #     return self.deleteUselessFiles()

    
    # def deleteUselessFiles(self): 
    #     print("파일 확인 완료")
    #     return self.textInfo()

    # def textInfo(self):
    #     chatdata = []
    #     for folder in self.exceptKakao:
    #         json_file_list = os.listdir(folder)
    #         for i in range(len(json_file_list)):
    #             kakao_path_data_path = os.path.join(folder, json_file_list[i])
    #             with open(kakao_path_data_path, 'r', encoding='UTF-8') as f:
    #                 contents = json.load(f)
    #                 condition1 = contents['info'][0]['annotations']['speaker_type']
    #                 condition2 = contents['info'][0]['annotations']['lines'][1]['speaker']['sex']
    #                 condition3 = contents['info'][0]['annotations']['lines'][1]['speaker']['age']
    #                 condition4 = contents['info'][0]['annotations']['lines'][1]['speaker']['id']
    #                 # print(len(contents['info'][0]['annotations']['lines'][1]))

    #                 if condition1 == "1:1" and condition2 == "여성" and condition3 == "20대" and condition4 == "2번":
    #                     with open(kakao_path_data_path, 'r', encoding='UTF-8') as target_file:
    #                         for i in range(len(contents['info'][0]['annotations']['lines'])):
    #                             chatdata.append({'id': contents['info'][0]['annotations']['lines'][i]['id'],
    #                                         'text': contents['info'][0]['annotations']['lines'][i]['norm_text'],
    #                                         'sex': contents['info'][0]['annotations']['lines'][i]['speaker']['sex'],
    #                                         'age': contents['info'][0]['annotations']['lines'][i]['speaker']['age'],
    #                                         'class': contents['info'][0]['annotations']['lines'][i]['speaker']['id'],
    #                                         'file_name' : contents['info'][0]['title']})
    #     df = pd.DataFrame(chatdata)
    #     print("데이터프레임화 완료, 레코드 개수: {0}".format(len(df)))
    #     return self.req_resDataframe(df)
    
    # def req_resDataframe(self,df):
    #     result_df = pd.DataFrame(columns=['req', 'res'])

    #     for i in range(len(df)):
    #         if df['class'][i] == '1번':
    #             req = df['text'][i]
    #         if i+1 < len(df) and df['class'][i+1] == '2번':
    #             res = df['text'][i+1]
    #             if req in result_df['req'].values:
    #                 req_index = result_df[result_df['req'] == req].index[0]
    #                 result_df.at[req_index, 'res'] += '/' + res
    #             else:
    #                 result_df = result_df.append({'req': req, 'res': res}, ignore_index=True)
    #     print("질문/답변 변환 완료")
    #     return self.character_conversion(result_df)
    
    # def character_conversion(self, result_df):
    #     result_df['req'] = result_df['req'].str.replace("키키", "ㅋㅋ")
    #     result_df['res'] = result_df['res'].str.replace("키키", "ㅋㅋ")
    #     print("문자 변환 완료")
    #     return self.SpecialCharacterConversion(result_df)
    
    # def SpecialCharacterConversion(self, result_df):
    #     result_df = result_df[~result_df['req'].str.contains("\*")]
    #     result_df = result_df[~result_df['res'].str.contains("\*")]
    #     print("특수 문자 제거 완료")
    #     return self.save_csv(result_df)
    
    # def save_csv(self, result_df):
    #     result_df.to_csv('band.csv', index=False)
    #     print("데이터셋 저장 완료")




if __name__ == "__main__":
    starter = Chatbot()
    print(starter.step1())