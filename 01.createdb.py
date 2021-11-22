from azure.cosmos import CosmosClient,exceptions
import os

url=os.environ["ACCOUNT_URI"]
key=os.environ["ACCOUNT_KEY"]

client=CosmosClient(url,credential=key)
print("client prepared...")
database_name="db1031"
try:
    database=client.create_database(database_name)
    print("Created Database")
except exceptions.CosmosResourceExistsError:
    database=client.get_database_client(database_name)
    print("Picking Existing database with same name")
