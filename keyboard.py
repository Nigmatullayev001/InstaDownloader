import requests


def video_downloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "b53bf27ebdmshab5fa2210825e24p136077jsne9fb82b53f47",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # json_data = json.loads(response.text)
    dict1 = {}
    if response.json()['Type'] == 'Post-Image':
        dict1['type'] = "image"
        dict1['media'] = response.json()['media']
        return dict1
    if response.json()['Type'] == 'Post-Video':
        dict1['type'] = "video"
        dict1['media'] = response.json()['media']
        return dict1
    if response.json()['Type'] == 'Carousel':
        dict1['type'] = "carousel"
        dict1['media'] = response.json()['media']
        return dict1
    return response.json()


# print(video_downloader(
#     link="https://www.instagram.com/p/C6EcQJLtDte/?utm_source=ig_web_button_share_sheet"))
# print(video(link="https://www.instagram.com/p/C6_mkPCtAjI/"))
