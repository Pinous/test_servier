import pandas as pd
import pytest


@pytest.fixture(name="correct_drugs")
def correct_drugs():
    df = pd.DataFrame(
        columns=["atccode", "drug"],
        data=[
            ["A04AD", "DIPHENHYDRAMINE"],
            ["S03AA", "TETRACYCLINE"],
            ["V03AB", "ETHANOL"],
            ["A03BA", "ATROPINE"],
            ["A01AD", "EPINEPHRINE"],
            ["6302001", "ISOPRENALINE"],
            ["R01AD", "BETAMETHASONE"],
        ],
    )
    return df


@pytest.fixture(name="correct_clinical_trials")
def correct_clinical_trials():
    df = pd.DataFrame(
        columns=["id", "scientific_title", "date", "journal"],
        data=[
            [
                "NCT01967433",
                "Use of Diphenhydramine as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids",
                "1 January 2020",
                "Journal of emergency nursing",
            ],
            [
                "NCT04189588",
                "Phase 2 Study IV QUZYTTIR™ (Cetirizine Hydrochloride Injection) vs V Diphenhydramine",
                "1 January 2020",
                "Journal of emergency nursing",
            ],
            ["NCT04237090", "  ", "1 January 2020", "Journal of emergency nursing"],
            [
                "NCT04237091",
                "Feasibility of a Randomized Controlled Clinical Trial Comparing the Use of Cetirizine to Replace Diphenhydramine in the Prevention of Reactions Related to Paclitaxel",
                "1 January 2020",
                "Journal of emergency nursing",
            ],
            [
                "NCT04153396",
                "Preemptive Infiltration With Betamethasone and Ropivacaine for Postoperative Pain in Laminoplasty or \\xc3\\xb1 Laminectomy",
                "1 January 2020",
                "Hôpitaux Universitaires de Genève",
            ],
            [
                "NCT03490942",
                "Glucagon Infusion in T1D Patients With Recurrent Severe Hypoglycemia: Effects on Counter-Regulatory Responses",
                "25/05/2020",
                "",
            ],
            [
                "",
                "Glucagon Infusion in T1D Patients With Recurrent Severe Hypoglycemia: Effects on Counter-Regulatory Responses",
                "25/05/2020",
                "Journal of emergency nursing",
            ],
            [
                "NCT04188184",
                "Tranexamic Acid Versus Epinephrine During Exploratory Tympanotomy",
                "27 April 2020",
                "Journal of emergency nursing\\xc3\\x28",
            ],
        ],
    )
    return df


@pytest.fixture(name="correct_pubmed")
def correct_pubmed():
    df = pd.DataFrame(
        columns=["id", "title", "date", "journal"],
        data=[
            [
                1,
                "A 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations",
                "01/01/2019",
                "Journal of emergency nursing",
            ],
            [
                2,
                "An evaluation of benadryl, pyribenzamine, and other so-called diphenhydramine antihistaminic drugs in the treatment of allergy.",
                "01/01/2019",
                "Journal of emergency nursing",
            ],
            [
                3,
                "Diphenhydramine hydrochloride helps symptoms of ciguatera fish poisoning.",
                "02/01/2019",
                "The Journal of pediatrics",
            ],
            [
                4,
                "Tetracycline Resistance Patterns of Lactobacillus buchneri Group Strains.",
                "01/01/2020",
                "Journal of food protection",
            ],
            [
                5,
                "Appositional Tetracycline bone formation rates in the Beagle.",
                "02/01/2020",
                "American journal of veterinary research",
            ],
            [
                6,
                "Rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.",
                "2020-01-01",
                "Psychopharmacology",
            ],
            [
                7,
                "The High Cost of Epinephrine Autoinjectors and Possible Alternatives.",
                "01/02/2020",
                "The journal of allergy and clinical immunology. In practice",
            ],
            [
                8,
                "Time to epinephrine treatment is associated with the risk of mortality in children who achieve sustained ROSC after traumatic out-of-hospital cardiac arrest.",
                "01/03/2020",
                "The journal of allergy and clinical immunology. In practice",
            ],
        ],
    )
    return df
