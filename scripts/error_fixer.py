import os
import sys
import re

errors_txt = sys.argv[1]
dest_pat = re.compile(r'(?:and )?File\s+.+(game/.+\.rpy)')
line_num_pat = re.compile(r'.+line (\d+):')
type_pat = re.compile(r'.+(non-empty|Line is indented)')


def add_error(error_dict, error):
    if not error['loc']:
        return
    if error['loc'] not in error_dict:
        error_dict[error['loc']] = [error]
    else:
        error_dict[error['loc']].append(error)


def get_error(line):
    error = dict()
    error['loc'] = dest_pat.match(line).group(1) if dest_pat.match(line) else None
    error['line_num'] = int(line_num_pat.match(line).group(1)) if line_num_pat.match(line) else None
    error['type'] = type_pat.match(line).group(1) if type_pat.match(line) else None
    if not error['type'] and line.startswith("and File"):
        error['type'] = 'duplicate'
    return error


def get_errors():
    error_dict = dict()
    lines = []
    with open(errors_txt, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        strip_line = line.strip()
        if not strip_line.startswith('File') and not strip_line.startswith("and File"):
            continue
        error = get_error(line)
        add_error(error_dict,error)
    return error_dict


def correct_errors(errors):
    project_dir = os.path.dirname(errors_txt)
    for key in errors.keys():
        lines = []
        current_file_loc = os.path.join(project_dir, key)
        with open(current_file_loc,encoding="utf-8") as f:
            lines = f.readlines()

        errors[key].reverse()
        for err in errors[key]:
            if 'non-empty' in err['type']:
                lines.pop(err['line_num'] - 1)
            elif 'Line is indented' in err['type']:
                line = lines[err['line_num'] - 1]
                lines[err['line_num'] - 1] = line[4:]
            elif 'duplicate' in err['type']:
                os.remove(current_file_loc)
                break

        if os.path.exists(current_file_loc):
            with open(current_file_loc, 'w', encoding="utf-8") as f:
                f.writelines(lines)


if __name__ == "__main__":
    # Must provide absolute path of errors.txt file
    if os.path.exists(errors_txt):
        errors = get_errors()
        correct_errors(errors)
