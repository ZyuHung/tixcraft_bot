import requests

API_KEY = "2b9565e3861dd674d6cc3de7ad0c2fe69a43e15d26469"


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
