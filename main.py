from lib.arg import CLIParser, ArgChecker, ArgAssembler
from lib.file import Writer, FileExecutor, RenpyReader


def run():
    parser = CLIParser()
    arg_namespace = parser.parse_args()
    if arg_namespace.folder_or_file.is_file() and arg_namespace.folder_or_file.name == "errors.txt":
        # TODO: Place error_fixer feature here!
        return
    ArgChecker.check_args(arg_namespace)
    ArgAssembler.assemble(arg_namespace)
    writer = Writer()
    writer.backup_dir(arg_namespace)
    file_executor = FileExecutor()
    reader = RenpyReader()
    file_infos = file_executor.file_lines(reader, arg_namespace.folder_or_file)
    # TODO: Place narration remover logic here!


if __name__ == "__main__":
    run()
