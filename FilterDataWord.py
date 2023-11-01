import json
import csv 
from nltk.stem.snowball import SnowballStemmer  # thư viện lấy ra root của 1 word 
stemmer = SnowballStemmer("english")
# Đọc file các từ TOEIC 
with open('DataWord.txt', 'r') as f:
    TOEICWord = [line.split() for line in f] 
# Đọc file Learn
f = open('Topic2.json')
data = json.load(f)
f.close
# Hàm convert list sang String
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

# Hàm FilterWordNotUsed trả về các từ không xuất hiện trong file Learn nhưng có trong từ điển các từ TOEIC
def FilterWordNotUsed(data,TOEICWord): 
    c = []
    d = []
    for i in data:
        content = i['Content'] # Đọc từng content trong từng file
        content_split = content.split() #Tách chuỗi các content 
        for a in content_split  : # vòng lặp với các từ trong mỗi content
            for b in TOEICWord :  # Vòng lặp với mỗi từ trong TOEICWord
                if stemmer.stem(listToString(b)) == stemmer.stem(a) : #Đưa về root word mỗi từ và so sánh nếu giống nhau thì add vào mảng c 
                    c.append(listToString(b))
    # Chuyển list TOIECWord từ list sang String để tiến hành filter ra các từ ko xuất hiện                 
    for i in TOEICWord : 
        d.append(listToString(i))
    # Đưa mảng c và d từ dạng list các string về dạng set sau đó trừ đi cho nhau để tìm ra các từ ko xuất hiện
    k = set(c) ^ set(d)
    res = dict.fromkeys(k, 0)
    with open('tukhongxuathien.csv', 'w') as csv_file:  # đặt tên cho file csv xuất ra các từ không xuất hiện 
        writer = csv.writer(csv_file)
        for key in res.items():
            writer.writerow([key])
    # return my_dict ,k, len(k)
    return k , len(k) 
def FilterWordUsed(data,TOEICWord): 
    c = []
    d = []
    for i in data:
        content = i['Content'] # Đọc từng content trong từng file
        content_split = content.split() #Tách chuỗi các content 
        for a in content_split  : # vòng lặp với các từ trong mỗi content
            for b in TOEICWord :  # Vòng lặp với mỗi từ trong TOEICWord
                if stemmer.stem(listToString(b)) == stemmer.stem(a) : #Đưa về root word mỗi từ và so sánh nếu giống nhau thì add vào mảng c 
                    c.append(listToString(b))
    # Chuyển list TOIECWord từ list sang String để tiến hành filter ra các từ ko xuất hiện                 
    my_dict = {i:c.count(i) for i in c} # Trả về các từ xuất hiện và đếm số lần xuất hiện của từng từ 
    with open('dattendic.csv', 'w') as csv_file:  # đặt tên cho file csv xuất ra các từ xuất hiện trong từng topic 
        writer = csv.writer(csv_file)
        for key , value in my_dict.items():
            writer.writerow([key , value])
    return my_dict

def main():
    # modified_data = FilterWordNotUsed(data,TOIECWord) # Mở cmt này nếu muốn filter những từ không xuất hiện và số lượng từ đó 
    modified_data = FilterWordUsed(data,TOEICWord) # Mở cmt này và cmt dòng trên nếu muốn filter những từ xuất hiện và đưa ra số lần lặp

    print(modified_data)

if __name__ == "__main__":
    main()


