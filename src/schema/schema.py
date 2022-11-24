import datetime

from pydantic import BaseModel

class Drugs(BaseModel):
    IdDrugs: str
    Drug: str


class Pubmed(BaseModel):
    IdPubmed: int
    Title: str
    Date: datetime.date
    Journal: str


class ClinicalTrials(BaseModel):
    IdClinicalTrials: str
    ScientificTitle: str
    Date: datetime.date
    Journal: str

