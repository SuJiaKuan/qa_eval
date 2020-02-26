import argparse

from qa_eval.data import parse as parse_data


def parse_args():
    parser = argparse.ArgumentParser(
        description="Evaluation tool of question answering model for 2020 "
                    "Formosa Grand Challenge",
    )
    parser.add_argument(
        'questions_path',
        type=str,
        help='Path to questions JSON file (.json)',
    )
    parser.add_argument(
        'answers_path',
        type=str,
        help='Path to answers JSON file (.json)',
    )
    parser.add_argument(
        'predictions_path',
        type=str,
        help='Path to predictions JSON Lines file (.jsonl)',
    )

    args = parser.parse_args()

    return args


def main(args):
    pqap_groups = parse_data(
        args.questions_path,
        args.answers_path,
        args.predictions_path,
    )
    # TODO


if __name__ == "__main__":
    main(parse_args())
