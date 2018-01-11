from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import dbaseconf
import psycopg2
import json

# Create your views here.

connection = dbaseconf.connection

def insertcontent(request):
    req = request.GET
    title = req.get('title')
    content = req.get('content')

    dbase = connection()
    dbase.cur.execute("""
        INSERT INTO pythoncontent (title, content)
        VALUES (%s, %s) RETURNING id;       
        """,
        (title, content)
    )
    ids = dbase.cur.fetchone()       # RETURNING id 小技巧 可以取得最后插入的这条记录的ID ids[0]就是id的值
    dbase.conn.commit()
    dbase.conn.close()
    dbase.cur.close()

    mydata = {'success':True,'message':'提交成功！', 'data':[{
        'title':title,
        'content':content,
        'id':ids[0]
    }]}
    return HttpResponse(json.dumps(mydata), content_type="application/json")

def getcontent(request):
    dbase = connection()
    dbase.cur.execute("SELECT * FROM pythoncontent;")
    alldata = dbase.cur.fetchall()
    dbase.conn.commit()
    dbase.conn.close()
    dbase.cur.close()

    dataList = []
    for i in alldata :
        dataList.append({
            'id' : i[2],
            'title' : i[0],
            'content' : i[1]
        })

    mydata = {'success':True,'message':'提交成功！', 'data':dataList}
    return HttpResponse(json.dumps(mydata), content_type="application/json")

def delcontent(request):
    req = request.GET
    ids = req.get('id')

    dbase = connection()
    dbase.cur.execute("DELETE FROM pythoncontent WHERE id=%s;", [(ids)])
    dbase.conn.commit()
    dbase.conn.close()
    dbase.cur.close()

    mydata = {'success':True,'message':'删除成功！'}
    return HttpResponse(json.dumps(mydata), content_type="application/json")

def updatecontent(request):
    req = request.GET
    ids = req.get('id')
    title = req.get('title')
    content = req.get('content')

    dbase = connection()
    dbase.cur.execute("UPDATE pythoncontent SET title=%s, content=%s WHERE id=%s;", (title, content, ids))
    dbase.conn.commit()
    dbase.conn.close()
    dbase.cur.close()

    mydata = {'success':True,'message':'更新成功！'}
    return HttpResponse(json.dumps(mydata), content_type="application/json")
