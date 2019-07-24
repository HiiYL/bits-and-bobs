import os
from os.path import expanduser

user_root = expanduser("~")
project_roots = [
                 '{user_root}/Projects',
                 '{user_root}/code/go/src/github.com/carousell',
]
output_file = '{user_root}/.project_shortcuts'

EXCLUDED_FOLDERS = ['.DS_Store']
TEMPLATE = \
"""
{shortcut}() {{
    cd {path}
    title {title}
}}
"""
SHORTCUT_PREFIX = "_"


# format
project_roots = [root.format(**{"user_root": user_root})
                 for root in project_roots]
output_file = output_file.format(**{"user_root": user_root})

project_shortcuts = {}
for root in project_roots:
    project_folders = os.listdir(root)
    for project_folder in project_folders:
        if project_folder not in EXCLUDED_FOLDERS:
            project_path = '{}/{}'.format(root, project_folder)
            # snake case
            project_name_in_words = project_folder.split("_")
            if len(project_name_in_words) <= 1:
                project_name_in_words = project_folder.split("-")
            uppercase_in_project_name = [
                a for a in project_folder if a.isupper()
            ]
            if len(project_name_in_words) > 1:
                shortcut = "".join([word[0] for word in project_name_in_words])
            elif len(uppercase_in_project_name) > 1:
                shortcut = "".join(uppercase_in_project_name)
            else:
                shortcut = "".join([s for s in project_folder[:2]])

            shortcut = shortcut.lower()
            shortcut = SHORTCUT_PREFIX + shortcut

            if shortcut not in project_shortcuts:
                project_shortcuts[shortcut] = {
                    "path": project_path,
                    "title": project_folder
                }
            else:
                print("conflict: {} -> {} ({})".format(
                    project_path,
                    project_shortcuts[shortcut],
                    shortcut)
                )

to_write = ""
for shortcut, project in project_shortcuts.items():
    to_write += TEMPLATE.format(**{
        "shortcut": shortcut,
        "path": project["path"],
        "title": project["title"],
    })
    to_write += "\n"

with open(output_file, 'w') as f:
    f.writelines(to_write)

print("{} entries written".format(len(project_shortcuts)))
print("note(*): To work correctly, ensure 'source {}' is added to your .bash_profile".format(output_file))
