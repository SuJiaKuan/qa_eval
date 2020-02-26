import pandas as pd
from tabulate import tabulate


CORRECTNESS_HEAD_KEY_LIST = [
    ("Type", "type"),
    ("Question Count", "question_count"),
    ("Correct Count", "correct_count"),
    ("Correct Rate", "correct_rate"),
]

ERROR_REASONS_HEAD_KEY_LIST = [
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


def _df_to_stdout(df, theme):
    print(
        "====================== {} Result ======================".format(theme)
    )
    print(tabulate(df, headers='keys', tablefmt='psql'))


def _df_to_csv(df, save_path):
    # Save result to a csv file if path is provided.
    if save_path is not None:
        df.to_csv(save_path)
        print("Result saved to {}".format(save_path))


def visualize_correctness(correctness_list, save_path=None):
    correctness_df = _list_to_df(correctness_list,CORRECTNESS_HEAD_KEY_LIST)
    _df_to_stdout(correctness_df, "Correctness")
    _df_to_csv(correctness_df, save_path)


def visualize_error_reasons(error_reasons, save_path=None):
    error_reasons_df = _list_to_df(error_reasons, ERROR_REASONS_HEAD_KEY_LIST)
    _df_to_stdout(error_reasons_df, "Error Reasons")
    _df_to_csv(error_reasons_df, save_path)
