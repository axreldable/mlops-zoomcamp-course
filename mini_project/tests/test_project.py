from mini_project.project import get_name, base64_decode, lambda_handler


def test_get_name():
    event = {
        "name": "name_value"
    }
    rez = get_name(event)

    expected_rez = "name_value"

    assert expected_rez == rez


def test_base64_decode():
    data = "ewogICAgICAgICJuYW1lIjogIm5hbWVfdmFsdWUiCiB9"

    rez = base64_decode(data)

    expected_rez = {
        "name": "name_value"
    }

    assert expected_rez == rez


def test_lambda_handler():
    event = {
        "Records": [
            {
                "kinesis": {
                    "data": "ewogICAgICAgICJuYW1lIjogIm5hbWVfdmFsdWUiCiB9"
                }
            }
        ]
    }

    rez = lambda_handler(event)

    expected_rez = {
        "result": ["name_value"]
    }

    assert expected_rez == rez
