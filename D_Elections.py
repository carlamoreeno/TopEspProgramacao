def calculateResults(votes):
    results = []
    for i, candidate in enumerate(votes):
        remaining_votes = [vote for j, vote in enumerate(votes) if j != i]
        winnerCandidate = max(remaining_votes)

        if winnerCandidate < candidate:
            results.append(0)
        elif winnerCandidate == candidate:
            results.append(1)
        else:
            results.append(winnerCandidate - candidate + 1)
    return results

num_elections = int(input())
for i in range(num_elections):
    votes = list(map(int, input().split()))
    results = calculateResults(votes)
    print(" ".join(str(x) for x in results))