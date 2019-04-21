# tools
常用的工具

## reference-arxiv-pdf.py 用法
将论文中从“Reference”开始的内容，拷贝到文本文件“reference.txt”中，与reference-arxiv-pdf.py放在同一个文件夹下。

运行 <br>
``````./reference-arxiv-pdf.py reference.txt > url.txt``````<br>
生成一个url.txt文件，其中包含所要下载的arXiv中参考文件的链接，


运行以下命令，通过wget模拟浏览器下载。<br>
``````wget --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" -c -i url.txt``````<br>
即可将相关论批量下载到本地。


