import pandas as pd
from src.data_processor import process_data

def test_process_data():
    df = pd.DataFrame({
        "name": ["A", "B", "B"],
        "salary": [1000, 2000, 2000]
    })

    result = process_data(df)
    assert result is not None
