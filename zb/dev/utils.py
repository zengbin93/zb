# coding: utf-8
import pandas as pd


def acl_bib2csv(file_bib):
    with open(file_bib, 'r', encoding="utf-8") as f:
        bib_list = f.read().strip().split("@")

    papers = []
    for bib in bib_list:
        if bib.startswith("inproceedings"):
            kvs = bib.split("\n")
            paper = dict()
            for kv in kvs:
                res = kv.split('=')
                if len(res) == 2:
                    k, v = res
                    paper[k.strip()] = v.strip(" \",")
            papers.append(paper)

    df = pd.DataFrame(papers)
    df_sel = df[['title', 'author', 'url', 'abstract', 'pages']]
    df_sel.to_excel(file_bib.replace(".bib", ".xlsx"), index=False)


if __name__ == '__main__':
    file_bib = r"C:\Users\zengb\Desktop\W19-41.bib"
    acl_bib2csv(file_bib)


