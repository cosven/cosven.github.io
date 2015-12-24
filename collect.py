#!/usr/bin/env python3

import os
import shutil


home_dir = os.path.expanduser('~')
src_dirs = [
    os.path.join(home_dir, 'Dropbox/notes/sources'),
    os.path.join(home_dir, 'Dropbox/diary')
    ]
dst_dir = os.path.join(home_dir, 'cosven.github.io')

html_index_path = os.path.join(dst_dir, 'index.html')


def get_htmls():
    html_files = []
    for src_dir in src_dirs:
        files = os.listdir(src_dir)
        for f in files:
            if f.split('.')[-1] in ('html', 'HTML'):
                file_path = os.path.join(src_dir, f)
                last_modify = os.path.getmtime(file_path)
                html_files.append((file_path, last_modify))
    return sorted(html_files, key=lambda f: f[1], reverse=True)


def copy_htmls(html_files):
    for f, last_modify in html_files:
        basename = os.path.basename(f)
        try:
            shutil.copyfile(f, os.path.join(dst_dir, basename))
        except Exception as e:
            print(str(e))


def generate_htmls_index(html_files):
    index = ''
    for f, last_modify in html_files:
        basename = os.path.basename(f)
        name = basename.split('.')[0]
        index_template = '<li><a href="%s">%s</a></li>\n' % (basename, name) 
        index += index_template

    template = """
    <!DOCTYPE HTML>
    <html>
        <head></head>
        <body>
        <h1>闲杂笔记等均基于此</h1>
        <h2>
            <code>
            Cosven / ysw / zjuysw
            </code>
        </h2>
        <ul>
            %s
        </ul>
        </body>
    </html>
    """ % index
    with open(html_index_path, 'w') as f:
        f.write(template)


if __name__ == '__main__':
    html_files = get_htmls()
    copy_htmls(html_files)
    generate_htmls_index(html_files)
