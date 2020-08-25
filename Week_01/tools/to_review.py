import re
from re import template
from pprint import pprint
import datetime


def get_status():
    """
    get leetcode quizs' status.
    """

    with open(taskpaper, "r", encoding="utf-8") as f:
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
    with open(taskpaper, "r", encoding="utf-8") as f:
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
            task_formated = task.lstrip()[4:]
            tasks_dict[last_date].append(task_formated)

    return tasks_dict


def get_tasks_first_add():
    """
    获取任务第一次添加的日期。
    
    out:
    dict { '日期' : [任务1, 任务2, ...] ... }
    """

    with open(taskpaper, "r", encoding="utf-8") as f:
        data = f.readlines()

    tasks_dict = {}
    last_date = ""

    for item in data:
        if re.match(r"\d{4}-\d{2}-\d{2}", item):
            date = re.match(r"\d{4}-\d{2}-\d{2}", item).group()
            last_date = date
            tasks_dict[date] = []
        elif item != r"\n" and not re.match(r"^[ \n]*$", item):
            if "Week" not in item and item.split("#")[1][0] == "1":
                task = item.split("#")[0]
                task_formated = task.lstrip()[4:]
                tasks_dict[last_date].append(task_formated)
    return tasks_dict


def is_all_done():
    with open(taskpaper, "r", encoding="utf-8") as f:
        data = f.readlines()

    if data[-1][:5] == "  [ ]":
        return False
    elif data[-1][:5] == "  [x]":
        return True
    else:
        return "taskpaper not in right format."


def new_review():
    """
    add new todo
    """
    if is_all_done():
        one_day = datetime.timedelta(days=1)
        task_dict = get_tasks_first_add()

        dates_strlist = task_dict.keys()
        tasks_add_raw = []
        tasks_add_dict = {}
        for day_ in list(dates_strlist):
            today = datetime.datetime(
                datetime.datetime.today().year,
                datetime.datetime.today().month,
                datetime.datetime.today().day,
            )
            date_ = datetime.datetime.strptime(day_, "%Y-%m-%d")

            """
            review rule (by day):
                Day 1-3 +
                Day 4   x
                Day 5   +
                Day 6-7 x
                Day 8   +
                After repeat 5 times:
                    review every week
            """
            if today - date_ <= one_day * 3:
                tasks_add_raw.extend(task_dict[day_])
            elif today - date_ == one_day * 4:
                continue
            elif today - date_ == one_day * 5:
                tasks_add_raw.extend(task_dict[day_])
            elif one_day * 5 < today - date_ <= one_day * 7:
                continue
            elif today - date_ == one_day * 8:
                tasks_add_raw.extend(task_dict[day_])
            elif (today - date_) % 7 == 0:
                tasks_add_raw.extend(task_dict[day_])

        status = dict(get_status())
        for item in tasks_add_raw:
            repeat = status[item]
            if int(repeat) < 8:
                tasks_add_dict[item] = status[item] + 1
            else:
                continue

        return {k: v for k, v in sorted(tasks_add_dict.items(), key=lambda item: item[1])}

    else:
        return "Please complete all tasks."


def new_task_write_to_file():
    today_str = datetime.datetime.today().strftime("%Y-%m-%d")
    with open(taskpaper, "a", encoding="utf-8") as f:
        task_add_dict = new_review()
        f.write("\n\n")
        f.write(today_str + ":\n")
        for key in task_add_dict:
            line = "  [ ] " + key + "#" + str(task_add_dict[key])
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    taskpaper = r"D:\mozli\Documents\GitHub\Python_Repo\LeetCode\leetcode.taskpaper"
    print("status(length {}):".format(len(get_status())))
    pprint(dict(get_status()))
    # print("\nStatus:")
    # print("  all done." if is_all_done() else "  not all done.")
    # print()
    # pprint(get_tasks_by_day())
    pprint(get_tasks_first_add())
    # pprint(new_review())
    # new_task_write_to_file()

