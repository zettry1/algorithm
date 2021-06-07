

HOME_TEAM_WON = 1
def tournamentWinner(competitions, results):
    currentBestTeam=""
    scores={currentBestTeam:0}
    for idx,competition in enumerate (competitions):
        result = results[idx]
        homeTeam,awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winningTeam,3,scores)
        if scores[winningTeam]> scores[currentBestTeam]:
            currentBestTeam=winningTeam
    return currentBestTeam

def updateScores(team,points,scores):
    if team not in scores:
        scores[team]=0
    scores[team]+=points



# def tournamentWinner2(competitions,results):
# scores={}
# for idx,match in enumerate (competitions,0):
#     if results[idx]==0:
#         if match[1] in scores:
#             scores[match[1]]+= 3
#         else:
#             scores[match[1]]=3
#     else:
#         if match[0] in scores:
#             scores[match[0]]+= 3
#         else:
#             scores[match[0]]=3

#     print(scores,max(scores))

tournamentWinner([ ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]],[0,1,1])