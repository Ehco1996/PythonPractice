'''
文档相似性比较：

步骤：
1 处理文档
2 构建分片集合
3 构建哈希值集合
4 提取特征指纹
5 进行比较
'''

import re


def preprocessing(filename):
    '''
    处理文档中的空白字符

    用re模块的sub方法去除英文字符文件中的字符串
    返回所有字符的小写形式
    '''
    file = open(filename)
    content = file.read()
    space = re.compile(r'\s+')
    content = space.sub('', content)
    content = content.lower()

    return content


def generate_n_gram(string, n):
    '''
    根据n-gram原理，指定文档分片
    将处理后的字符串分割为大小为n的字符串集合
    '''
    n_gram = []
    for i in range(len(string) - n + 1):
        n_gram.append(string[i:i + n])

    return n_gram


def rolling_hashing(n_gram, Base, n):
    '''
    构建哈希值集合，对文档的每个分片进行计算
    '''
    hashlist = []
    hash_valve = 0
    initial = n_gram[0]
    # 初始化： Base一般设置为素数，
    # intial： 第一个分片的hash值通常要几个小手动计算

    for i in range(n):
        hash_valve += ord(initial[i]) * (Base**(n - i - 1))
    hashlist.append(hash_valve)

    for i in range(1, len(n_gram)):
        pre = n_gram[i - 1]
        present = n_gram[i]

        hash_valve = (
            hash_valve - ord(pre[0]) * (Base**(n - 1))) * Base + ord(present[n - 1])
        hashlist.append(hash_valve)

    return hashlist


def winnowing(hashlist, t, n):
    '''
    确定阀值t，所有长度超过t的hash值均会被匹配到，
    确定阀值n，所有长度小于n的hash值均会被忽略。
    则我们的窗口长度为W=t-n+1

    返回特征指纹的字典。特征即为窗口字段的最小值
    返回的字典key为位置，value 为最小值
    '''
    window = t - n + 1
    minValue = minPos = 0
    fingerprint = {}
    for i in range(len(hashlist) - window + 1):
        temp = hashlist[i:i + window]
        minValue = temp[0]
        minPos = 0
        # 开始找出最小值
        for j in range(window):
            if temp[j] < minValue:
                minValue = temp[j]
                minPos = j
        # 将找到的最小值存入字典
        if (i + minPos) not in fingerprint.keys():
            fingerprint[i + minPos] = minValue
    return fingerprint


def comparison(fingerprint_1, fingerprint_2):
    '''
    比较操作检查两片文档的之分之是否存在相同的值
    返回相似的比例
    '''
    count = 0
    size = min(len(fingerprint_1), len(fingerprint_2))
    for i in fingerprint_1.values():
        for j in fingerprint_2.values():
            if i == j:
                count += 1
                break
    return count / size


text1 = '''
In many applications it is useful to record not only 
the fingerprints of a document, but also the position of the fingerprints in the document. 
For example, we need positional information to show the matching substrings in a user interface. 
An efficient implementation of winnowing also needs to retain the position of the most recently selected fingerprint. 
Figure 2(f) shows the set of [fingerprint, position] pairs for this example (the first position is numbered 0). 
To avoid the notational complexity of indexing all hashes with their position in the global sequence of hashes of k-grams of a document, 
we suppress most explicit references to the position of k-grams in documents in our presentation.
'''

text2 = '''
An efficient implementation of winnowing needs to keep the pos of most recently selected fingerprint, too. 
To avoid the complexity of indexing hashes with position in global sequence of hashes of k-grams in a document. 
It is very useful in many applications to not only record the fingerprints of documents, 
but also to record the fingerprints. 
For example, if we need positions to show the matching substrings in a user's interface.
'''

if __name__ == '__main__':
    print('分片大小为5，检测阀值为9')

    text1 = text1.replace(' ', '')
    text1_n_gram = generate_n_gram(text1, 5)
    text1_hash = rolling_hashing(text1_n_gram, 7, 5)
    text1_fingerprint = winnowing(text1_hash, 9, 5)

    text2_fingerprint = winnowing(rolling_hashing(generate_n_gram(text2.replace(' ',''), 5),7, 5), 9, 5)
    
    print(comparison(text1_fingerprint,text2_fingerprint))