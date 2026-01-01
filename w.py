import requests 
def send(url,title,discription,content):


    data = {
        "username" : "ClOUD Supporting 인증로그",
        "content" : content,
        
    }

    data["embeds"] = [
        {
            "description" : discription,
            "title" : title,
            "color": 7776511
    
        }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

