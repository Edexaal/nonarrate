from lib.arg import CLIParser, ArgChecker, ArgAssembler
from lib.file import Writer, FileExecutor, RenpyReader
from lib.narrator_handler import NarratorHandler
from lib.validator.speaker import ObjectStrategy


def run():
    parser = CLIParser()
    arg_namespace = parser.parse_args()
    reader = RenpyReader()
    file_executor = FileExecutor()
    if arg_namespace.folder_or_file.is_file() and arg_namespace.folder_or_file.name == "errors.txt":
        file_executor.fix_errors(arg_namespace.folder_or_file, reader)
        return
    ArgChecker.check_args(arg_namespace)
    ArgAssembler.assemble(arg_namespace)
    writer = Writer()
    writer.backup_dir(arg_namespace)
    file_infos = file_executor.file_lines(reader, arg_namespace.folder_or_file)
    ObjectStrategy.define_speakers(file_infos)
    narrator_handler = NarratorHandler()
    file_infos = narrator_handler.remove(file_infos, arg_namespace)
    file_executor.write_files(writer, file_infos)


if __name__ == "__main__":
    run()
