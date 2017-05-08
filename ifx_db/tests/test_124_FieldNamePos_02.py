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

  def test_124_FieldNamePos_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_124)

  def run_test_124(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
  
    if conn:
       result = ifx_db.exec_immediate(conn, "select * from staff, employee, org where employee.lastname in ('HAAS','THOMPSON', 'KWAN', 'GEYER', 'STERN', 'PULASKI', 'HENDERSON', 'SPENSER', 'LUCCHESSI', 'OCONNELL', 'QUINTANA', 'NICHOLLS', 'ADAMSON', 'PIANKA', 'YOSHIMURA', 'SCOUTTEN', 'WALKER', 'BROWN', 'JONES', 'LUTZ', 'JEFFERSON', 'MARINO', 'SMITH', 'JOHNSON', 'PEREZ', 'SCHNEIDER', 'PARKER', 'SMITH', 'SETRIGHT', 'MEHTA', 'LEE', 'GOUNOT') order by org.location,employee.lastname,staff.id")
       cols = ifx_db.num_fields(result)
       j = 0
       row = ifx_db.fetch_both(result)
       while ( row ):
          for i in range(0, cols):
             field = ifx_db.field_name(result, i)
             value = row[ifx_db.field_name(result, i)]
             if (value == None): 
                value = ''
             print "%s:%s" % (field, value)
          print "---------"
          j += 1
          if (j == 10):
            break
       
          row = ifx_db.fetch_both(result)
       
       ifx_db.close(conn)
       print "done"
    else:
       print ifx_db.conn_errormsg()
#__END__
#__LUW_EXPECTED__
#ID:10
#NAME:Sanders
#DEPT:20
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:20
#NAME:Pernal
#DEPT:20
#JOB:DESIGNER
#YEARS:8
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:30
#NAME:Marenghi
#DEPT:38
#JOB:DESIGNER
#YEARS:5
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:40
#NAME:OBrien
#DEPT:38
#JOB:DESIGNER
#YEARS:6
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:50
#NAME:Hanes
#DEPT:15
#JOB:DESIGNER
#YEARS:10
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:60
#NAME:Quigley
#DEPT:38
#JOB:DESIGNER
#YEARS:
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:70
#NAME:Rothman
#DEPT:15
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:80
#NAME:James
#DEPT:20
#JOB:DESIGNER
#YEARS:
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:90
#NAME:Koonitz
#DEPT:42
#JOB:DESIGNER
#YEARS:6
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:100
#NAME:Plotz
#DEPT:42
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#done
#__ZOS_EXPECTED__
#ID:10
#NAME:Sanders
#DEPT:20
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:20
#NAME:Pernal
#DEPT:20
#JOB:DESIGNER
#YEARS:8
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:30
#NAME:Marenghi
#DEPT:38
#JOB:DESIGNER
#YEARS:5
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:40
#NAME:OBrien
#DEPT:38
#JOB:DESIGNER
#YEARS:6
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:50
#NAME:Hanes
#DEPT:15
#JOB:DESIGNER
#YEARS:10
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:60
#NAME:Quigley
#DEPT:38
#JOB:DESIGNER
#YEARS:
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:70
#NAME:Rothman
#DEPT:15
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:80
#NAME:James
#DEPT:20
#JOB:DESIGNER
#YEARS:
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:90
#NAME:Koonitz
#DEPT:42
#JOB:DESIGNER
#YEARS:6
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:100
#NAME:Plotz
#DEPT:42
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#done
#__SYSTEMI_EXPECTED__
#ID:10
#NAME:Sanders
#DEPT:20
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:20
#NAME:Pernal
#DEPT:20
#JOB:DESIGNER
#YEARS:8
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:30
#NAME:Marenghi
#DEPT:38
#JOB:DESIGNER
#YEARS:5
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:40
#NAME:OBrien
#DEPT:38
#JOB:DESIGNER
#YEARS:6
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:50
#NAME:Hanes
#DEPT:15
#JOB:DESIGNER
#YEARS:10
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:60
#NAME:Quigley
#DEPT:38
#JOB:DESIGNER
#YEARS:
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:70
#NAME:Rothman
#DEPT:15
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:80
#NAME:James
#DEPT:20
#JOB:DESIGNER
#YEARS:
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:90
#NAME:Koonitz
#DEPT:42
#JOB:DESIGNER
#YEARS:6
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#ID:100
#NAME:Plotz
#DEPT:42
#JOB:DESIGNER
#YEARS:7
#SALARY:25280.00
#COMM:2022.00
#EMPNO:000150
#FIRSTNME:BRUCE
#MIDINIT: 
#LASTNAME:ADAMSON
#WORKDEPT:D11
#PHONENO:4510
#HIREDATE:1972-02-12
#JOB:DESIGNER
#EDLEVEL:16
#SEX:M
#BIRTHDATE:1947-05-17
#SALARY:25280.00
#BONUS:500.00
#COMM:2022.00
#DEPTNUMB:38
#DEPTNAME:South Atlantic
#MANAGER:30
#DIVISION:Eastern
#LOCATION:Atlanta
#---------
#done
#__IDS_EXPECTED__
#id:10
#name:Sanders
#dept:20
#job:DESIGNER
#years:7
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:20
#name:Pernal
#dept:20
#job:DESIGNER
#years:8
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:30
#name:Marenghi
#dept:38
#job:DESIGNER
#years:5
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:40
#name:OBrien
#dept:38
#job:DESIGNER
#years:6
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:50
#name:Hanes
#dept:15
#job:DESIGNER
#years:10
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:60
#name:Quigley
#dept:38
#job:DESIGNER
#years:
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:70
#name:Rothman
#dept:15
#job:DESIGNER
#years:7
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:80
#name:James
#dept:20
#job:DESIGNER
#years:
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:90
#name:Koonitz
#dept:42
#job:DESIGNER
#years:6
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#id:100
#name:Plotz
#dept:42
#job:DESIGNER
#years:7
#salary:25280.00
#comm:2022.00
#empno:000150
#firstnme:BRUCE
#midinit: 
#lastname:ADAMSON
#workdept:D11
#phoneno:4510
#hiredate:1972-02-12
#job:DESIGNER
#edlevel:16
#sex:M
#birthdate:1947-05-17
#salary:25280.00
#bonus:500.00
#comm:2022.00
#deptnumb:38
#deptname:South Atlantic
#manager:30
#division:Eastern
#location:Atlanta
#---------
#done



