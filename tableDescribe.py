#!/usr/bin/python
# -*- encoding=utf-8 -*-

import MySQLdb

#config:
curHost = "10.0.0.4"
curUser = "shengwu"
curPass = "qfire"
curDb = "cake_db"


def listTables(cur):
	cur.execute("""show tables;""")
	result = cur.fetchall()
	return result

def describeTable(cur, tableName):
	cur.execute("""describe %s;""" % tableName)
	result = cur.fetchall()
	return result

def printTableInfo(table):
	for info in table:
		print '\t', info[0],'\t' ,info[1],'\t', info[3]

def mainFunc():
	#connect:
	db = MySQLdb.connect(
			host= curHost, 
			user= curUser, 
			passwd= curPass, 
			db = curDb,
			)
	cur = db.cursor()

	allTables = listTables(cur) 
	for table in allTables:
		print "-----------", table[0], "--------------"
		desc = describeTable(cur, table[0])
		printTableInfo(desc)
		print "----------------------------------------"

	#close:
	db.close()
	cur.close()

if __name__ == "__main__":
	mainFunc()
