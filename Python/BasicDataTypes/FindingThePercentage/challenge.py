from functools import reduce


def get_student_average(name, students_and_scores):
    return reduce((lambda x, y: x + y), students_and_scores[name])/len(students_and_scores[name])


if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print "{0:.2f}".format(get_student_average(query_name, student_marks))
