import time

import numpy as np
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    """封装创建数据库连接和游标"""
    # 建立连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='cov')
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    """封装关闭数据库连接和游标"""
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    """封装通用查询"""
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_c1_data():
    """获取最新数据"""
    sql = """
    select sum(confirm),
           (select suspect from history order by ds desc limit 1),
           sum(heal),
           sum(dead)
    from details
    where update_time = (select update_time from details order by update_time desc limit 1)
    """
    res = query(sql)
    return res[0]


def get_c2_data():
    """返回各省数据"""
    sql = """
    select province, sum(confirm)
    from details
    where update_time = (select update_time
                         from details
                         order by update_time desc
                         limit 1)
    group by province
    """
    res = query(sql)
    return res


def get_l1_data():
    """返回每日新增数"""
    sql = """
    select ds, confirm, suspect, heal, dead
    from history
    """
    res = query(sql)
    return res


def get_l2_data():
    """返回每日新增数"""
    sql = """
    select ds, confirm_add, suspect_add
    from history
    """
    res = query(sql)
    return res


def get_r1_data():
    """返回非湖北城市确诊人数top5"""
    sql = """
    select city, confirm
    from (select city, confirm
          from details
          where update_time = (select update_time
                               from details
                               order by update_time desc
                               limit 1)
            and province not in ('湖北', '北京', '上海', '天津', '重庆')
          union all
          select province as city, sum(confirm) as confirm
          from details
          where update_time = (select update_time
                               from details
                               order by update_time desc
                               limit 1)
            and province in ('北京', '上海', '天津', '重庆')
          group by province) as a
    order by confirm desc
    limit 5
    """
    res = query(sql)
    return res


def get_r2_data():
    """返回热搜词频"""
    sql = """
    select content, hot from hotsearch order by id desc  limit 20;
    """
    res = query(sql)
    return res


if __name__ == '__main__':
    res = get_c2_data()
    data = []
    res_num = []
    per_num = [0]
    per = []
    for tup in res:
        data.append({'name': tup[0], 'value': int(tup[1])})
        res_num.append(int(tup[1]))
    da = np.array(res_num)
    per_num.append(np.percentile(da, 25))
    per_num.append(np.median(da))
    per_num.append(np.percentile(da, 75))
    per_num.append(np.percentile(da, 95))
    for i in range(len(per_num) - 1):
        per.append({'start': per_num[i], 'end': per_num[i + 1]})
    per.append({'start': per_num[-1]})
    print(per)
