# from django.template import Template, Context
# from django.http import HttpResponse
# import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)


# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
# import datetime
# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)

from django.shortcuts import render
import datetime
# import MySQLdb
def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,'current_datetime.html', {'current_date': now},locals())


# def book_list(request):
#     db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
#     cursor = db.cursor()
#     cursor.execute('SELECT name FROM books ORDER BY name')
#     names = [row[0] for row in cursor.fetchall()]
#     db.close()
#     return render(request,'book_list.html', {'names': names})