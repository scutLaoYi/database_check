#!/usr/bin/python
# -*- encoding=utf-8 -*-

import MySQLdb


def getElement(data):
	pieces = data.split(':')
	return pieces[1].strip(' \n')

def configReading():
	try:
		file = open('config.ini')

		config = {}
		for line in file:
			if line.startswith('#'):
				continue
			if line.startswith('Host'):
				config['Host'] = getElement(line)
			if line.startswith('User'):
				config['User'] = getElement(line)
			if line.startswith('Password'):
				config['Pass'] = getElement(line)
			if line.startswith('Database'):
				config['Database'] = getElement(line)
				
		file.close()

	except IOError as e:
		print "config file reading failed!"
		print e
		return False

	return config

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

def mainFunc(config):
	#connect:
	try:
		db = MySQLdb.connect(
				host= config['Host'], 
				user= config['User'], 
				passwd= config['Pass'], 
				db = config['Database'],
				)
		cur = db.cursor()

	except MySQLdb.Error as e:
		print "something wrong when try to connect the database..."
		print e
		return 

	try:
		allTables = listTables(cur) 
		for table in allTables:
			print "-----------", table[0], "--------------"
			desc = describeTable(cur, table[0])
			printTableInfo(desc)
			print "----------------------------------------"

	except MySQLdb.Error as e:
		print "something wrong when executing..."
		print e

	finally:
		#close:
		db.close()
		cur.close()

if __name__ == "__main__":
	config = configReading()
	if config:
		print "config reading ok. now try to connect the database..."
		mainFunc(config)
	else:
		print "exit!"
