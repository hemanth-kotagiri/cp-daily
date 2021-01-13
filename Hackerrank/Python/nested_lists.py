if __name__ == '__main__':
    scores = set()
    scores_students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        if score in scores_students:
            scores_students[score].append(name)
        else:
            scores_students[score] = [name]

    score = sorted(scores)[1]
    if score in scores_students:
        if len(scores_students[score]) > 1:
            curr = sorted(scores_students[score])
            print(curr[0])
            print(curr[1])
        else:
            print(scores_students[score])
