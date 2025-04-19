import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


with open("books/meta_data.json", "r", encoding="utf-8") as my_file:
    books = json.load(my_file)


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        books=books
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
