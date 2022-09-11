import json
import base64
import boto3

kinesis_client = boto3.client('kinesis')

def prepare_features(ride):
    features = {}
    features["PU_DO"] = "%s_%s" % (ride["PULocationID"], ride["DOLocationID"])
    features["trip_distance"] = ride["trip_distance"]

    return features

def predict(features):
    return 10.0

def lambda_handler(event, context):
    print(json.dumps(event))
    
    predictions = []
    for record in event['Records']:
        encoded_data = record['kinesis']['data']
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        ride_event = json.loads(decoded_data)
        print(ride_event)
        
        features = prepare_features(ride_event['ride'])
        prediction = predict(features)
        
        prediction_event = {
            'model': 'ride_duration_model',
            'versio': '123',
            'prediction': {
                'ride_duration': prediction,
                'ride_id': ride_event['ride_id']
            }
        }
        
        predictions.append(prediction_event)
        
        kinesis_client.put_record(
            StreamName='ride_predictions',
            Data=json.dumps(prediction_event),
            PartitionKey=str(ride_event['ride_id'])
        )
        
    
    
    return {
        'predictions': predictions
    }
