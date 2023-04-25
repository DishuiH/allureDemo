import uuid
import time

import psycopg2

conn = psycopg2.connect(database="service_notification", user="mamoru", password="Uber=!=55",
                        host="mamoru-dev-instance-1.cnal5cl42wcb.ap-east-1.rds.amazonaws.com", port="5432")
cur = conn.cursor()
# 执行查询命令
cur.execute("SELECT code,content,subject FROM public.templates where channel = 'C_EMAIL' order by subject;")
rows = cur.fetchall()
p = 145
for i in rows:
    code = i[0]
    id = uuid.uuid4()
    print(id)
    break
    # updated_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '.000'
    # sql = "update public.templates set id = '{}' where id = '{}';" .format(id,p)
    # p += 1
    # cur.execute(sql)
    # print(id, i[0], "add successful")
    # conn.commit()


