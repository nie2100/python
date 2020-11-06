import wordcloud
import jieba

txt = open('关于实施乡村振兴战略的意见.txt').read()

w = wordcloud.WordCloud(width=1000, font_path='wqy-microhei.ttc', height=700,background_color='white')
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('关于实施乡村振兴战略的意见.png')