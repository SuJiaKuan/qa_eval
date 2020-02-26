from qa_eval.util import load_json
from qa_eval.util import load_jsonl
from qa_eval.util import any_sep_contained
from qa_eval.util import split_multi_seps
from qa_eval.const import PROBLEM_TYPE
from qa_eval.const import ERROR_REASON
from qa_eval.const import MODEL_TYPE_MAPPING
from qa_eval.const import MULTIPLE_SPANS_SEPARATORS
from qa_eval.const import YESNO_WORDS
from qa_eval.const import ANSWER_COMPARABLE_SEPARATOR


def _parse_answer(passage_text, question_text, answer_text):
    # Remove all white spaces in answer text
    answer_text_trimmed = "".join(answer_text.split())

    # Math is the default problem type.
    answer_type = PROBLEM_TYPE.MATH
    # Answer comparable is a list that each item represent a candidate of
    # correct answers.
    answer_comparable = answer_text.split(sep=ANSWER_COMPARABLE_SEPARATOR)

    # Specify answer type (and adjust answer comparable) according to passage,
    # question and answer.
    if answer_text_trimmed in YESNO_WORDS:
        answer_type = PROBLEM_TYPE.YESNO
    elif any(a in passage_text for a in answer_comparable):
        answer_type = PROBLEM_TYPE.PASSAGE_SPAN
    elif any(a in question_text for a in answer_comparable):
        answer_type = PROBLEM_TYPE.QUESTION_SPAN
    elif any(any_sep_contained(a, MULTIPLE_SPANS_SEPARATORS)
             for a in answer_comparable):
        answer_type = PROBLEM_TYPE.MULTIPLE_SPANS
        answer_comparable = [split_multi_seps(a, MULTIPLE_SPANS_SEPARATORS)
                             for a in answer_comparable]

    return answer_type, answer_comparable


def _parse_prediction(prediction_model_type, prediction_text):
    # Map from model type name to our type name.
    prediction_type = MODEL_TYPE_MAPPING[prediction_model_type]

    if prediction_type != PROBLEM_TYPE.MULTIPLE_SPANS:
        # For non-multiple-spans prediction, its comparable equals to its text.
        prediction_comparable = prediction_text
    else:
        # For multiple-spans prediction, if its prediction contains more than
        # one span, than its comparable is a list of string; otherwise, it is
        # just a string.
        if any_sep_contained(prediction_text, MULTIPLE_SPANS_SEPARATORS):
            prediction_comparable = split_multi_seps(
                prediction_text,
                MULTIPLE_SPANS_SEPARATORS,
            )
        else:
            prediction_comparable = prediction_text

    return prediction_type, prediction_comparable


def _compare_answer(answer_type, answer_comparable, prediction_comparable):
    # Walk through the answer candidates.
    for candidate in answer_comparable:
        # If answer type is multiple-spans, convert answer candidate and
        # prediction into sets to make comparision easier
        candidate_trans = set(candidate) \
                          if answer_type is PROBLEM_TYPE.MULTIPLE_SPANS \
                          else candidate
        prediction_trans = set(prediction_comparable) \
                           if answer_type is PROBLEM_TYPE.MULTIPLE_SPANS \
                           else prediction_comparable

        # Return true if any candidate equals to the prediction.
        if candidate_trans == prediction_trans:
            return True

    # Return false if no candidate equals to the prediction.
    return False


def _decide_error_reason(answer_type, prediction_type):
    if answer_type == prediction_type:
        return ERROR_REASON.RIGHT_TYPE_WRONG_PREDICTION

    return ERROR_REASON.WRONG_TYPE


def parse(questions_path, answers_path, predictions_path):
    pqap_groups = []

    # Load data from JSON / JSON Lines files.
    questions_groups = load_json(questions_path)
    answers = load_json(answers_path)
    predictions = load_jsonl(predictions_path)

    # Convert answers and predictions from list of dictionary that will be
    # easier to be accessed.
    answers = {a["QID"]: a["ANSWER"] for a in answers}
    predictions = {p["query_id"]: p["answer"] for p in predictions}

    for questions_group in questions_groups:
        # Parse passage in a questions group.
        pid = questions_group["DID"]
        passage_text = questions_group["DTEXT"]

        qap_list = []
        # Parse each question and its corresponding answer and prediction.
        for question in questions_group["QUESTIONS"]:
            # Parse question
            qid = question["QID"]
            question_text = question["QTEXT"]
            # Parse answer instance to get its text, type and comparable.
            answer_text = answers[qid]
            answer_type, answer_comparable = _parse_answer(
                passage_text,
                question_text,
                answer_text,
            )
            # Parse prediction instance to get its text, type and comparable.
            prediction = predictions[qid]
            prediction_text = prediction["value"]
            prediction_model_type = prediction["answer_type"]
            prediction_type, prediction_comparable = _parse_prediction(
                prediction_model_type,
                prediction_text,
            )
            # Decide the prediction is correct or not.
            is_correct = _compare_answer(
                answer_type,
                answer_comparable,
                prediction_comparable,
            )
            # Decide the reason if it is not correct.
            error_reason = None \
                           if is_correct \
                           else _decide_error_reason(answer_type, prediction_type)

            qap_list.append({
                "qid": qid,
                "question_text": question_text,
                "answer_type": answer_type,
                "answer_text": answer_text,
                "prediction_type": prediction_type,
                "prediction_text": prediction_text,
                "is_correct": is_correct,
                "error_reason": error_reason,
            })

        pqap_groups.append({
            "pid": pid,
            "passage_text": passage_text,
            "qap_list": qap_list,
        })

    return pqap_groups
