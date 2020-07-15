ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty" ,"fifty", "sixty", "seventy", "eighty", "ninety"]
bigs = ["", "thousand", "million", "billion", "trillion"]

num = 555280

#(five hundred (fifty-five)) (thousand) (two hundred) (eighty)

def num20(num):
    number = ones[num]
    if number == "":
        number = "zero"
    return f"{number}"
	
def num99(num):
    num = str(num)
    ten_c = tens[int(num[0])] 
    one_c = ones[int(num[1])]
    dash = '-'
    if one_c == "":
        dash = ''
    return f"{ten_c}{dash}{one_c}"

def teens(num):
    if num < 20:
        txt = num20(num)
    else:
        txt = num99(num)
    return txt 
	
def num999(num):
    num = str(num)
    hun = ones[int(num[0])]
    digs = teens(int(num))
    return f"{hun} hundred {digs}"
	
def big_nums(num):
    new_num = []
    num = str(num)
    txt = []
    while len(num) >= 3:
        new_num.append(num[-3:])
        num = num[:-3]
    new_num = new_num[-1::-1]
    for number in new_num:
        if len(new_num) > 1:
            print(new_num)
            how_big = len(new_num) - 1
            ions = bigs[how_big]
        num_name = num999(int(number))    
        txt.append(num_name)
        if len(new_num) > 1:
            txt.append(ions)
        new_num.remove(number)       
        print(new_num)
    print(txt)

big_nums(num)
