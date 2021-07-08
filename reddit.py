import requests
import json 


def format_d(timestep_ob):
    from datetime import datetime
    dtobj= datetime.fromtimestamp(timestep_ob)
    return str(dtobj)

def get_data(url):
    response = requests.get(url,headers={'user-agent':'your bot 0.1'})

    python_obj= json.loads(response.text)
    news= python_obj['data']['children']
    filter_data=[]
    num=1
    for new in news:
        news_data={
            f'news #{num}':{
                'title':new['data']['title'],
                'author':new['data']['author'],
                'created': format_d(new['data']['created'])
            }
        } 
        filter_data.append(news_data)
        num+=1
    return filter_data

def write_json(data):
    with open('Redditnews.json','w') as jfile:
        json.dump(data,jfile,indent=4)
    

def main (url):
    data = get_data(url)
    write_json(data)


main('https://www.reddit.com/r/entertainment/.json')
