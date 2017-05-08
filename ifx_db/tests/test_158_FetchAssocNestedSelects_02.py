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

  def test_158_FetchAssocNestedSelects_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_158)

  def run_test_158(self):
    conn = ifx_db.connect(config.database, config.user, config.password)

    server = ifx_db.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'IDS'):
      op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
      ifx_db.set_option(conn, op, 1)

    result = ifx_db.exec_immediate(conn, "SELECT * FROM staff WHERE id < 50")
    
    output = ''
    row = ifx_db.fetch_assoc(result)
    while ( row ):
      output += str(row['ID']) + ', ' + row['NAME'] + ', ' + str(row['DEPT']) + ', ' + row['JOB'] + ', ' + str(row['YEARS']) + ', ' + str(row['SALARY']) + ', ' + str(row['COMM'])
      row = ifx_db.fetch_assoc(result)
      
    result2 = ifx_db.exec_immediate(conn,"SELECT * FROM department WHERE substr(deptno,1,1) in ('A','B','C','D','E')")
    row2 = ifx_db.fetch_assoc(result2)
    while ( row2 ):
        if (row2['MGRNO'] == None): 
            row2['MGRNO'] = ''
        if (row2['LOCATION'] == None): 
            row2['LOCATION'] = ''
        output += str(row2['DEPTNO']) + ', ' + row2['DEPTNAME'] + ', ' + str(row2['MGRNO']) + ', ' + row2['ADMRDEPT'] + ', ' + row2['LOCATION']
        row2 = ifx_db.fetch_assoc(result2)
    
    result3 = ifx_db.exec_immediate(conn,"SELECT * FROM employee WHERE lastname IN ('HAAS','THOMPSON', 'KWAN', 'GEYER', 'STERN', 'PULASKI', 'HENDERSON', 'SPENSER', 'LUCCHESSI', 'OCONNELL', 'QUINTANA', 'NICHOLLS', 'ADAMSON', 'PIANKA', 'YOSHIMURA', 'SCOUTTEN', 'WALKER', 'BROWN', 'JONES', 'LUTZ', 'JEFFERSON', 'MARINO', 'SMITH', 'JOHNSON', 'PEREZ', 'SCHNEIDER', 'PARKER', 'SMITH', 'SETRIGHT', 'MEHTA', 'LEE', 'GOUNOT')")
    row3 = ifx_db.fetch_tuple(result3)
    while ( row3 ):
        output += row3[0] + ', ' + row3[3] + ', ' + row3[5]
        row3=ifx_db.fetch_tuple(result3)
    print output

