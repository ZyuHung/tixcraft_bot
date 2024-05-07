import requests

API_KEY = "9dee83f6880892820b744ae6204b432c86d30a2026469"


def image_to_text(base64):
    register_url = "https://api.yescaptcha.com/createTask"
    # 添加请求头，需要就传
    header = {
        "Content-Type": "application/json"
    }

    # json类型的参数
    json = {
        "clientKey": API_KEY,
        "task": {
            "type": "ImageToTextTaskTest",
            "body": base64
        }
    }
    # 发送post请求
    response = requests.post(url=register_url, json=json, headers=header)
    result = response.json()
    if result["errorId"] == 0:
        ocr_result = result["solution"]["text"]
        print("YesCaptcha Result:", ocr_result)
        return ocr_result
    else:
        print("YesCaptcha Error:", result)
    return None


if __name__ == "__main__":
    image_to_text("aa")
