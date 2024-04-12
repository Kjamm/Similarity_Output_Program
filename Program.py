from gensim.models import Word2Vec
from konlpy.tag import Okt

okt = Okt()

corpus = open('txt 파일 입력', 'r', encoding='utf-8')
#txt 파일 입력 칸에 txt 파일 경로를 입력해주세요.

tokens = []

for sentence in corpus :
    tokens.append(okt.morphs(sentence.strip()))


model = Word2Vec(sentences=tokens, min_count=1, vector_size=5, sg=1)

for i in range(6) :
    str = input("단어를 입력하시오 : ")
    try:
        similarWord = model.wv.most_similar(positive=[str], topn=5)
        print(similarWord)
    except KeyError as e :
        print("txt파일에 없는 단어입니다.")

