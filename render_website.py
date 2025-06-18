import json
import os
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def on_reload():
    with open("meta_data.json", "r", encoding="utf-8") as my_file:
        books = json.load(my_file)
    os.makedirs('pages', exist_ok=True)
    pages = list(chunked(books, 10))
    all_pages = len(pages)
    for page, books_page in enumerate(pages):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template('template.html')

        rendered_page = template.render(
            books=books_page,
            all_pages=all_pages,
            page_number=page+1
        )

        with open(f'pages/index{page+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()
