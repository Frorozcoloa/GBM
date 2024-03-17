import pandas as pd
import numpy as np
from pathlib import Path
from feature_engeenier import q25, q50, q75, read_df, pretransform_peridoc, transform_peridic, transform_date, transform_tran_amount, create_target, dropdataset, extract_feature

def test_q25():
    df = pd.DataFrame({'tran_amount': [100, 200, 150, 300]})
    result = q25(df['tran_amount'])
    assert result ==  137.5

def test_q50():
    df = pd.DataFrame({'tran_amount': [100, 200, 150, 300]})
    result = q50(df['tran_amount'])
    assert result == 175.0

def test_q75():
    df = pd.DataFrame({'tran_amount': [100, 200, 150, 300]})
    result = q75(df['tran_amount'])
    assert result == 225.0


def test_pretransform_peridoc():
    df = pd.DataFrame({
        'trans_date': pd.date_range(start='2023-01-01', periods=5),
        'weekday_sin': [0.1, 0.2, 0.3, 0.4, 0.5],
        'weekday_cos': [-0.1, -0.2, -0.3, -0.4, -0.5]
    })
    result = pretransform_peridoc(df)
    assert 'weekday_sin' in result.columns
    assert 'weekday_cos' in result.columns

def test_transform_peridic():
    df = pd.DataFrame({
        'customer_id': [1, 1, 2, 2],
        'weekday_sin': [0.1, 0.2, 0.3, 0.4],
        'weekday_cos': [-0.1, -0.2, -0.3, -0.4]
    })
    result = transform_peridic(df)
    assert 'customer_id' in result.columns
    assert 'weekday_sin_mean' in result.columns
    assert 'weekday_cos_std' in result.columns

def test_transform_date():
    df = pd.DataFrame({
        'customer_id': [1, 1, 2, 2],
        'trans_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'])
    })
    result = transform_date(df)
    assert 'customer_id' in result.columns
    assert 'trans_date_std' in result.columns
    assert 'trans_date_range' in result.columns

def test_transform_tran_amount():
    df = pd.DataFrame({
        'customer_id': [1, 1, 2, 2],
        'tran_amount': [100, 200, 150, 300]
    })
    result = transform_tran_amount(df)
    assert 'customer_id' in result.columns
    assert 'tran_amount_min' in result.columns
    assert 'tran_amount_mean' in result.columns

def test_create_target():
    df = pd.DataFrame({
        'customer_id': [1, 1, 2, 2],
        'tran_amount': [100, 200, 150, 300]
    })
    result = create_target(df)
    assert 'customer_id' in result.columns
    assert 'type_consumer' in result.columns

def test_dropdataset():
    df = pd.DataFrame({
        'customer_id': [1, 1, 2, 2],
        'weekday_sin_mean': [0.1, 0.2, 0.3, 0.4]
    })
    result = dropdataset(df)
    assert 'customer_id' not in result.columns
