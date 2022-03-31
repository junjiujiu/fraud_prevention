from jieba import lcut

def word_frequency_counter(text: str):
    words_data = {}
    with open(text, "r", encoding="utf-8") as f:
        line_counter = 0
        for line in f:
            line_counter += 1
            text = lcut(line)
            for word in text:
                if len(word) > 1 and "x" not in word:
                    if word not in words_data:
                        words_data[word] = 0
                    words_data[word] += 1
        for k, v in words_data.items():
            words_data[k] = v/line_counter
    return words_data


def Bayes_filter(txt: str, spam: dict, ham: dict):
    spam_rate = 1/12  # 垃圾短信占比
    ham_rate = 11/12  # 普通短信占比
    word_pos = 0.0
    count = 0
    for word in lcut(txt):
        if len(word) > 1 and "x" not in word:
            if word in spam:
                count += 1
                # 决定P(A|!B)的值
                ham_pos = 0 if word not in ham else ham[word]
                # 贝叶斯公式
                pos = (spam_rate * spam[word]) / (spam_rate * spam[word] + ham_rate * ham_pos)
                word_pos += pos
    if not count:  # 不含有任何关键字，返回0
        return 0
    return word_pos / count  # 计算概率期望



def calculate_safe_percentage(message: str) -> float:
    spam_frequency = word_frequency_counter("spam.txt")
    ham_frequency = word_frequency_counter("ham.txt")
    text1 = str
    safe = Bayes_filter(text1, spam_frequency, ham_frequency)
    print("pos1", safe)

    return safe
