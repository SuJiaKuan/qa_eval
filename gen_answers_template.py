import json
import argparse


def load_json(file_path, encoding='utf-8'):
    with open(file_path, encoding=encoding) as f:
        data = json.load(f)

        return data


def save_text(file_path, text, encoding='utf-8'):
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(text)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate answers template from official questions",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "questions_path",
        type=str,
        help="Path to questions JSON file (.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="./answers.json",
        help="Path to output file (.json)",
    )

    args = parser.parse_args()

    return args


def gen_template(questions_path, output_path):
    answers_template = []

    # Load questions from JSON file.
    questions_groups = load_json(questions_path)

    # Parse each questions group.
    for questions_group in questions_groups:
        # Parse each question.
        for question in questions_group["QUESTIONS"]:
            # Add an empty answer to the template.
            answers_template.append({
                "QID": question["QID"],
                "QTYPE": question["QTYPE"],
                "ANSWER": "",
            })

    # Save the generated template as a JSON file.
    a_json = json.dumps(answers_template,
                        ensure_ascii=False,
                        indent=4,
                        sort_keys=False)
    save_text(output_path, a_json)


def main(args):
   gen_template(args.questions_path, args.output)


if __name__ == "__main__":
    main(parse_args())
