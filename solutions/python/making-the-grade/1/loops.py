"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return list(map(lambda score: int(round(score)), student_scores))


def count_failed_students(student_scores):
    counter = 0
    for score in student_scores:
        if score <= 40:
            counter += 1
    return counter


def above_threshold(student_scores, threshold):
    return list(filter(lambda score: score >= threshold, student_scores))
def letter_grades(highest):
    step = (highest - 40) // 4
    return [41, 41 + 1 * step, 41 + 2 * step, 41 + 3 * step]

def student_ranking(student_scores, student_names):
    return [f"{i}. {name}: {score}" for name, score, i in zip(student_names, student_scores, range(1, (len(student_names) + 1)))]


def perfect_score(student_info):
    smart_kids = []
    for student in student_info:
        if 100 in student and len(smart_kids) == 0:
            smart_kids.extend(student)
    return smart_kids
            
