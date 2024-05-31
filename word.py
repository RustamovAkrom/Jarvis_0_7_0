import yaml
import os

commands_search = dict(yaml.safe_load(open("search_commands.yaml", "rt", encoding="utf-8")))
commands = dict(yaml.safe_load(open("commands.yaml", "rt", encoding="utf-8")))

os.startfile("Asistent/ahk\\screenshot.exe")
# for i in commands.items():
#     print(i[1][0])
# def is_search_activator(text: str) -> dict:
#     data = {}
#     for command, value in commands_search.items():
#         for v in value:
#             if v in text:
#                 data['value'] = command
#                 data['commanda'] = text.strip(v)

#     return data

# output = is_search_activator("Hello World!")
# if output:
#     print(output)
