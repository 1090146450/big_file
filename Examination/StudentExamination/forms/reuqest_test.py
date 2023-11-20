import json

import requests
import datetime, re


def get_kd(dh):
    params = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "17token": "6AFA3318BFD3451E0B30D95677C2F430",
    }
    data = [
        {
            'number': f'{dh}',
        }
    ]
    # 注册
    # request = requests.post(url=f"https://api.17track.net/track/v2/register",headers=params,json=data)
    # 获取注册列表
    # request = requests.request("POST", "https://api.17track.net/track/v2/gettracklist", headers=params)
    # 进行推送
    # request = requests.post(url="https://api.17track.net/track/v2.2/push",headers=params,json=data)
    # 获取详情
    request = requests.post(url="https://api.17track.net/track/v2.2/gettrackinfo", json=data, headers=params)
    # print(request.text)
    return json.loads(request.text)


data = get_kd("JDX020948274499")




data = data["data"]["track_info"]["tracking"]["providers"][0]["events"]
data_dict ={}
for i in range(len(data)):
    data_dict[data[i]["time_raw"]["date"]+"_"+data[i]["time_raw"]["time"]] = data[i]["description"]+" "+data[i]["location"]
print(data_dict)
