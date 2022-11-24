import json
import os
from typing import Dict

import pandas as pd

from src.ingestion import Ingestion
from src.processing import create_reference
from src.schema.schema import DfClinicalTrials, DfDrugs, DfPubmed


class Pipeline:
    def __init__(self, config: Dict):
        self.drugs_filename = config["drugs_filename"]
        self.pubmed_csv_filename = config["pubmed_csv_filename"]
        self.pubmed_json_filename = config["pubmed_json_filename"]
        self.clinical_trials_filename = config["clinical_trials_filename"]

    def load_df(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        df_drugs = Ingestion(self.drugs_filename, DfDrugs).load_valided_df()
        df_pubmed_csv = Ingestion(self.pubmed_csv_filename, DfPubmed).load_valided_df()
        df_pubmed_json = Ingestion(
            self.pubmed_json_filename, DfPubmed
        ).load_valided_df()
        df_pubmed = pd.concat([df_pubmed_csv, df_pubmed_json], ignore_index=True)
        clinical_trials = Ingestion(
            self.clinical_trials_filename, DfClinicalTrials
        ).load_valided_df()
        return df_drugs, df_pubmed, clinical_trials

    def execute(self) -> str:
        df_drugs, df_pubmed, clinical_trials = self.load_df()
        reference = create_reference(df_drugs, df_pubmed, clinical_trials)
        return json.dumps(reference, indent=4, sort_keys=True, default=str)


if __name__ == "__main__":
    config = {
        "drugs_filename": os.path.realpath("data/") + "/drugs.csv",
        "pubmed_csv_filename": os.path.realpath("data/") + "/pubmed.csv",
        "pubmed_json_filename": os.path.realpath("data/") + "/pubmed.json",
        "clinical_trials_filename": os.path.realpath("data/") + "/clinical_trials.csv",
    }
    pipeline = Pipeline(config)
    print(pipeline.execute())
