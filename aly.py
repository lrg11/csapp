def sortbyScore(score, k):
    '''
    col = len(score)
    scorecol = []
    for i, row in enumerate(score):
        scorecol.append([row[k],i])
    scorecol.sort(reverse=True)
    
    ans = []
    for i, rownum in enumerate(scorecol):
        ans.append(score[rownum[1]])
        '''
    score.sort(key=lambda x: -x[k])
    return score

score= [[10,6,9,1],[7,5,11,2],[4,8,3,15]]

k = 1

print('\n'.join([' '.join([str(i) for i in row]) for row in sortbyScore(score, k)]))