#__END__
#__LUW_EXPECTED__
#10, Sanders, 20, Mgr  , 7, 18357.50, None20, Pernal, 20, Sales, 8, 18171.25, 612.4530, Marenghi, 38, Mgr  , 5, 17506.75, None40, OBrien, 38, Sales, 6, 18006.00, 846.55A00, SPIFFY COMPUTER SERVICE DIV., 000010, A00, B01, PLANNING, 000020, A00, C01, INFORMATION CENTER, 000030, A00, D01, DEVELOPMENT CENTER, , A00, D11, MANUFACTURING SYSTEMS, 000060, D01, D21, ADMINISTRATION SYSTEMS, 000070, D01, E01, SUPPORT SERVICES, 000050, A00, E11, OPERATIONS, 000090, E01, E21, SOFTWARE SUPPORT, 000100, E01, 000010, HAAS, 3978000020, THOMPSON, 3476000030, KWAN, 4738000050, GEYER, 6789000060, STERN, 6423000070, PULASKI, 7831000090, HENDERSON, 5498000100, SPENSER, 0972000110, LUCCHESSI, 3490000120, OCONNELL, 2167000130, QUINTANA, 4578000140, NICHOLLS, 1793000150, ADAMSON, 4510000160, PIANKA, 3782000170, YOSHIMURA, 2890000180, SCOUTTEN, 1682000190, WALKER, 2986000200, BROWN, 4501000210, JONES, 0942000220, LUTZ, 0672000230, JEFFERSON, 2094000240, MARINO, 3780000250, SMITH, 0961000260, JOHNSON, 8953000270, PEREZ, 9001000280, SCHNEIDER, 8997000290, PARKER, 4502000300, SMITH, 2095000310, SETRIGHT, 3332000320, MEHTA, 9990000330, LEE, 2103000340, GOUNOT, 5698
#__ZOS_EXPECTED__
#10, Sanders, 20, Mgr  , 7, 18357.50, None20, Pernal, 20, Sales, 8, 18171.25, 612.4530, Marenghi, 38, Mgr  , 5, 17506.75, None40, OBrien, 38, Sales, 6, 18006.00, 846.55A00, SPIFFY COMPUTER SERVICE DIV., 000010, A00, B01, PLANNING, 000020, A00, C01, INFORMATION CENTER, 000030, A00, D01, DEVELOPMENT CENTER, , A00, D11, MANUFACTURING SYSTEMS, 000060, D01, D21, ADMINISTRATION SYSTEMS, 000070, D01, E01, SUPPORT SERVICES, 000050, A00, E11, OPERATIONS, 000090, E01, E21, SOFTWARE SUPPORT, 000100, E01, 000010, HAAS, 3978000020, THOMPSON, 3476000030, KWAN, 4738000050, GEYER, 6789000060, STERN, 6423000070, PULASKI, 7831000090, HENDERSON, 5498000100, SPENSER, 0972000110, LUCCHESSI, 3490000120, OCONNELL, 2167000130, QUINTANA, 4578000140, NICHOLLS, 1793000150, ADAMSON, 4510000160, PIANKA, 3782000170, YOSHIMURA, 2890000180, SCOUTTEN, 1682000190, WALKER, 2986000200, BROWN, 4501000210, JONES, 0942000220, LUTZ, 0672000230, JEFFERSON, 2094000240, MARINO, 3780000250, SMITH, 0961000260, JOHNSON, 8953000270, PEREZ, 9001000280, SCHNEIDER, 8997000290, PARKER, 4502000300, SMITH, 2095000310, SETRIGHT, 3332000320, MEHTA, 9990000330, LEE, 2103000340, GOUNOT, 5698
#__SYSTEMI_EXPECTED__
#10, Sanders, 20, Mgr  , 7, 18357.50, None20, Pernal, 20, Sales, 8, 18171.25, 612.4530, Marenghi, 38, Mgr  , 5, 17506.75, None40, OBrien, 38, Sales, 6, 18006.00, 846.55A00, SPIFFY COMPUTER SERVICE DIV., 000010, A00, B01, PLANNING, 000020, A00, C01, INFORMATION CENTER, 000030, A00, D01, DEVELOPMENT CENTER, , A00, D11, MANUFACTURING SYSTEMS, 000060, D01, D21, ADMINISTRATION SYSTEMS, 000070, D01, E01, SUPPORT SERVICES, 000050, A00, E11, OPERATIONS, 000090, E01, E21, SOFTWARE SUPPORT, 000100, E01, 000010, HAAS, 3978000020, THOMPSON, 3476000030, KWAN, 4738000050, GEYER, 6789000060, STERN, 6423000070, PULASKI, 7831000090, HENDERSON, 5498000100, SPENSER, 0972000110, LUCCHESSI, 3490000120, OCONNELL, 2167000130, QUINTANA, 4578000140, NICHOLLS, 1793000150, ADAMSON, 4510000160, PIANKA, 3782000170, YOSHIMURA, 2890000180, SCOUTTEN, 1682000190, WALKER, 2986000200, BROWN, 4501000210, JONES, 0942000220, LUTZ, 0672000230, JEFFERSON, 2094000240, MARINO, 3780000250, SMITH, 0961000260, JOHNSON, 8953000270, PEREZ, 9001000280, SCHNEIDER, 8997000290, PARKER, 4502000300, SMITH, 2095000310, SETRIGHT, 3332000320, MEHTA, 9990000330, LEE, 2103000340, GOUNOT, 5698
#__IDS_EXPECTED__
#10, Sanders, 20, Mgr  , 7, 18357.50, None20, Pernal, 20, Sales, 8, 18171.25, 612.4530, Marenghi, 38, Mgr  , 5, 17506.75, None40, OBrien, 38, Sales, 6, 18006.00, 846.55A00, SPIFFY COMPUTER SERVICE DIV., 000010, A00, B01, PLANNING, 000020, A00, C01, INFORMATION CENTER, 000030, A00, D01, DEVELOPMENT CENTER, , A00, D11, MANUFACTURING SYSTEMS, 000060, D01, D21, ADMINISTRATION SYSTEMS, 000070, D01, E01, SUPPORT SERVICES, 000050, A00, E11, OPERATIONS, 000090, E01, E21, SOFTWARE SUPPORT, 000100, E01, 000010, HAAS, 3978000020, THOMPSON, 3476000030, KWAN, 4738000050, GEYER, 6789000060, STERN, 6423000070, PULASKI, 7831000090, HENDERSON, 5498000100, SPENSER, 0972000110, LUCCHESSI, 3490000120, OCONNELL, 2167000130, QUINTANA, 4578000140, NICHOLLS, 1793000150, ADAMSON, 4510000160, PIANKA, 3782000170, YOSHIMURA, 2890000180, SCOUTTEN, 1682000190, WALKER, 2986000200, BROWN, 4501000210, JONES, 0942000220, LUTZ, 0672000230, JEFFERSON, 2094000240, MARINO, 3780000250, SMITH, 0961000260, JOHNSON, 8953000270, PEREZ, 9001000280, SCHNEIDER, 8997000290, PARKER, 4502000300, SMITH, 2095000310, SETRIGHT, 3332000320, MEHTA, 9990000330, LEE, 2103000340, GOUNOT, 5698
