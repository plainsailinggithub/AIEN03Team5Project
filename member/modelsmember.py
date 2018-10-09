from django.db import connection

class Member:
    def all(self):
        with connection.cursor() as cursor:
            sql = '''select * from members'''
            cursor.execute(sql)
            members = cursor.fetchall()
        return members
    def single(self,id):
        with connection.cursor() as cursor:
            sql = """select * from members where id=%s"""
            #tuple
            cursor.execute(sql,(id,))
            member = cursor.fetchone()
        return member
    def update(self,member):
        with connection.cursor() as cursor:
            sql = """update members set gender=%s,company=%s,companyen=%s,position=%s,positionen=%s,skill=%s,language=%s
                     where id=%s"""
            #tuple
            cursor.execute(sql,member)
    def delete(self,id):
        with connection.cursor() as cursor:
            sql = '''delete from members where id=%s'''
            cursor.execute(sql,(id,))
    def create(self,member):
        with connection.cursor() as cursor:
            sql = '''insert into members(mem_name,emailid,password)values(%s,%s,%s)'''
            cursor.execute(sql,member)
    def updatephoto(self,member):
        with connection.cursor() as cursor:
            sql = """update members set img=%s
                     where id=%s"""
            #tuple
            cursor.execute(sql,member)
    