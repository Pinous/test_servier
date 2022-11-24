from src.processing import (
    create_reference,
    get_mentioned_drug_in_journal,
    get_mentioned_drug_in_title,
    initialize_reference,
)


def test_should_return_initiate_reference(correct_drugs):
    expected_refrence = {
        "atropine": "",
        "betamethasone": "",
        "diphenhydramine": "",
        "epinephrine": "",
        "ethanol": "",
        "isoprenaline": "",
        "tetracycline": "",
    }
    assert initialize_reference(correct_drugs) == expected_refrence


def test_should_return_list_of_date_and_title_for_the_drug_diphenhydramine(
    correct_clinical_trials,
):
    expected_list = [
        {
            "date": "1 January 2020",
            "scientific_title": "use of diphenhydramine as an adjunctive sedative for colonoscopy in patients chronically on opioids",
        },
        {
            "date": "1 January 2020",
            "scientific_title": "phase 2 study iv quzyttir™ (cetirizine hydrochloride injection) vs v diphenhydramine",
        },
        {
            "date": "1 January 2020",
            "scientific_title": "feasibility of a randomized controlled clinical trial comparing the use of cetirizine to replace diphenhydramine in the prevention of reactions related to paclitaxel",
        },
    ]
    assert (
        get_mentioned_drug_in_title(
            correct_clinical_trials, "scientific_title", "diphenhydramine"
        )
        == expected_list
    )


def test_should_return_list_of_date_and_title_for_the_drug_diphenhydramine_dataframe_pubmed(
    correct_pubmed,
):
    expected_list = [
        {
            "date": "01/01/2019",
            "title": "a 44-year-old man with erythema of the face diphenhydramine, neck, "
            "and chest, weakness, and palpitations",
        },
        {
            "date": "01/01/2019",
            "title": "an evaluation of benadryl, pyribenzamine, and other so-called "
            "diphenhydramine antihistaminic drugs in the treatment of allergy.",
        },
        {
            "date": "02/01/2019",
            "title": "diphenhydramine hydrochloride helps symptoms of ciguatera fish "
            "poisoning.",
        },
    ]
    assert (
        get_mentioned_drug_in_title(correct_pubmed, "title", "diphenhydramine")
        == expected_list
    )


def test_should_return_journal_for_drug_diphenhydramine_dataframe(
    correct_clinical_trials, correct_pubmed
):
    expected_ref = [
        {"date": "01/01/2019", "journal": "Journal of emergency nursing"},
        {"date": "02/01/2019", "journal": "The Journal of pediatrics"},
        {"date": "1 January 2020", "journal": "Journal of emergency nursing"},
    ]
    assert (
        get_mentioned_drug_in_journal(
            correct_clinical_trials, correct_pubmed, "diphenhydramine"
        )
        == expected_ref
    )


def test_should_return_full_reference_for_diphenhydramine(
    correct_drugs, correct_pubmed, correct_clinical_trials
):
    correct_drugs_diphenhydramine = correct_drugs[0:1]
    expected_reference = {
        "diphenhydramine": {
            "clinical_trials": [
                {
                    "date": "1 January 2020",
                    "scientific_title": "use of "
                    "diphenhydramine "
                    "as an "
                    "adjunctive "
                    "sedative for "
                    "colonoscopy in "
                    "patients "
                    "chronically on "
                    "opioids",
                },
                {
                    "date": "1 January 2020",
                    "scientific_title": "phase 2 study "
                    "iv quzyttir™ "
                    "(cetirizine "
                    "hydrochloride "
                    "injection) vs v "
                    "diphenhydramine",
                },
                {
                    "date": "1 January 2020",
                    "scientific_title": "feasibility of "
                    "a randomized "
                    "controlled "
                    "clinical trial "
                    "comparing the "
                    "use of "
                    "cetirizine to "
                    "replace "
                    "diphenhydramine "
                    "in the "
                    "prevention of "
                    "reactions "
                    "related to "
                    "paclitaxel",
                },
            ],
            "journal": [
                {"date": "01/01/2019", "journal": "Journal of emergency nursing"},
                {"date": "02/01/2019", "journal": "The Journal of pediatrics"},
                {"date": "1 January 2020", "journal": "Journal of emergency nursing"},
            ],
            "pubmed": [
                {
                    "date": "01/01/2019",
                    "title": "a 44-year-old man with erythema of "
                    "the face diphenhydramine, neck, and "
                    "chest, weakness, and palpitations",
                },
                {
                    "date": "01/01/2019",
                    "title": "an evaluation of benadryl, "
                    "pyribenzamine, and other so-called "
                    "diphenhydramine antihistaminic "
                    "drugs in the treatment of allergy.",
                },
                {
                    "date": "02/01/2019",
                    "title": "diphenhydramine hydrochloride helps "
                    "symptoms of ciguatera fish "
                    "poisoning.",
                },
            ],
        }
    }
    assert (
        create_reference(
            correct_drugs_diphenhydramine, correct_pubmed, correct_clinical_trials
        )
        == expected_reference
    )
