def Count():
    for i in range(0,len(S),3):
        if card[S[i]][int(S[i+1:i+3])-1]:
            return 'ERROR'
        card[S[i]][int(S[i+1:i+3])-1] = 1
    return ' '.join([str(card[key].count(0)) for key in card.keys()])
 
T = int(input())
for t in range(1,T+1):
    S = input().rstrip()
    card = {key:[0]*13 for key in 'SDHC'}
    print(f'#{t} {Count()}')


"""

join() 메소드의 활용: string.join(list)
인덱스 활용에 주의하자

"""