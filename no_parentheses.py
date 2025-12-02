import os
import re
import sys

game_dir = sys.argv[1]

def get_files():
    invalid_folders = {'tl', 'menu', 'gui', 'saves', 'images', 'cache', "fonts", "voices", "functions","music"}
    invalid_files = {'gui.rpy', 'options.rpy', 'screens.rpy','images.rpy'}
    rpy_file_ext = 'rpy'
    renpy_files = []
    for dirpath, sub_dir_names, file_names in os.walk(game_dir):
        if any([x in dirpath for x in invalid_folders]):
            continue
        for file_name in file_names:
            if file_name.endswith(rpy_file_ext) and file_name not in invalid_files:
                renpy_files.append(os.path.join(dirpath, file_name))
    return renpy_files

def modify_files():
    parenthesis_pat = re.compile(r'^[^=]+"\([^)]+\)"$')
    file_urls = get_files()
    cleaned_lines = []
    changed_urls = set()
    for file_url in file_urls:
        lines = []
        with open(file_url, encoding="utf-8") as f:
            lines = f.readlines()

        is_menu = False
        for line in lines:
            strip_line = line.strip()

            # jacob happy "(this is a narrator dialogue)"
            if is_menu or not parenthesis_pat.match(strip_line):
                cleaned_lines.append(line)
            elif file_url not in changed_urls:
                changed_urls.add(file_url)

            # Keeps the narrator during choice menu appearance
            if strip_line.startswith("menu:"):
                is_menu = True
            elif is_menu and len(strip_line) != 0:
                is_menu = False

        if len(cleaned_lines) != 0 and len(changed_urls) != 0:
            with open(file_url, 'w',encoding="utf-8") as f:
                f.writelines(cleaned_lines)
        cleaned_lines.clear()
    return changed_urls

def get_indent_num(line):
    return len(line) - len(line.lstrip())

def clean_up(changed_files):
    for file_url in changed_files:
        cleaned_lines = []
        lines = []

        with open(file_url,encoding="utf-8") as f:
            lines = f.readlines()

        prev_line = dict()
        for line in lines:
            strip_line = line.strip()
            if strip_line.endswith(':') and not len(prev_line):
                prev_line['line'] = line
                prev_line['indent'] = get_indent_num(line)
            elif strip_line.endswith(':') and len(prev_line):
                line_indent_num = get_indent_num(line)
                if prev_line['indent'] < line_indent_num:
                    cleaned_lines.append(prev_line['line'])
                    cleaned_lines.append(line)
                elif prev_line['indent'] > line_indent_num:
                    cleaned_lines.append(line)
                prev_line.clear()
            elif len(prev_line):
                line_indent_num = get_indent_num(line)
                if prev_line['indent'] < line_indent_num:
                    cleaned_lines.append(prev_line['line'])
                    cleaned_lines.append(line)
                elif not strip_line:
                    cleaned_lines.append(prev_line['line'])
                else:
                    cleaned_lines.append(line)

                prev_line.clear()
            else:
                cleaned_lines.append(line)

        with open(file_url, 'w',encoding="utf-8") as f:
            f.writelines(cleaned_lines)


if __name__ == "__main__":
    changed_files = modify_files()
    clean_up(changed_files)
