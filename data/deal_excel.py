import  xlrd


workbook = xlrd.open_workbook(r'../data/0306.xls')
sheet_name = workbook.sheet_names()[0]
print(sheet_name)
sheet = workbook.sheet_by_index(1)
print(sheet.name, sheet.nrows, sheet.ncols)

#获取每一行的内容

user_insert_list = []
point_insert_list = []

for i in range(0, sheet.nrows):
    rows = sheet.row_values(i)
    #取出每一样的数据

    str = 'insert  into `user`(`mobile`, `nick_name`, `team`, `total_integral`, `available_integral`) ' \
          'values (\'%s\', \'%s\', \'%s\', +%d, +%d);' % (int(rows[1]), rows[2], rows[6] or 'NULL', int(rows[4]), int(rows[4]))

    user_insert_list.append(str)

    str2 = 'insert into `integral`(`integral_type`, `admin_user_id`, `admin_user_name`, `web_user_id`, `web_user_name`, `total_integral`, `available_integral`, `create_time`, `record_type`, `reason`, `message_code`)' \
           ' values(30, 5, \'小旦\', (select user_id from user where mobile = \'%s\'), \'%s\', \'+%d\', \'+%d\', \'2018-12-31 16:25:20\', 1, \'Yisrc\', \'\');' % (int(rows[1]), rows[2],int(rows[4]), int(rows[4]))

    point_insert_list.append(str2)


print(len(user_insert_list))
print(len(point_insert_list))


for _ in point_insert_list:
    print(_)

