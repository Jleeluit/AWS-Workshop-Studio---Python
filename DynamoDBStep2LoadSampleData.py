import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )

#In the Cloud9 terminal use the following command to download the moviedata.zip
#wget https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/moviedata.zip

#Use the following command extract the data file (moviedata.json)
#unzip moviedata.zip


#To run the program, enter the following command.
#python MoviesLoadData.py
