# Question Answering Evaluation Tools

The project targets on question answering models for 2020 Formosa Grand Challenge. It provides tools for correctness evaluation, analytics and visualization.

## Prerequisites

The project only support Python3. You need to install following packages via pip or conda:

- json-lines
- pandas
- tabulate

## Usages

### Example Usage

Run following command and you will see the results:

```bash
python3 eval.py \
  ./examples/official_1_questions.json \
  ./examples/official_1_answers.json \
  ./examples/predictions.jsonl
```

### Detailed Usages

Run following command to see detail usages:

```bash
python3 eval.py -h
```

The usages is shown as follows:

```
usage: eval.py [-h] [-o OUTPUT] questions_path answers_path predictions_path

Evaluation tool of question answering model for 2020 Formosa Grand Challenge

positional arguments:
  questions_path        Path to questions JSON file (.json)
  answers_path          Path to ground truth answers JSON file (.json)
  predictions_path      Path to predictions JSON Lines file (.jsonl)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to directory that saves the results
```
