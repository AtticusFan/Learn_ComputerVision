import sqlite3
from datetime import datetime

def db_save(db, name):
    connect = sqlite3.connect(db)
    sql = 'CREATE TABLE IF NOT EXISTS mytable \
            ("姓名" TEXT, "打卡時間" TEXT)'
    connect.execute(sql)
    save_time = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    sql = f'insert into mytable values("{name}", "{save_time}")'
    connect.execute(sql)        
    connect.commit()            
    connect.close()              
    print('儲存成功')
db_save('mydatabase.sqlite', '曹家憲')                       # 自行輸入名字到資料庫

def db_check(db):
    try:
        connect = sqlite3.connect(db)
        sql = 'select * from mytable'
        cursor = connect.execute(sql)
        dataset = cursor.fetchall()
        print('姓名\t時間')
        print('----\t  ----')
        for data in dataset:
            print(f"{data[0]}\t{data[1]}")
    except:
        print('讀取資料庫錯誤')
    connect.close()
db_check('mydatabase.sqlite')
