import dagangword as dg
from word_tools import lemmatize_list   #词性还原
from nltk.tokenize import RegexpTokenizer  #分词，去掉标点


# text 为需要检测的文本，grade_input 为年级， unit_input为单元
text = 'Here are some nice photos of pandas. I’m He Hua. I’m in the first photo. I’m 3 years old. I am black and white. In the next photo, you can see a panda, too. Who is he? His name’s He Ye. He is my brother. He Ye is black and white, too. He Ye and I are in Chengdu now. Cheng Gong is our(我们的) mother. Our father is Mei Lan. Here, in the last photo is a special(特殊的) panda. He is brown and white! What’s his name? He’s Qi Zhai. Now he is in Qinling, Shaanxi.'
grade_input = 1
unit_input = 4
#获取大纲词汇，wd_right 为不超纲单词；wd_out 为超纲单词
wd_right, wd_out = dg.word_Normal(grade_input,unit_input)
#处理文本，首先做分词，去掉数字，标点等，并取小写
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(text)   #分词，去掉标点
#words = nltk.word_tokenize(text)
# TODO 需要去掉专用名词； 名词需要变为单数； 动词需要变为一般时态
words = lemmatize_list(words)  #词形变化

words = [word for word in words if not word.isdigit()]  #去掉数字
words = [word for word in words if len(word) > 1]
words=[word.lower() for word in words if word.isalpha()]   #转成小写



for word in words:
    if word in wd_right.keys():
        continue
    elif word in wd_out.keys():
        print(wd_out[word])
    else:
        print(word , "can't find the word in the book")

