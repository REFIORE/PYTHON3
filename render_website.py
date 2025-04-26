import json
import os
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


with open("books/meta_data.json", "r", encoding="utf-8") as my_file:
    books = json.load(my_file)


def on_reload():
    os.makedirs('pages', exist_ok=True)
    pages = list(chunked(books, 10))
    for page, books_page in enumerate(pages):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template('template.html')

        rendered_page = template.render(
            books=books_page
        )

        with open(f'pages/index{page}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


on_reload()
server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
