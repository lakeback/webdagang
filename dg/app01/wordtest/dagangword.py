import xlrd

word_path = 'app01/wordtest/data/word list.xls'
wb = xlrd.open_workbook(word_path)
wb.sheet_names()
sh = wb.sheet_by_name('latest')
grade_name = {
    '1.0': '七上',
    '2.0': '七下',
    '3.0': '八上',
    '4.0': '八下',
    '5.0': '九'
}

def word_Normal(grade = 1.0,unit = 1.0):
    word_in_rightgrade = {}
    word_out_grade = {}
    grade = float(grade)
    unit = float(unit)

    for rn in range(1, sh.nrows):
        word, _, word_mean, _, _, _, _,grd, unt, cls = sh.row_values(rn)
        if word.isalpha():
            word = word.lower()
        if grd < grade:
            word_in_rightgrade[word] = [word, word_mean, grade_name[str(grd)], unt, cls]
        elif grd == grade and unt <= unit:
            word_in_rightgrade[word] = [word,word_mean,grade_name[str(grd)],unt,cls]
        else:
            word_out_grade[word] = [word,word_mean,grade_name[str(grd)],unt,cls]
    return word_in_rightgrade, word_out_grade



if __name__ == '__main__':

    wd_right,wd_out = word_Normal(1,2)
    print(len(wd_right))