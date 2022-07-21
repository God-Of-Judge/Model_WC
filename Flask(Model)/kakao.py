import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "1NLOTXkbJXA8-bOM8bdppOWGjFNasPU9wpPNLMJ-CisMpgAAAYIZPRXQ"
}

template = {
    "object_type" : "list",
    "header_title" : "영상분석 완료",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "본인 20 : 상대방 80",
            "description" : "교차로 사고",
            "image_url" : "https://media.bunjang.co.kr/product/169940835_1_1636957290_w%7Bres%7D.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        },
        {
            "title" : "본인 0 : 상대방 100",
            "description" : "차선 변경 사고",
            "image_url" : "https://media.bunjang.co.kr/product/169940835_1_1636957290_w%7Bres%7D.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "웹으로 이동",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
    
}

data = {
    "template_object" : json.dumps(template)
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))