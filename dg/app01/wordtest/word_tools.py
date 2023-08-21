from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag,word_tokenize
from nltk.stem import WordNetLemmatizer
import app01.wordtest.dagangword as dg
#对整个句子进行词性还原
def lemmatize_all(sentence):
    wnl = WordNetLemmatizer()
    for word, tag in pos_tag(word_tokenize(sentence)):
        if tag.startswith('NN'):
            yield wnl.lemmatize(word, pos='n')
        elif tag.startswith('VB'):
            yield wnl.lemmatize(word, pos='v')
        elif tag.startswith('JJ'):
            yield wnl.lemmatize(word, pos='a')
        elif tag.startswith('R'):
            yield wnl.lemmatize(word, pos='r')
        else:
            yield word

#对已经进行分词处理的列表进行词性还原
"""
CC 连词 and, or,but, if, while,although
CD 数词 twenty-four, fourth, 1991,14:24
DT 限定词 the, a, some, most,every, no
EX 存在量词 there, there's
FW 外来词 dolce, ersatz, esprit, quo,maitre
IN 介词连词 on, of,at, with,by,into, under
JJ 形容词 new,good, high, special, big, local
JJR 比较级词语 bleaker braver breezier briefer brighter brisker
JJS 最高级词语 calmest cheapest choicest classiest cleanest clearest
LS 标记 A A. B B. C C. D E F First G H I J K
MD 情态动词 can cannot could couldn't
NN 名词 year,home, costs, time, education
NNS 名词复数 undergraduates scotches
NNP 专有名词 Alison,Africa,April,Washington
NNPS 专有名词复数 Americans Americas Amharas Amityvilles
PDT 前限定词 all both half many
POS 所有格标记 ' 's
PRP 人称代词 hers herself him himself hisself
PRP$ 所有格 her his mine my our ours
RB 副词 occasionally unabatingly maddeningly
RBR 副词比较级 further gloomier grander
RBS 副词最高级 best biggest bluntest earliest
RP 虚词 aboard about across along apart
SYM 符号 % & ' '' ''. ) )
TO 词to to
UH 感叹词 Goodbye Goody Gosh Wow
VB 动词 ask assemble assess
VBD 动词过去式 dipped pleaded swiped
VBG 动词现在分词 telegraphing stirring focusing
VBN 动词过去分词 multihulled dilapidated aerosolized
VBP 动词现在式非第三人称时态 predominate wrap resort sue
VBZ 动词现在式第三人称时态 bases reconstructs marks
WDT Wh限定词 who,which,when,what,where,how
WP WH代词 that what whatever
WP$ WH代词所有格 whose
WRB WH副词
"""
def lemmatize_list(tokened_words):
    wnl = WordNetLemmatizer()
    word_list = []
    for word, tag in pos_tag(tokened_words):
        if word in ['am','is','are']:
            word_list.append(word)
        elif tag.startswith('NNP'):
            continue
        elif tag.startswith('NN'):
            word_list.append(wnl.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            word_list.append(wnl.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            word_list.append(wnl.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            word_list.append(wnl.lemmatize(word, pos='r'))
        elif tag.startswith('S'):
            continue
        else:
            word_list.append(word)
    return word_list

# 封装了超纲词汇辨识函数
# 输入text：输入的文本
# grade：年级
# unit：单元
def chaogangword(text, grade, unit):
    text = text
    grade_input = grade
    unit_input = unit

    # 获取大纲词汇，wd_right 为不超纲单词；wd_out 为超纲单词
    wd_right, wd_out = dg.word_Normal(grade_input, unit_input)
    # 处理文本，首先做分词，去掉数字，标点等，并取小写
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)  # 分词，去掉标点
    # words = nltk.word_tokenize(text)
    # TODO 需要去掉专用名词； 名词需要变为单数； 动词需要变为一般时态
    words = lemmatize_list(words)  # 词形变化

    words = [word for word in words if not word.isdigit()]  # 去掉数字
    words = [word for word in words if len(word) > 1]
    words = [word.lower() for word in words if word.isalpha()]  # 转成小写

    chao_words = []
    for word in words:
        if word in wd_right.keys():
            continue
        elif word in wd_out.keys():
            chao_words.append(wd_out[word])
        else:
            chao_words.append([word, "can't find the word in the book"])

    return chao_words

if __name__ == '__main__':
    sentence =  "NLTK is a powerful Python library for working with human language data."
    # words = lemmatize_all(sentence)
    # for w in words:
    #     print(w)
    tokenizer = RegexpTokenizer(r'\w+')
    word = tokenizer.tokenize(sentence)
    # word = word_tokenize(sentence)
    # words = lemmatize_list(word)
    #
    # for w in words:
    #     print(w)
    print(word)