import os
import subprocess
import re
import threading

def get_all_files():
    files = list()
    for item in os.walk('test'):
        for file in item[2]:
            files.append(f"{item[0]}/{file}")
    return files


def find_emails_in_file(path):
    with open(path) as file:
        lines = file.readlines()
    for line in lines:
        if re.match('.+@.+\..+', line):
            print(line.strip())


def task1():
    # в папке test найти все файлы filenames вывести колличество
    files_count = 0
    for item in os.walk('test'):
        for file in item[2]:
            if file.startswith('filenames'):
                files_count += 1
    print(files_count)


def task2():
    # в папке test найти все email адреса записанные в файлы

    # 1 способ
    print('-------------------------------------')
    emails = subprocess.check_output('grep -E -o -r "\\b[A-Za-z0-9._%+-]+@[A-Za-z'
                                     '0-9.-]+\.[A-Za-z]{2,6}\\b" test/', shell=True).splitlines()
    for email in emails:
        print(email.decode('utf-8'))
    print('-------------------------------------')
    # 2 способ
    files = get_all_files()
    for file_path in files:
        find_emails_in_file(file_path)
    print('-------------------------------------')
    # 3 способ
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)
    threads = list()
    files = get_all_files()
    for file_path in files:
        thread = threading.Thread(target=find_emails_in_file, args=(file_path,))
        threads.append(thread)
        thread.start()
    for thread in threads:
         thread.join()
    print('-------------------------------------')

if __name__ == '__main__':
    task1()
    task2()
