def get_second_lowest_scorers(score_name_list):
    score_name_list.sort()  # format: [ [score1, name1], [score2, name2] ...]
    second_lowest_score = get_second_lowest_score(score_name_list)

    names = [person[1] for person in score_name_list if person[0] == second_lowest_score]
    names.sort()

    return names


def get_second_lowest_score(score_name_list):
    scores = [person[0] for person in score_name_list]
    scores = list(set(scores))
    scores.sort()
    return scores[1]


if __name__ == "__main__":
    scores_and_names = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        scores_and_names.append([score, name])
    for name in get_second_lowest_scorers(scores_and_names):
        print name
