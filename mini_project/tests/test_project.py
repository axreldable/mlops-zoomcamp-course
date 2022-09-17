from mini_project.project import get_name


def test_get_name():
    event = {
        "name": "name_value"
    }
    rez = get_name(event)

    expected_rez = "name_value"

    assert expected_rez == rez
