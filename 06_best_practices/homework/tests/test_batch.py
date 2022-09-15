from datetime import datetime

import pandas as pd
from batch import prepare_data
from deepdiff import DeepDiff


def test_prepare_data():
    def dt(hour, minute, second=0):
        return datetime(2021, 1, 1, hour, minute, second)

    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (1, 1, dt(1, 2, 0), dt(2, 2, 1)),
    ]
    columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
    df = pd.DataFrame(data, columns=columns)

    categorical = ['PUlocationID', 'DOlocationID']
    rez_df = prepare_data(df, categorical)
    print(rez_df)

    data = [
        ("-1", "-1", dt(1, 2), dt(1, 10), 8.0),
        ("1", "1", dt(1, 2), dt(1, 10), 8.0),
    ]
    columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime', 'duration']
    expected_df = pd.DataFrame(data, columns=columns)
    print(expected_df)

    diff = DeepDiff(rez_df.to_dict(), expected_df.to_dict(), significant_digits=1)
    print(f'diff={diff}')

    assert 'type_changes' not in diff
    assert 'values_changed' not in diff
