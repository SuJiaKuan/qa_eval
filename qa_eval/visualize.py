import pandas as pd
from tabulate import tabulate


_DETAILS_COMPACT_HEAD_KEY_LIST = [
    ("PID", "pid"),
    ("QID", "qid"),
    ("Question Type", "answer_type"),
    ("Prediction Type", "prediction_type"),
    ("Correct?", "is_correct"),
    ("Score", "score"),
    ("Non-Correct Reason", "error_reason"),
]

_DETAILS_FULL_HEAD_KEY_LIST = [
    ("PID", "pid"),
    ("QID", "qid"),
    ("Passage", "passage_text"),
    ("Question", "question_text"),
    ("Question Type", "answer_type"),
    ("Answer", "answer_text"),
    ("Prediction", "prediction_text"),
    ("Prediction Type", "prediction_type"),
    ("Correct?", "is_correct"),
    ("Score", "score"),
    ("Non-Correct Reason", "error_reason"),
]

_CORRECTNESS_HEAD_KEY_LIST = [
    ("Type", "type"),
    ("Question Count", "question_count"),
    ("Correct Count", "correct_count"),
    ("Correct Rate", "correct_rate"),
]

_ERROR_REASONS_HEAD_KEY_LIST = [
    ("Reason", "reason"),
    ("Count", "count"),
    ("Rate", "rate"),
]


def _list_to_df(source_list, head_key_list):
    # Convert source list to DataFrame to make visualization and file saving
    # easier.
    df = pd.DataFrame({
        head: [s[key] for s in source_list]
        for head, key in head_key_list
    })

    return df


def _df_to_stdout(df, theme, table_format):
    print(
        "====================== {} Result ======================".format(theme)
    )
    print(tabulate(df, headers='keys', tablefmt=table_format))


def _df_to_csv(df, save_path):
    # Save result to a csv file if path is provided.
    if save_path is not None:
        df.to_csv(save_path)
        print("Result saved to {}".format(save_path))


def visualize_details(pqap_groups, table_format, save_path=None):
    # Convert Passage-Question-Answer-Prediction (PQAP) groups to a list that
    # each item contains detail about a PQAP. The converted list can be fitted
    # to a DataFrame for further use.
    details_list = []
    for pqap_group in pqap_groups:
        pid = pqap_group["pid"]
        passage_text = pqap_group["passage_text"]
        for index, qap in enumerate(pqap_group["qap_list"]):
            details_list.append({
                "pid": pid,
                "passage_text": passage_text if index == 0 else None,
                **qap,
            })

    details_compact_df = _list_to_df(details_list, _DETAILS_COMPACT_HEAD_KEY_LIST)
    _df_to_stdout(details_compact_df, "Details (Compact Version)", table_format)

    details_full_df = _list_to_df(details_list, _DETAILS_FULL_HEAD_KEY_LIST)
    _df_to_csv(details_full_df, save_path)


def visualize_correctness(correctness_list, table_format, save_path=None):
    correctness_df = _list_to_df(correctness_list, _CORRECTNESS_HEAD_KEY_LIST)
    _df_to_stdout(correctness_df, "Correctness", table_format)
    _df_to_csv(correctness_df, save_path)


def visualize_error_reasons(error_reasons, table_format, save_path=None):
    error_reasons_df = _list_to_df(error_reasons, _ERROR_REASONS_HEAD_KEY_LIST)
    _df_to_stdout(error_reasons_df, "Error Reasons", table_format)
    _df_to_csv(error_reasons_df, save_path)


def visualize_scores(score_total):
    print("====================== Scores Result ======================")
    print("Total Score: {}".format(score_total))
