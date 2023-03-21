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
PPO를 고려하지 않은 데이터셋이기에 **score** 는 고려하지 않았습니다.

<img width="2048" height="340" alt="image" src="https://user-images.githubusercontent.com/89598307/225176113-0927ce44-6f01-4eee-86d1-a5a11248d352.png">
