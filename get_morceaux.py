import boto3
from collections import defaultdict

session = boto3.Session()

# Initialisation du client DynamoDB
dynamodb_client = session.client('dynamodb')

def get_morceaux():
    # Utilisation de defaultdict pour stocker les éléments en fonction de leur type
    items = defaultdict(list)
    
    # Scan de la table pour récupérer tous les éléments
    response = dynamodb_client.scan(TableName='morceaux-caco')
    data = response['Items']
    
    # Ajout des éléments aux listes correspondant à leur type
    for item in data:
        type = item['type']['S']
        items[type].append(item['long_name']['S'])
    
    # Pagination en cas de résultat trop volumineux
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data = response['Items']
        
        for item in data:
            type = item['type']['S']
            items[type].append(item['long_name']['S'])
    
    return items

# Appel de la fonction
items = get_morceaux()

for debut in items['debut']:
    print(f"{debut}")