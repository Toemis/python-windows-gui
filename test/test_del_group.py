import random


def test_del_group(app):
    if len(app.groups.get_group_list()) <= 1:
        app.groups.add_new_group("one more")
    old_list = app.groups.get_group_list()
    group_index = random.randint(0, len(old_list)-1)
    # print(len(old_list))
    # print(group_index)
    app.groups.delete_group(group_index)
    new_list = app.groups.get_group_list()
    old_list.pop(group_index)
    assert sorted(old_list) == sorted(new_list)
