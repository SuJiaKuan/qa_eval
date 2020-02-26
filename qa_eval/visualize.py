import pandas as pd
from tabulate import tabulate


def visualize_correctness(correctness_list, save_path=None):
    # Convert correctness list to DataFrame to make visualization and file
    # saving easier.
    correctness_df = pd.DataFrame({
        "Type": [c["type"] for c in correctness_list],
        "Question Count": [c["question_count"] for c in correctness_list],
        "Correct Count": [c["correct_count"] for c in correctness_list],
        "Correct Rate": [c["correct_rate"] for c in correctness_list],
    })

    print("====================== Correctness Result ======================")
    print(tabulate(correctness_df, headers='keys', tablefmt='psql'))

    # Save result to a csv file.
    if save_path is not None:
        correctness_df.to_csv(save_path)
        print("Correctness result saved to {}".format(save_path))


def visualize_error_reasons(error_reasons, save_path=None):
    # Convert error rates to DataFrame to make visualization and file
    # saving easier.
    error_reasons_df = pd.DataFrame({
        "Reason": [r["reason"] for r in error_reasons],
        "Count": [r["count"] for r in error_reasons],
        "Rate": [r["rate"] for r in error_reasons],
    })

    print("====================== Error Reasons Result ======================")
    print(tabulate(error_reasons_df, headers='keys', tablefmt='psql'))

    # Save result to a csv file.
    if save_path is not None:
        error_reasons_df.to_csv(save_path)
        print("Error reasons result saved to {}".format(save_path))
