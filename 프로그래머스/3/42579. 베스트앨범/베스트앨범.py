def solution(genres, plays):
    answer = []
    total = {} # 장르 : 총 재생 횟수
    album = {} # 장르 : [(플레이 횟수, 고유번호)]
    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        album[genres[i]] = album.get(genres[i], [])+[(plays[i], i)]

    sorted_total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for (genre, total) in sorted_total:
        album[genre] = sorted(album[genre], key=lambda x: (-x[0], x[1],))
        answer += [idx for (play, idx) in album[genre][:2]]

    return answer