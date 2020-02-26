from qa_eval.const import PROBLEM_TYPE


# Put types that we want to analyze for correctness here.
_CORRECTNESS_TYPES = [
    PROBLEM_TYPE.PASSAGE_SPAN,
    PROBLEM_TYPE.QUESTION_SPAN,
    PROBLEM_TYPE.MULTIPLE_SPANS,
    PROBLEM_TYPE.YESNO,
    PROBLEM_TYPE.MATH,
    "overall",
]
# Create a inversed index table to make the index search of correctness type
# faster.
_CORRECTNESS_TYPE_INDEX = {
    t: _CORRECTNESS_TYPES.index(t)
    for t in _CORRECTNESS_TYPES
}


def analyze_correctness(pqap_groups):
    correctness_list = [
        {"type": t, "question_count": 0, "correct_count": 0, "correct_rate": "0%"}
        for t in _CORRECTNESS_TYPES
    ]

    overall_index = _CORRECTNESS_TYPE_INDEX["overall"]

    # Walk through each Question-Answer-Prediction for each
    # Passage-Question-Answer-Prediction group.
    for pqap_group in pqap_groups:
        for qap in pqap_group["qap_list"]:
            type_index = _CORRECTNESS_TYPE_INDEX[qap["answer_type"]]
            correctness_list[overall_index]["question_count"] += 1
            correctness_list[type_index]["question_count"] += 1
            if qap["is_correct"]:
                correctness_list[overall_index]["correct_count"] += 1
                correctness_list[type_index]["correct_count"] += 1

    # Calculate correct rate for each question type.
    for correctness in correctness_list:
        question_count = correctness["question_count"]
        correct_count = correctness["correct_count"]
        if question_count > 0:
            correct_rate = int(correct_count / question_count * 100)
            correct_rate = "{}%".format(correct_rate)
            correctness["correct_rate"] = correct_rate

    return correctness_list
