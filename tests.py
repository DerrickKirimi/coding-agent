from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
def main():
    working_dir = "calculator"
    print(get_file_content(working_dir, "lorem.txt"))
    #root_contents = get_files_info(working_dir)
    #print(root_contents)
    #pkg_contents = get_files_info(working_dir, "pkg")
    #pkg_contents = get_files_info(working_dir, "/bin")
    #print(pkg_contents)
    #pkg_contents = get_files_info(working_dir, "../")
    #print(pkg_contents)

main()