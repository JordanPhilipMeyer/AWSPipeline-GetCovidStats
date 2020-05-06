import requests
import json
import boto3

dynamodb = boto3.resource('dynamodb')
covid = dynamodb.Table('VAcovid')



def lambda_handler(event, context):
    # TODO implement

    url = 'https://www.vdh.virginia.gov/content/uploads/sites/182/2020/03/VDH-COVID-19-PublicUseDataset-Cases.csv'
    covidDataPull = requests.get(url, verify=False)
    data = covidDataPull.text
    adjusted =list(data.split("\r\n"))

    count =1 
    for item in adjusted:
        record = list(item.split(','))
        if len(record)==7:
            covid.put_item(
            Item = {"ID":str(count),
            "Date":record[0],
            "FIPS": record[1],
            "Locality":record[2],
            "VDH Health District":record[3],
            "Total Cases":record[4],
            "Hospitalizations":record[5],
            "Deaths":record[6]
            })
            count += 1
        else:
            continue
    


    return {
        'statusCode': 200,
        'body': {}
    }
