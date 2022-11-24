from typing import Dict, List

import pandas as pd


def _get_drugs_list(df: pd.DataFrame) -> List[str]:
    return [drug.lower() for drug in df.drug.unique().tolist()]


def initialize_reference(drugs: pd.DataFrame) -> Dict:
    unique_drugs_list = _get_drugs_list(drugs)
    return dict.fromkeys(unique_drugs_list, "")


def get_mentioned_drug_in_title(
    df: pd.DataFrame, title_column: str, drug: str
) -> List[Dict]:
    df_expected_for_reference = _get_df_for_reference(df, title_column, drug, False)
    return df_expected_for_reference.to_dict(orient="records")


def get_mentioned_drug_in_journal(
    clinical_trials_df: pd.DataFrame, pubmed_df: pd.DataFrame, drug: str
) -> List[Dict]:
    pubmed_journal = _get_df_for_reference(pubmed_df, "title", drug, True)
    clinical_trials_journal = _get_df_for_reference(
        clinical_trials_df, "scientific_title", drug, True
    )
    journal_df = pd.concat([pubmed_journal, clinical_trials_journal])[
        ["date", "journal"]
    ]
    return journal_df.to_dict(orient="records")


def _get_df_for_reference(
    df: pd.DataFrame, title_column: str, drug: str, column_journal: bool = False
) -> pd.DataFrame:
    column_reference = title_column
    if column_journal:
        column_reference = "journal"
    df[title_column] = df[title_column].apply(lambda x: x.lower())
    df = df[df[title_column].str.contains(drug)]
    df = df[["date", column_reference]]
    return df.drop_duplicates()


def create_reference(
    drugs: pd.DataFrame, pubmed_df: pd.DataFrame, clinical_trials_df: pd.DataFrame
) -> Dict:
    reference = initialize_reference(drugs)
    for drug in reference:
        reference[drug] = {
            "pubmed": get_mentioned_drug_in_title(pubmed_df, "title", drug),
            "clinical_trials": get_mentioned_drug_in_title(
                clinical_trials_df, "scientific_title", drug
            ),
            "journal": get_mentioned_drug_in_journal(
                clinical_trials_df, pubmed_df, drug
            ),
        }
    return reference
