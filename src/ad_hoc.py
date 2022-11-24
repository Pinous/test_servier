import pandas as pd


def get_journal_from_json_output_with_the_most_drugs_mentioned() -> str:
    df = pd.read_json("src/json_expected/drug.json")
    journaux_dict = {}
    for journal_name, row in df.T["journal"].iteritems():
        journaux = list(set([f["journal"] for f in row]))
        for journal in journaux:
            if journal == "Journal of emergency nursing\\xc3\\x28":
                journal = "Journal of emergency nursing\\xc3\\x28".replace(
                    "\\xc3\\x28", ""
                )
            if journal not in journaux_dict:
                journaux_dict[journal] = 1
            else:
                journaux_dict[journal] = journaux_dict[journal] + 1
    return sorted(journaux_dict.items(), key=lambda x: x[1])[-1][0]
