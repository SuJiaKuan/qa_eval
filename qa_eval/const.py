# Definition of problem (i.e., answer or prediction) types.
class PROBLEM_TYPE(object):
    PASSAGE_SPAN = 'passage_span'
    QUESTION_SPAN = 'question_span'
    MULTIPLE_SPANS = 'multiple_spans'
    YESNO = 'yesno'
    MATH = 'math'


# The table that maps from model defined type name to our type name.
MODEL_TYPE_MAPPING = {
    "passage_span": PROBLEM_TYPE.PASSAGE_SPAN,
    "question_span": PROBLEM_TYPE.QUESTION_SPAN,
    "multiple_spans": PROBLEM_TYPE.MULTIPLE_SPANS,
    "yesno": PROBLEM_TYPE.YESNO,
    "arithmetic": PROBLEM_TYPE.MATH,
    "count": PROBLEM_TYPE.MATH,
}


# Separator that separates comparable for answer.
ANSWER_COMPARABLE_SEPARATOR = ";"
# Separators for multi-spans problems.
MULTIPLE_SPANS_SEPARATORS = ["、", "及", "與", "和", "以及"]
# Words for yesno problems.
YESNO_WORDS = ["是", "否"]
