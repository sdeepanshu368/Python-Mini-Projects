def mathingWords(query, sentence):
    qwords = query.strip().split(" ")
    swords = sentence.strip().split(" ")
    score = 0
    for qword in qwords:
        for sword in swords:
            # print(f"Matching {word1} with {word2}")
            if qword.lower() == sword.lower():
                score += 1
    return score


if __name__ == "__main__":
    sentences = ["python is a good", "this is snake",
                 "dev is a good boy", "easy to write"]

    query = input("Please enter the query string\n")
    scores = [mathingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0 ]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")
