import re


def aa():
    htmlstr = ''
    html = '''
    <br>
    %s
    <br>
    <img src="%s" alt="" />
    <br>
    <audio src="%s" controls="controls"></audio>
    <br>
    %s
    <br>
    <br>
    <br>
    '''

    with open(r'C:\Users\lcc92\Desktop\音频.txt', 'r', encoding='UTF-8-sig') as f:
        l = list(f)
    print(l)
    # for i in l:
    #     m1 = re.match(r'^.*aac', i).group()
    #     m2 = re.search(r' .*秒 ', i).group()
    #     m3 = re.search(r'——.*——', i).group()
    #     p = re.compile(r'——')
    #     m3 = p.sub(r'', m3)
    #     try:
    #         m4 = re.search(r'http://im.*jpeg', i).group()
    #     except:
    #         m4 = ''
    #     htmll = html % (m3, m4, m1, m2)
    #     htmlstr += htmll
    #     # print(htmlstr)
    #
    #
    # with open(r'C:\Users\lcc92\Desktop\1.html', 'r+', encoding='utf-8') as f:
    #     f.seek(285, 0)
    #     f.write(htmlstr)

aa()