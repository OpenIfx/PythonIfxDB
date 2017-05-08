#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_311_InsertSelectDeleteNumLiterals(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_311)

  def run_test_311(self):
    # Make a connection
    conn = ifx_db.connect(config.database, config.user, config.password)

    if conn:
       ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_ON )

       # Drop the tab_num_literals table, in case it exists
       drop = 'DROP TABLE tab_num_literals'
       result = ''
       try:
         result = ifx_db.exec_immediate(conn, drop)
       except:
         pass
       # Create the animal table
       create = "CREATE TABLE tab_num_literals (col1 INTEGER, col2 FLOAT, col3 DECIMAL(7,2))"
       result = ifx_db.exec_immediate(conn, create)
   
       insert = "INSERT INTO tab_num_literals values ('11.22', '33.44', '55.66')"
       res = ifx_db.exec_immediate(conn, insert)
       print "Number of inserted rows:", ifx_db.num_rows(res)

       stmt = ifx_db.prepare(conn, "SELECT col1, col2, col3 FROM tab_num_literals WHERE col1 = '11'")
       ifx_db.execute(stmt)
       data = ifx_db.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         data = ifx_db.fetch_both(stmt)

       sql = "UPDATE tab_num_literals SET col1 = 77 WHERE col2 = 33.44"
       res = ifx_db.exec_immediate(conn, sql)
       print "Number of updated rows:", ifx_db.num_rows(res)

       stmt = ifx_db.prepare(conn, "SELECT col1, col2, col3 FROM tab_num_literals WHERE col2 > '33'")
       ifx_db.execute(stmt)
       data = ifx_db.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         data = ifx_db.fetch_both(stmt)
	 
       sql = "DELETE FROM tab_num_literals WHERE col1 > '10.0'"
       res = ifx_db.exec_immediate(conn, sql)
       print "Number of deleted rows:", ifx_db.num_rows(res)

       stmt = ifx_db.prepare(conn, "SELECT col1, col2, col3 FROM tab_num_literals WHERE col3 < '56'")
       ifx_db.execute(stmt)
       data = ifx_db.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         data = ifx_db.fetch_both(stmt)

       ifx_db.rollback(conn)
       ifx_db.close(conn)

#__END__
#__LUW_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
#__ZOS_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
#__SYSTEMI_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
#__IDS_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
