import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
conn= MySQLdb.connect(host='localhost',user='root',passwd='chenanzhe',db='web',port=3306,charset='utf8')
def insertDB(tableName = None, listOfColumns = [], listOfValues = [], sql = None):
	if sql != None:
		cur = conn.cursor()
		cur.execute(sql.decode('gbk').encode('utf-8') )
		conn.commit()
		cur.close()
	else:
		assert len(listOfColumns) == len(listOfValues)
		columns = ",".join(listOfColumns)
		values = "'"
		values += "','".join(listOfValues)
		values += "'"
		sql = """insert into {0}({1}) values({2})""".format(tableName,columns,values)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		cur.close()

def searchDB(tableName=None, columns = [], where = None,sql =None):
	if sql != None:
		cur = conn.cursor()
		cur.execute(sql.decode('gbk').encode('utf-8'))
		results = cur.fetchall()
	else:
		if where == None and columns == None:
			sql = "select * from {0}".format(tableName)
		elif where == None and columns != []:
			columns = ",".join(columns)
			sql = "select {0} from {1}".format(columns, tableName)
		elif where != None and columns == []:
			sql = "select * from {0} where {1}".format(tableName, where)
		else:
			columns = ",".join(columns)
			sql = "select {0} from {1} where {2}".format(columns, tableName, where)

		cur = conn.cursor()
		cur.execute(sql.decode('gbk').encode('utf-8') )
		results = cur.fetchall()
	return results

def deleteDB(tableName,where = None):
	if where == None :
		sql = "delete * from {0}".format(tableName)
	else:
		sql = "delete * from {0} where {1}".format(tableName, where)
	cur = conn.cursor()
	cur.execute(sql.decode('gbk').encode('utf-8') )
	results = cur.fetchall()
	return results