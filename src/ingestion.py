import logging

import pandas as pd
import yaml as yaml
from yaml import SafeLoader

from src.schema.schema import Drugs, DfDrugs
from src.schema.schema import DfDrugs, DfPubmed

def _id_null_string(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[4, 'id'] = 13
    df['id'] = df['id'].astype('int')
    return df

def transform_date_column_into_datetime(df: pd.DataFrame) -> pd.DataFrame:
    if "date" in df.columns:
        df['date'] = pd.to_datetime(df["date"])
    return df

def replace_nan_by_empty_string(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna("")

def clean_df_for_specific_needs(df: pd.DataFrame, id_issue: bool = False) -> pd.DataFrame:
    df_final = transform_date_column_into_datetime(df)
    df_final = replace_nan_by_empty_string(df_final)
    if id_issue:
        df_final = _id_null_string(df_final)
    return df_final


def transform_into_df_input_file(input_file: str) -> pd.DataFrame:
    logging.info("Pre Processing : Transform file to df")
    if input_file.endswith('.json'):
        with open(input_file) as json_f:
            result = yaml.load(json_f, Loader=SafeLoader)
            df = pd.DataFrame(result)
            df = clean_df_for_specific_needs(df, True)
            return df
    df = pd.read_csv(input_file)
    df = clean_df_for_specific_needs(df)
    return df

if __name__ == "__main__":
    file = "/Users/SF5966@engie.com/Documents/affiliation/test_servier/src/data/clinical_trials.csv"
    df = transform_into_df_input_file(file)
    print(DfDrugs(df_dict=df.to_dict(orient="records")))
