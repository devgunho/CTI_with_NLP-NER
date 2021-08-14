import datetime
import os
import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse


def load_url_list():
    url_list = ['https://www.microsoft.com/security/blog/2021/08/25/cybersecuritys-next-fight-how-to-protect-employees-from-online-harassment/',
                'https://www.fireeye.com/current-threats/apt-groups.html',
                'https://attack.mitre.org/techniques/enterprise/',
                'https://security.googleblog.com/',
                'https://www.securitymagazine.com/blogs/14-security-blog',
                'https://www.securitymagazine.com/topics/2786-management'
                ]
    return url_list


def run_crawling():
    blacklist = [
        'style',
        'script',
        # other elements,
    ]

    url_list = load_url_list()

    for target_url in url_list:
        req = requests.get(
            target_url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        text_elements = [t for t in soup.find_all(
            text=True) if t.parent.name not in blacklist]
        full_text = ''.join(str(e) for e in text_elements)

        # urlparse
        url = urlparse(target_url)
        # print(url.netloc, url.path)
        parent_dir = "./text_data"
        path = os.path.join(parent_dir, url.netloc)
        # print(path)
        if not os.path.isdir(path):
            os.mkdir(path)

        # crawling date
        # d = datetime.datetime.now()
        filename = url.path
        # filename += '-'+str(d.year)+'-' + \
        #     str(d.month)+'-'+str(d.day)
        filename = filename.replace("/", "_")
        filename += '.txt'
        # print(filename)

        # write
        complete_filename = os.path.join(path, filename)
        print("[+] Stacking", complete_filename)
        with open(complete_filename, "w",  encoding='utf-8') as file:
            file.write(str(full_text))


if __name__ == "__main__":
    run_crawling()
