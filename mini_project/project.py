import base64
import json


def get_name(event):
    return event["name"]


def base64_decode(encoded_data):
    decoded_data = base64.b64decode(encoded_data).decode("utf-8")
    json_event = json.loads(decoded_data)
    return json_event


def lambda_handler(event):
    print(json.dumps(event))

    result = []

    for record in event["Records"]:
        encoded_data = record["kinesis"]["data"]
        json_event = base64_decode(encoded_data)

        print(json_event)
        name = get_name(json_event)
        result.append(name)

    return {
        "result": result
    }


if __name__ == "__main__":
    print("Mini project is starting...")

    event = {
        "name": "name_value"
    }
    name = get_name(event)
    print("name", name)

    print("Mini project completed.")
