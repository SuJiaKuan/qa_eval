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

## Outputs

After running the tools, you will get three kinds of result: details, correctness and error reasons.

### Details

The result shows detail for each of your model prediction. You can see a compact version report on stdout and full version report in `output/details.csv`.

Meaning of the fields:

- `PID`: Passage ID
- `QID`: Question ID
- `Passage`: Passage text (only in full version)
- `Question`: Question text (only in full version)
- `Question Type`: Question type, it can be:
    - `passage_span`: The answer should be extracted from passage
    - `question_span`: The answer should be extracted from question
    - `multiple_spans`: The answer should be extracted from passage (more than one span)
    - `yesno`: The answer should be yes or no
    - `math`: The answer is a math problem (arithmetic or counting)
- `Answer`: Ground truth text (only in full version)
- `Prediction`: Your model prediction text (only in full version)
- `Correct?`: Your model prediction is correct or not
- `Non-Correct Reason`: If your model prediction is not correct, what is the reason? It can be:
    - `right_type_wrong_prediction`: Your model predicted a correct question type, but its prediction is wrong
    - `wrong_type`: Your model predicted a wrong question type

An example of compact version details report is shown as follows:

```
====================== Details (Compact Version) Result ======================
+----+-------+---------+-----------------+------------+-----------------------------+
|    | PID   | QID     | Question Type   | Correct?   | Non-Correct Reason          |
|----+-------+---------+-----------------+------------+-----------------------------|
|  0 | D058  | D058Q07 | multiple_spans  | False      | right_type_wrong_prediction |
|  1 | D058  | D058Q10 | multiple_spans  | False      | wrong_type                  |
|  2 | D058  | D058Q11 | passage_span    | False      | right_type_wrong_prediction |
|  3 | D058  | D058Q13 | passage_span    | False      | right_type_wrong_prediction |
|  4 | D058  | D058Q14 | passage_span    | False      | right_type_wrong_prediction |
|  5 | D058  | D058Q15 | passage_span    | False      | right_type_wrong_prediction |
|  6 | D058  | D058Q17 | passage_span    | False      | right_type_wrong_prediction |
|  7 | D124  | D124Q02 | passage_span    | True       |                             |
|  8 | D124  | D124Q03 | yesno           | False      | right_type_wrong_prediction |
|  9 | D124  | D124Q04 | yesno           | False      | right_type_wrong_prediction |
| 10 | D124  | D124Q05 | passage_span    | False      | right_type_wrong_prediction |
| 11 | D124  | D124Q06 | passage_span    | False      | right_type_wrong_prediction |
| 12 | D124  | D124Q07 | math            | False      | wrong_type                  |
| 13 | D124  | D124Q08 | passage_span    | True       |                             |
| 14 | D126  | D126Q01 | passage_span    | True       |                             |
| 15 | D126  | D126Q02 | passage_span    | True       |                             |
| 16 | D126  | D126Q03 | multiple_spans  | False      | right_type_wrong_prediction |
| 17 | D126  | D126Q04 | passage_span    | True       |                             |
| 18 | D126  | D126Q05 | multiple_spans  | False      | wrong_type                  |
| 19 | D126  | D126Q06 | multiple_spans  | False      | right_type_wrong_prediction |
| 20 | D126  | D126Q07 | yesno           | True       |                             |
| 21 | D126  | D126Q09 | passage_span    | False      | right_type_wrong_prediction |
| 22 | D201  | D201Q01 | yesno           | True       |                             |
| 23 | D201  | D201Q02 | yesno           | True       |                             |
| 24 | D201  | D201Q03 | yesno           | True       |                             |
| 25 | D201  | D201Q04 | yesno           | False      | right_type_wrong_prediction |
| 26 | D201  | D201Q05 | yesno           | False      | right_type_wrong_prediction |
| 27 | D204  | D204Q01 | passage_span    | True       |                             |
| 28 | D204  | D204Q02 | passage_span    | False      | right_type_wrong_prediction |
| 29 | D204  | D204Q03 | passage_span    | False      | right_type_wrong_prediction |
| 30 | D204  | D204Q04 | math            | False      | wrong_type                  |
| 31 | D204  | D204Q06 | passage_span    | True       |                             |
| 32 | D204  | D204Q07 | passage_span    | False      | right_type_wrong_prediction |
| 33 | D204  | D204Q08 | yesno           | True       |                             |
| 34 | D320  | D320Q01 | passage_span    | True       |                             |
| 35 | D320  | D320Q02 | yesno           | True       |                             |
| 36 | D320  | D320Q03 | yesno           | True       |                             |
| 37 | D320  | D320Q05 | yesno           | False      | right_type_wrong_prediction |
| 38 | D320  | D320Q06 | yesno           | True       |                             |
| 39 | D320  | D320Q07 | yesno           | True       |                             |
| 40 | D320  | D320Q08 | yesno           | False      | right_type_wrong_prediction |
| 41 | D324  | D324Q01 | passage_span    | False      | right_type_wrong_prediction |
| 42 | D324  | D324Q02 | passage_span    | True       |                             |
| 43 | D324  | D324Q03 | passage_span    | False      | wrong_type                  |
| 44 | D324  | D324Q05 | passage_span    | True       |                             |
| 45 | D324  | D324Q09 | passage_span    | False      | right_type_wrong_prediction |
| 46 | D325  | D325Q01 | passage_span    | False      | right_type_wrong_prediction |
| 47 | D325  | D325Q03 | passage_span    | True       |                             |
| 48 | D325  | D325Q04 | passage_span    | True       |                             |
| 49 | D325  | D325Q05 | yesno           | False      | right_type_wrong_prediction |
+----+-------+---------+-----------------+------------+-----------------------------+
```
