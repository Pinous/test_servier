import os
import pytest

from src.preprocess import transform_into_df_input_file
from src.schema.schema import DfDrugs, DfPubmed, DfClinicalTrials


@pytest.mark.parametrize("filename,lenght", [("/drugs.csv", 7), ("/pubmed.csv", 8), ("/clinical_trials.csv", 8)])
def test_should_return_dataframe_when_input_is_a_csv(filename, lenght):
    csv_path = os.path.realpath("test/data/") + filename
    assert len(transform_into_df_input_file(csv_path)) == lenght

def test_should_return_dataframe_when_input_is_a_json():
    json_path = os.path.realpath("test/data/") + "/pubmed.json"
    assert len(transform_into_df_input_file(json_path)) == 5

def test_should_return_validated_model_Drugs():
    file = os.path.realpath("test/data/") + "/drugs.csv"
    df = transform_into_df_input_file(file)
    assert DfDrugs(df_dict=df.to_dict(orient="records"))

def test_should_return_validated_model_pubmed():
    file = os.path.realpath("test/data/") + "/pubmed.csv"
    df = transform_into_df_input_file(file)
    assert DfPubmed(df_dict=df.to_dict(orient="records"))

def test_should_return_validated_model_pubmed_json():
    file = os.path.realpath("test/data/") + "/pubmed.json"
    df = transform_into_df_input_file(file)
    assert DfPubmed(df_dict=df.to_dict(orient="records"))

def test_should_return_validated_model_clinical_trials():
    file = os.path.realpath("test/data/") + "/clinical_trials.csv"
    df = transform_into_df_input_file(file)
    assert DfClinicalTrials(df_dict=df.to_dict(orient="records"))
