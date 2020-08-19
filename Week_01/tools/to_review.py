import re
from re import template
from pprint import pprint


def get_status():
    """
    get leetcode quizs' status.
    """

    with open(r"D:\mozli\Documents\GitHub\Python_Repo\LeetCode\leetcode.taskpaper", "r", encoding='utf-8') as f:
        data = f.read()
        quiz_status = re.findall(r"\d{3}.*#\d", data)

    status_dict = {}
    for item in quiz_status:
        temp_list = item.split('#')
        already = status_dict.get(temp_list[0], 0)
        if already < int(temp_list[1]):
            status_dict[temp_list[0]] = int(temp_list[1])
        
    return sorted(status_dict.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    pprint(get_status())

