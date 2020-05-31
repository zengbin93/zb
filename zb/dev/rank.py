# -*- coding: UTF-8 -*-
import re
import jieba.analyse
import string


class BaseRank:
    """基类"""

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def rank(self, top=None):
        raise NotImplementedError

    @property
    def top30(self):
        return self.rank(top=30)

    @property
    def top50(self):
        return self.rank(top=50)

    @property
    def top100(self):
        return self.rank(top=100)


class TfidfDocRank(BaseRank):
    """基于TFIDF的文档重要性排序

    :param documents: list
        中文文档内容列表，如：
        ['美俄安全对话：会谈5小时，未发布联合声明',
         '内塔尼亚胡仍盼美国承认戈兰高地归以色列',
         '缩量盘整中资金调仓换股 金融股5日吸金近60亿元']
    :param N: int, 默认值 10
        从每篇文档中取出的重要关键词的数量

    ========================================================
    核心思想：
        文档由词构成，前 N 个关键词的平均重要性高的文档重要性也高；
        同时，对短文本施加惩罚。

    算法过程
    ========================================================
    输入:
        1）文档列表，2）N
    计算:
        step 1. 对每一个文档进行分词，提取 N 个关键词，计算每个
            关键词的 tfidf值；
        step 2. 计算每篇文档的前 N 个关键词的词均tfidf值，公式如下：
            文档词均 tfidf值 = 所有关键词的 tfidf值之和 / N
        step 3. 对 文档词均 tfidf值  施加惩罚
        step 4. 按照施加惩罚后的 “文档词均tfidf值”，从大到小排序
    输出:
        文档排序结果
    ========================================================
    """

    def __init__(self, documents, N=10):
        desc = "基于TFIDF的文档重要性排序"
        super(TfidfDocRank).__init__(name='tfidf_doc_rank', desc=desc)
        self.documents = documents
        self.N = N

        # doc 平均长度
        self.mean_length = sum([len(doc) for doc in documents]) / len(documents)

    def data_prepare(self):
        docs = self.documents
        # 清理数字、字母
        docs = [re.sub("[\d+\u3000a-zA-Z]", "", x) for x in docs]

        # 清理中英文标点
        ch_punc = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀" \
                  "｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟" \
                  "〰〾〿–—‘’‛“”„‟…‧﹏."
        punc = ch_punc + string.punctuation
        docs = [re.sub("[%s]" % punc, "", x) for x in docs]
        return docs

    def mean_tfidf(self, doc, top_k=None):
        """计算doc的词均tfidf值"""
        doc_length = len(doc)
        # punish 范围：0.1 ~ 3 
        punish = 1 / (self.mean_length / doc_length)
        if punish < 0.1:
            punish = 0.1
        elif punish > 3:
            punish = 3
        else:
            punish = punish

        kw = jieba.analyse.extract_tags(doc, topK=None, withWeight=True)
        if len(kw) >= top_k:
            kw = kw[:top_k]
        else:
            for i in range(top_k - len(kw)):
                kw.append(kw[-1])
        total = sum([x[1] for x in kw])
        mean_tfidf = total / len(kw)
        return mean_tfidf * punish

    def rank(self, top=None, reverse=True):
        docs = self.data_prepare()

        results = [(self.mean_tfidf(doc, top_k=self.N), self.documents[i])
                   for i, doc in enumerate(docs)]
        results = sorted(results, key=lambda x: x[0], reverse=reverse)

        if not top:
            return results
        else:
            return results[:top]
