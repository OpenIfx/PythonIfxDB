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

  def test_231_FieldTypeName(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_231)

  def run_test_231(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    result = ifx_db.exec_immediate(conn, "select * from sales")
    result2 = ifx_db.exec_immediate(conn, "select * from staff")
    result3 = ifx_db.exec_immediate(conn, "select * from emp_photo")
    
    for i in range(0, ifx_db.num_fields(result) + 1):
      print str(i) + ":" + str(ifx_db.field_type(result,ifx_db.field_name(result,i)))
    
    print "\n-----"
    
    for i in range(0, ifx_db.num_fields(result2)):
      print str(i) + ":" + ifx_db.field_type(result2,ifx_db.field_name(result2,i))
    
    print "\n-----"
    
    for i in range(0, 3):
      print str(i) + ":" + ifx_db.field_type(result3,ifx_db.field_name(result3,i))
    
    print "\n-----"
    
    print "region:%s" % ifx_db.field_type(result,'region')
    print "5:%s" % ifx_db.field_type(result2,5)

#__END__
#__LUW_EXPECTED__
#0:date
#1:string
#2:string
#3:int
#4:False
#
#-----
#0:int
#1:string
#2:int
#3:string
#4:int
#5:decimal
#6:decimal
#
#-----
#0:string
#1:string
#2:blob
#
#-----
#region:False
#5:decimal
#__ZOS_EXPECTED__
#0:date
#1:string
#2:string
#3:int
#4:False
#
#-----
#0:int
#1:string
#2:int
#3:string
#4:int
#5:decimal
#6:decimal
#
#-----
#0:string
#1:string
#2:blob
#
#-----
#region:False
#5:decimal
#__SYSTEMI_EXPECTED__
#0:date
#1:string
#2:string
#3:int
#4:False
#
#-----
#0:int
#1:string
#2:int
#3:string
#4:int
#5:decimal
#6:decimal
#
#-----
#0:string
#1:string
#2:blob
#
#-----
#region:False
#5:decimal
#__IDS_EXPECTED__
#0:date
#1:string
#2:string
#3:int
#4:False
#
#-----
#0:int
#1:string
#2:int
#3:string
#4:int
#5:decimal
#6:decimal
#
#-----
#0:string
#1:string
#2:string
#
#-----
#region:string
#5:decimal