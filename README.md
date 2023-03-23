# KakaoData
총 73000여개의 질문/답변 데이터셋입니다.

AI Hub에 있는 일상 대화 데이터셋을 정재하였고, NLP, Chatbot 제작에 사용할 수 있습니다.
질문 및 답변이 2개 이상인 경우 "/" 로 나누어놨습니다.

```
오 이거 용량이 작나?/나 다 깔렸어 들어와
```

답변의 경우 20대 여성을 기준으로 1:1 대화만 추출했습니다.

코드로 작성한거라 질문/답변이 부정확할수있습니다.

개인정보가 포함된 대화는 삭제하였고, 몇몇 문자는 변경하였습니다.(키키 -> ㅋㅋ)


<img width="856" alt="image" src="https://user-images.githubusercontent.com/89598307/224911500-feb8c7a2-9b69-4e67-ae46-50da1ab6212a.png">

# LlamaJsonData
Llama에 학습시키기 적합한 데이터셋 형식으로 변환한 json 파일입니다.

**req** 와 **res**에 대응되는 키값으로 각각 **user_input** , **completion** 가 할당되었습니다.

<img width="982" alt="image" src="https://user-images.githubusercontent.com/89598307/226497929-53078097-f1b1-4230-a195-3a03078311b6.png">

# alpaca_data
Llama 모델기반 스탠퍼드 대학교에서 제작한 Alpaca 데이터셋에 맞춰 변형하였습니다.

Llama와 크게 다른점은 없습니다.

* alpaca_data_CRLF.json : 윈도우 json 줄 바꿈입니다.

* alpaca_data_LF.json : 리눅스 json 줄 바꿈입니다.
<!--
<img width="983" alt="image" src="https://user-images.githubusercontent.com/89598307/226498183-8282e516-e5b3-4a36-8426-d9414664fe0f.png">

학습시키기 위한 VRAM 용량입니다.

<img width="580"  alt="llama-7b_vram_batch_128" src="https://user-images.githubusercontent.com/89598307/226541632-807a0c00-8ae8-407d-a871-ea74aa87e8a6.png">

* 배치 사이즈 : 128

<img width="580" alt="llama-7b_vram_batch_256" src="https://user-images.githubusercontent.com/89598307/226541667-57296efe-1625-4c8c-b169-e188365205ab.png">

* 배치 사이즈 : 256

<img width="580" alt="time_of_1_epoch" src="https://user-images.githubusercontent.com/89598307/226541686-14268bd4-227a-4d4f-a808-7b406dfb853b.png">

* 1epoch 시간
-->
# Alldata
카카오톡, 페이스북, 인스타그램, 밴드, 네이트온에 있는 채팅데이터를 하나로 모은 데이터셋 파일입니다.

크기는 총 88974개로

카카오톡에 비해 약 15000개정도 늘었습니다.
