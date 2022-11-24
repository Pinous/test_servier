import datetime
from typing import List

from pydantic import BaseModel


class Drugs(BaseModel):
    atccode: str
    drug: str


class DfDrugs(BaseModel):
    df_dict: List[Drugs]


class Pubmed(BaseModel):
    id: int
    title: str
    date: datetime.date
    journal: str


class DfPubmed(BaseModel):
    df_dict: List[Pubmed]


class ClinicalTrials(BaseModel):
    id: str
    scientific_title: str
    date: datetime.date
    journal: str


class DfClinicalTrials(BaseModel):
    df_dict: List[ClinicalTrials]
