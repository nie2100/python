#BeautifulSoup库解析器

bs4的HTML解析器             BeautifulSoup(mk,'html.parser')         安装bs4库
lxml的HTML解析器            BeautifulSoup(mk,'lxml')                pip install lxml
lxml的XML解析器             BeautifulSoup(mk,'xml')                 pip install lxml
html5lib的解析器            BeautifulSoup(mk,'html5lib')            pip install html5lib

#Beautiful Soup类的基本元素

tag                        标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
Name                       标签的名字，<p>...</p>的名字是'p'，格式：<tag>.name
Attributes                 标签的属性，字典形式组织，格式：<tag>.attrs
NavigableString            标签内非属性字符串，<>..</>中字符串，格式：<tag>.string
Comment                    标签内字符串的注释部分，一种特殊的Comment类型


    标签树的下行遍历

        .contents                  子节点的列表，将<tag>所有儿子节点存入列表
        .children                  子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
        .descendants               子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

    标签树的上行遍历

        .parent                    节点的父亲标签
        .parents                   节点先辈标签的迭代类型，用于循环遍历先辈节点

    标签树的平行遍历

        .next_sibling              返回按照HTML文本顺序的下一个平行节点标签
        .previous_sibling          返回按照HTML文本顺序的上一个平行节点标签
        .next_siblings             迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
        .previous_siblings         迭代类型，返回按照HTML文本顺序的前序所有平行节点标签

#BeautifulSoup Soup类的基本方法

<>.prettify()                                           对内容进行美化
<>.find_all(name,attrs,recursive,string,**kwargs)       返回一个列表类型，储存查找的结果。

        name                        对标签名称的检索字符串
        attrs                       对标签属性值的检索字符串，可标注属性检索。
        recursive                   是否对子孙全部检索，默认True
        string                      <>...</>中字符串区域的检索字符串
        <tag>(..)   等价于     <tag>.find_all(..)
        soup(..)    等价于     soup.find__all(..)