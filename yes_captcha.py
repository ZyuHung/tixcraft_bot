import requests

API_KEY = "a977c568fd3e3c4af4cd0f9d1a986c2a0244b2d426469"


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
