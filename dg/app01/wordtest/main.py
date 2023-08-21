from word_tools import chaogangword

"""
输入三个参数
text: 粘入阅读材料
grade: 年级,数字对应关系如下：  七上：1；七下：2；八上：3；八下：4；九：5； 
unit：单元数字对应关系，几单元就写数字几。特别说明的是七上的S1-S3对应的数字为-3，-2，-1
输出格式如下
['here', '（用以介绍某人或某物）这就是；在这里', 1.0, 2.0, 5.0]对应的参数是
[单词，               汉语意思，             年级，单元，课时]
"""

text = "Here are some nice photos of pandas." \
       " I’m He Hua. I’m in the first photo. I’m 3 years old." \
       " I am black and white. In the next photo, you can see a panda, too." \
       " Who is he? His name’s He Ye. He is my brother. He Ye is black and white, too." \
       " He Ye and I are in Chengdu now. Cheng Gong is our(我们的) mother. Our father is Mei Lan. " \
       "Here, in the last photo is a special(特殊的) panda. He is brown and white! What’s his name? He’s Qi Zhai. Now he is in Qinling, Shaanxi. "
grade = 1
unit = 2

chaogangword(text, grade, unit)