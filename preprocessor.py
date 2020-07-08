import pandas as pd
import json

def preprocessJson(path):
    fil=open(path,'r',encoding='utf-8')
    stringDicts=fil.read().splitlines()
    dicts={}
    keys=['id','conversation_id','created_at','date','time','timezone','user_id','username','name','place',
    'tweet','hashtags','retweet','near','geo']
    temp=json.loads(stringDicts[0])
    for k in keys:
        dicts[k]=[temp[k]]    
    for i in range(1,len(stringDicts)):
        temp=json.loads(stringDicts[i])    
        for k in keys:
            dicts[k].append(temp[k])

    df=pd.DataFrame(dicts)
    df.to_csv(f'preprocess_{path[:-5]}.csv')

def checkRetweet(pathCSV):
    df=pd.read_csv(pathCSV)
    if np.sum(df.loc[:,'retweet']!=False)!=0:
        df=df[df.retweet!=False]
        df.to_csv(pathCSV)


# preprocessJson("psychotherapy_2020.json")
# checkRetweet("preprocess_psychotherapy_2020.csv")