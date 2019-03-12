import  xlrd

workbook = xlrd.open_workbook(r'../data/0306.xls')
sheet = workbook.sheet_by_name('Sheet2')
print(sheet.name, sheet.nrows, sheet.ncols)


point_insert_list = []
update_user_list = []

for i in range(0, sheet.nrows):
    rows = sheet.row_values(i)
    #取出每一样的数据

    str2 = 'insert into `integral`(`integral_type`, `admin_user_id`, `admin_user_name`, `web_user_id`, `web_user_name`, `total_integral`, `available_integral`, `create_time`, `record_type`, `reason`, `message_code`)' \
           ' values(30, 5, \'小旦\', (select user_id from user where mobile = \'%s\'), \'%s\', \'+%d\', \'+%d\', \'2018-12-31 16:25:20\', 1, \'Yisrc\', \'\');' % (int(rows[1]), rows[2],int(rows[4]), int(rows[4]))

    point_insert_list.append(str2)


    str3 =  'update user set total_integral = (total_integral + %d ), available_integral = (available_integral + %d) where mobile = \'%s\';' % (int(rows[4]), int(rows[4]), str(int(rows[1])))
    update_user_list.append(str3)
    #更新数据库


print(len(point_insert_list))


for _ in point_insert_list:
    print(_)
