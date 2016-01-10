import urllib.request
import json
from gitstar.models import Stargazer
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def stargazer_count(self, url):
        request = url
        response = urllib.request.urlopen(request)
        str_response = response.readall().decode('utf-8')
        obj = json.loads(str_response)
        return obj['stargazers_count']

    def user_list(self, owner, repo, page, per_page):
        request = 'https://api.github.com/repos/' + owner + '/' + repo
        request += '/' + 'stargazers?page=' + page + '&per_page=' + per_page
        response = urllib.request.urlopen(request)
        str_response = response.readall().decode('utf-8')
        objects = json.loads(str_response)
        usr_list = []
        for obj in objects:
            usr_list.append(obj['login'])
        return usr_list

    def master_user_list(self, owner, repo, star_count, per_page):
        total_page = int(int(star_count) / int(per_page) + 1)
        master_usr_list = []
        for x in range(1, 1 + 1):
            master_usr_list += self.user_list(owner, repo, str(x), per_page)
        return master_usr_list

    def create_db_user(self, master_usr_list):
        for user in master_usr_list:
            request = 'https://api.github.com/users/' + user
            response = urllib.request.urlopen(request)
            str_response = response.readall().decode('utf-8')
            obj = json.loads(str_response)
            print(obj)
            print(len(Stargazer.objects.filter(login=obj['login'])))
            if len(Stargazer.objects.filter(login=obj['login'])) == 0:
                if obj['company'] == 'null'or obj['company'] is None:
                    obj['company'] = ""
                if obj['blog'] == 'null' or obj['blog'] is None:
                    obj['blog'] = ""
                if obj['location'] == 'null' or obj['location'] is None:
                    obj['location'] = ""
                if obj['email'] == 'null' or obj['email'] is None:
                    obj['email'] = ""
                django_obj = Stargazer.objects.create(login=obj['login'],
                                                      avatar_url=obj['avatar_url'],
                                                      url=obj['url'],
                                                      html_url=obj['html_url'],
                                                      name=obj['name'],
                                                      company=obj['company'],
                                                      blog=obj['blog'],
                                                      location=obj['location'],
                                                      email=obj['email'],
                                                      followers=obj['followers'],
                                                      following=obj['following'])
                django_obj.save()

    def handle(self, *args, **options):
        url = 'https://api.github.com/repos/django-oscar/django-oscar'
        star_count = self.stargazer_count(url)
        master_usr_list = self.master_user_list('django-oscar', 'django-oscar', star_count, '30')
        self.create_db_user(master_usr_list)
