def get_name(event):
    return event["name"]


if __name__ == "__main__":
    print("Mini project is starting...")

    event = {
        "name": "name_value"
    }
    name = get_name(event)
    print("name", name)

    print("Mini project completed.")
