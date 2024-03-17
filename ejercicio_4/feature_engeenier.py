import pandas as pd
import numpy as np
from pathlib import Path


def q25(x: pd.Series) -> float:
    return x.quantile(0.25)

def q50(x: pd.Series) -> float:
    return x.quantile(0.5)

def q75(x: pd.Series) -> float:
    return x.quantile(0.75)



def read_df() -> pd.DataFrame:
    path = Path(__file__).parent/"data_customer_classification 1.xlsx"
    df = pd.read_excel(path)
    return df

def pretransform_peridoc(df: pd.DataFrame) -> pd.DataFrame:
    cycle = 7
    df["trans_date"] = pd.to_datetime(df["trans_date"])
    df["weekday_sin"] = np.sin(2 * np.pi * df["trans_date"].dt.dayofweek / cycle)
    df["weekday_cos"] = np.cos(2 * np.pi *  df["trans_date"].dt.dayofweek / cycle)
    return df

def transform_peridic(df:pd.DataFrame) -> pd.DataFrame:
    results_weekday = df.groupby(["customer_id"])[["weekday_sin", "weekday_cos"]].agg(
        [("mean", "mean"), ("std", "std"), ("q25", q25),
        ("q50", q50), ("q75", q75),
        ]
    )
    results_weekday.columns = ["_".join(x) for x in results_weekday.columns.ravel()]
    results_weekday = results_weekday.reset_index()
    return results_weekday

def transform_date(df: pd.DataFrame) -> pd.DataFrame:
    result_trans_date = df.groupby(["customer_id"])["trans_date"].agg(["min", "std", "max"])
    result_trans_date["range"] = (result_trans_date["max"] - result_trans_date["min"]) / np.timedelta64(1, 'D')
    result_trans_date["std"] = result_trans_date["std"] / np.timedelta64(1, 'D')
    result_trans_date.drop(["min", "max"], axis=1, inplace=True)

    result_trans_date.columns = ["trans_date_"+x for x in result_trans_date.columns]
    result_trans_date = result_trans_date.reset_index()
    return result_trans_date

def transform_tran_amount(df: pd.DataFrame) -> pd.DataFrame:
    result_tran_amount = df.groupby(["customer_id"])["tran_amount"].agg(["min", "std", "max", "mean"])
    result_tran_amount.columns = ["tran_amount_"+x for x in result_tran_amount.columns]
    result_tran_amount = result_tran_amount.reset_index()
    return result_tran_amount

def create_target(df: pd.DataFrame) -> pd.DataFrame:
    count_tran = df.groupby(["customer_id"])["tran_amount"].count().reset_index().rename(columns={"tran_amount": "count"})
    q75 = count_tran["count"].quantile(0.75)
    q25 = count_tran["count"].quantile(0.25)

    count_tran["type_consumer"] = np.where(count_tran["count"] > q75, 2, np.where(count_tran["count"] < q25, 0, 1))
    return count_tran

def dropdataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(["customer_id"], axis=1)
    return df


def extract_feature():
    df = read_df()
    df = pretransform_peridoc(df)
    result_per = transform_peridic(df)
    result_date = transform_date(df)
    result_tran = transform_tran_amount(df)
    result_target = create_target(df)
    new_df = pd.concat([result_per, result_date, result_tran, result_target], axis=1)
    new_df = dropdataset(new_df)
    return new_df

if __name__ == "__main__":
    extract_feature()
    
    