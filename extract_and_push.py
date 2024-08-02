import requests
import csv
from google.cloud import storage

# replace with your own api
url = ""

querystring = {"formatType":""} # (odi,test)

headers = {
	"x-rapidapi-key": "",
	"x-rapidapi-host": ""
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

if response.status_code == 200:
    data = response.json().get('rank',[])
    csv_filename = "batsmen_ranking.csv"

    if data:
        field_names = ['rank', 'name', 'country']

        with open(csv_filename,'w',newline='',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=field_names)
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})
        
        print(f"data fetched successfully and writer ti '{csv_filename}'")

        bucket_name = 'bkt-iccranking-data'
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"FIle {csv_filename} uploaded to gcs bucket {bucket_name} as {destination_blob_name}")
    else:
        print("data not avaialble from api")
else:
    print("failed to fetched the data",response.status_code)  