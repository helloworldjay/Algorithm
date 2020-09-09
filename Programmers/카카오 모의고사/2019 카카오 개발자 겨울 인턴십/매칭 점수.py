# 주소를 찾는 함수
def find_name(page):
    idx = page.find("content=")
    idx += 9
    domain = []
    while True:
        if page[idx] == '"':
            break
        domain.append(page[idx])
        idx += 1
    return ''.join(domain)
# 어디로 링크하는지 찾는 함수
def find_anchor(html):
    domain = []
    while True:
        idx = html.find("href=")
        if idx == -1:
            break
        html = html[:idx] + "t" + html[idx+1:]
        idx += 6
        anchor = []
        while True:
            if html[idx] == '"':
                break
            anchor.append(html[idx])
            idx += 1
        domain.append(''.join(anchor))
    return domain

def solution(word, pages):
    # 단어를 소문자로
    word = word.lower()
    # 기본 점수
    base_score = {}
    # 외부 링크의 개수
    to_out_link = {}
    # 외부 링크의 종류
    from_out_line = {}
    # 모든 페이지를 소문자로
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
        # 주소를 저장해두기
        address = find_name(pages[i])
        base_score[address] = 0
        to_out_link[address] = 0
        from_out_line[address] = []
    # 기본 점수는 pages에 word가 몇개 있는지로 결정한다.
    for i in range(len(pages)):
        address = find_name(pages[i])
        base_score[address] = (i,pages[i].count(word))
        to_out_link[address] = (i, pages[i].count("</a>"))
        temp = find_anchor(pages[i])
        for j in range(len(temp)):
            if temp[j] in from_out_line:
                from_out_line[temp[j]].append(i)
    match_score = [0]*len(pages)
    #items의 결과물은 list로 나온다
    base_score_values = sorted(list(base_score.items()), key= lambda x:x[1][0])
    to_out_link_values = sorted(list(to_out_link.items()), key= lambda x:x[1][0])
    for i in range(len(match_score)):
        match_score[i] = base_score_values[i][1][1] 
    return 

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
# print(find_name("content=\"http://www.naver.com\""))