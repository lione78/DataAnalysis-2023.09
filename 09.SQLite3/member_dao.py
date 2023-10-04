#
#   member 테이블에 대한 Data Access Object(DAO)
#

import sqlite3 as sq

# member table에 있는 데이터 모두 가져오는 함수
def get_members():
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'select * from member'
    cur.execute(sql)
    results = cur.fetchall()
    
    cur.close()
    conn.close()

    return results

# ?세 미만의 데이터 가져오는 함수
def get_members_under_age(age):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'select * from member where age < ?'
    cur.execute(sql, (age, ))
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results

# mid에 해당하는 데이터 한 건 가져오기
def get_member_by_mid(mid):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'select * from member where mid = ?'
    cur.execute(sql, (mid, ))
    result = cur.fetchone()

    cur.close()
    conn.close()

    return result

# 데이터 추가하는 함수
def insert_member(params):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'insert into member(name, age) values(?, ?)'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

# 데이터 수정하는 함수
def update_member(params):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'update member set name=?, age=? where mid=?'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

# 데이터 삭제하는 함수
def delete_member_by_mid(mid):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'delete from member where mid=?'
    cur.execute(sql, (mid, ))
    conn.commit()

    cur.close()
    conn.close()


