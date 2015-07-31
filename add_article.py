#!/usr/bin/env python
import os
import sys
from django.core.wsgi import get_wsgi_application
from blog.models import *
import time

ARTICLE_DIR = os.path.join(os.path.dirname(__file__),'blog/articles')
def getFile():
    file_list = []
    new_timetuple = 0
    timetuple = update_timetuple.objects.get(update_type='article')

    for dirpath,dirnames,filenames in os.walk(ARTICLE_DIR):
        for filename in filenames:
            filetime =  os.stat(os.path.join(dirpath,filename)).st_mtime
            if filetime > timetuple.time:
                if filetime > new_timetuple:
                    new_timetuple = filetime
	            print 'new_time:',new_timetuple
                file_list.append(os.path.join(dirpath,filename))
		print os.path.join(dirpath,filename)
    if new_timetuple != 0:    
        timetuple.time = new_timetuple
        print 'timetuple:',timetuple.time
        timetuple.save()
    return file_list


def update_tags(tag_list):
    tag_obj_list = []
    for tag in tag_list:
        if tag[-1] == '\n':
            tag = tag[:-1]
        try:
            obj = ArticleTags.objects.get(tag_name=tag)
        except ArticleTags.DoesNotExist:
            obj = ArticleTags.objects.create(tag_name=tag)
        tag_obj_list.append(obj)

    return tag_obj_list


def update_articles(path):
    article_file = open(path,'r')

    article = article_file.readlines()
    article_file.close()
    article_title = article[0][:-1]
    article_content = ''
    preview_index = 1

    for index,content in enumerate(article[2:]):
        if content[0:2] == '@@':
            preview_index = index
            content = content[2:]
        article_content = article_content + content

    tag_list = article[1].split(' ')
    article_tag = update_tags(tag_list)

    try:
        article_obj = Article.objects.get(title=article_title)
    except Article.DoesNotExist:
        article_obj = Article.objects.create(title=article_title,content=article_content,preview_line=preview_index)
    else:
        article_obj.content = article_content
        article_obj.preview_line = preview_index
        article_obj.save()

    for tag_obj in article_tag:
        article_obj.tag.add(tag_obj)


def main():
    file_list = getFile()
    for filepath in file_list:
        update_articles(filepath)
    print 'DONE!'
    


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'disoul_blog.settings'
    application = get_wsgi_application() 
    sys.exit(main())
