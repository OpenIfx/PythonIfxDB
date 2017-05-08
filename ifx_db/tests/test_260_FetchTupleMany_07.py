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

  def test_260_FetchTupleMany_07(self):
    obj = IfxDbTestFunctions() 
    obj.assert_expect(self.run_test_260)

  def run_test_260(self):
      conn = ifx_db.connect(config.database, config.user, config.password)
      
      if conn:
        stmt = ifx_db.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
        
        row = ifx_db.fetch_tuple(stmt)
        while ( row ):
            for i in row:
                print i
            row = ifx_db.fetch_tuple(stmt)
        
        ifx_db.close(conn)
        
      else:
        print "Connection failed."

#__END__
#__LUW_EXPECTED__
#0
#cat
#Pook            
#3.20
#__ZOS_EXPECTED__
#0
#cat
#Pook            
#3.20
#__SYSTEMI_EXPECTED__
#0
#cat
#Pook            
#3.20
#__IDS_EXPECTED__
#0
#cat
#Pook            
#3.20
