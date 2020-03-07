import argparse
import os

from qa_eval.data import parse as parse_data
from qa_eval.analytics import analyze_correctness
from qa_eval.analytics import analyze_error_reasons
from qa_eval.visualize import visualize_details
from qa_eval.visualize import visualize_correctness
from qa_eval.visualize import visualize_error_reasons
from qa_eval.config import DEFAULT_OUTPUT_DIR
from qa_eval.config import DEFAULT_TABLE_FORMAT
from qa_eval.config import TABLE_FORMAT_CHOICES
from qa_eval.config import OUTPUT_FILE_NAME


def parse_args():
    parser = argparse.ArgumentParser(
        description="Evaluation tool of question answering model for 2020 "
                    "Formosa Grand Challenge",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        'questions_path',
        type=str,
        help='Path to questions JSON file (.json)',
    )
    parser.add_argument(
        'answers_path',
        type=str,
        help='Path to ground truth answers JSON file (.json)',
    )
    parser.add_argument(
        'predictions_path',
        type=str,
        help='Path to predictions JSON Lines file (.jsonl)',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=DEFAULT_OUTPUT_DIR,
        help='Path to directory that saves the results',
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default=DEFAULT_TABLE_FORMAT,
        help='Format to print the result tables',
        choices=TABLE_FORMAT_CHOICES,
    )

    args = parser.parse_args()

    return args


def main(args):
    # If necessary, create a folder to save output files.
    if not os.path.exists(args.output):
        os.mkdir(args.output)

    # Prase the data from given JSON / JSON Lines files and we get a list
    # Passage-Question-Answer-Prediction (PQAP) group.
    pqap_groups = parse_data(
        args.questions_path,
        args.answers_path,
        args.predictions_path,
    )

    # Visualize and save the details.
    visualize_details(
        pqap_groups,
        args.format,
        save_path=os.path.join(args.output, OUTPUT_FILE_NAME.DETAILS),
    )

    # Analyze the correctness and then visualize and save the results.
    correctness_list = analyze_correctness(pqap_groups)
    visualize_correctness(
        correctness_list,
        args.format,
        save_path=os.path.join(args.output, OUTPUT_FILE_NAME.CORRECTNESS),
    )

    # Analyze the error reason and then visualize and save the results.
    error_reasons = analyze_error_reasons(pqap_groups)
    visualize_error_reasons(
        error_reasons,
        args.format,
        save_path=os.path.join(args.output, OUTPUT_FILE_NAME.ERROR_REASONS),
    )


if __name__ == "__main__":
    main(parse_args())
