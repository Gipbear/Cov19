import time

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


if __name__ == '__main__':
    print(get_c1_data())
