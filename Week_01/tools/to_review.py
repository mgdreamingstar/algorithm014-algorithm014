import re
from re import template
from pprint import pprint
from datetime import datetime


def get_status():
    """
    get leetcode quizs' status.
    """

    with open(
        r"D:\mozli\Documents\GitHub\Python_Repo\LeetCode\leetcode.taskpaper", "r", encoding="utf-8"
    ) as f:
        data = f.read()
        quiz_status = re.findall(r"\d{3}.*#\d", data)

    status_dict = {}
    for item in quiz_status:
        temp_list = item.split("#")
        already = status_dict.get(temp_list[0], 0)
        if already < int(temp_list[1]):
            status_dict[temp_list[0]] = int(temp_list[1])

    return sorted(status_dict.items(), key=lambda x: x[1], reverse=True)


def get_tasks_by_day():
    with open(
        r"D:\mozli\Documents\GitHub\Python_Repo\LeetCode\leetcode.taskpaper", "r", encoding="utf-8"
    ) as f:
        data = f.readlines()

    # today_str = datetime.today().strftime("%Y-%m-%d")
    # last_date = today_str
    tasks_dict = {}
    last_date = ""

    for item in data:
        if re.match(r"\d{4}-\d{2}-\d{2}", item):
            date = re.match(r"\d{4}-\d{2}-\d{2}", item).group()
            last_date = date
            tasks_dict[date] = []
        elif item != r"\n" and not re.match(r"^[ \n]*$", item):
            task = item.split("#")[0]
            task_formated = task.lstrip()
            tasks_dict[last_date].append(task_formated)

    return tasks_dict


def is_all_done():
    with open(
        r"D:\mozli\Documents\GitHub\Python_Repo\LeetCode\leetcode.taskpaper", "r", encoding="utf-8"
    ) as f:
        data = f.readlines()

    if data[-1][:5] == "  [ ]":
        return False
    elif data[-1][:5] == "  [x]":
        return True
    else:
        return "taskpaper not in right format."


if __name__ == "__main__":
    pprint(get_status())
    print("\nStatus:")
    print("  all done." if is_all_done() else "  not all done.")
    print()
    pprint(get_tasks_by_day())

