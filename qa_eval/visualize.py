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
