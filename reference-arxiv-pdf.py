#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import urllib.request


def download_arxiv_pdf(reference_content):
    """
    @param reference_content: 参考文件的文本字符串，形如：

    References
    [1] Pieter Abbeel and Andrew Y Ng. Inverse reinforcement learning. In Encyclopedia of machine
    learning, pages 554–558. Springer, 2011.
    [2] Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, and Mario Marchand.
    Domain-adversarial neural networks. arXiv preprint arXiv:1412.4446, 2014.
    [3] Grigory Antipov, Moez Baccouche, and Jean-Luc Dugelay. Face aging with conditional
    generative adversarial networks. arXiv preprint arXiv:1702.01983, 2017.
    [4] Martin Arjovsky and Léon Bottou. Towards principled methods for training generative
    adversarial networks. arXiv preprint arXiv:1701.04862, 2017.
    """
    idx = reference_content.find('arXiv:',  0)
    while idx > 0:
        idx_start = idx+6
        idx_end = reference_content.find(',', idx_start)
        arxiv_id = reference_content[idx_start:idx_end]
        url = "https://arxiv.org/pdf/{}.pdf".format(arxiv_id)
        print(url)
        # pdf_file_name = "arvix_{}.pdf".format(arxiv_id)
        # 从网上下载图片数据，并且，保存到本地文件
        # print("下载：%s" % url)
        # urllib.request.urlretrieve(url, "arvix_{}.pdf".format(arxiv_id))
        # print("保存到：%s" % pdf_file_name)
        idx = reference_content.find('arXiv:',  idx_start)


def download_reference(txt_file):
    """
    @param txt_file: 论文中，参考文件部分的文本内容。
    """

    # 读取文本文件内容
    file = open(txt_file, 'r')
    content = file.read()
    # 下载所有的arvix网站相关pdf文件
    download_arxiv_pdf(content)


download_reference('reference.txt')
