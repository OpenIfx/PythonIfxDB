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

  def test_047_FetchTupleMany_06(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_047)

  def run_test_047(self):
    conn = ifx_db.connect(config.database, config.user, config.password)

    server = ifx_db.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'IDS'):
      result = ifx_db.exec_immediate(conn, "SELECT empno, photo_format, photo_format from emp_photo")
    else:
      result = ifx_db.exec_immediate(conn, "SELECT empno, photo_format, length(PICTURE) from emp_photo")
    row = ifx_db.fetch_tuple(result)
    while ( row ):
      if (row[1] == 'gif'):
        print "<img src='test_047.php?EMPNO=%s&FORMAT=%s'><br>\n" % (row[0], row[1])
      if (row[1] != 'xwd'):
        print "<a href='test_047.php?EMPNO=%s&FORMAT=%s' target=_blank>%s - %s - %s bytes</a>\n<br>" % (row[0], row[1], row[0], row[1], row[2])
      row = ifx_db.fetch_tuple(result)
#__END__
#__LUW_EXPECTED__
#<a href='test_047.php?EMPNO=000130&FORMAT=jpg' target=_blank>000130 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000130&FORMAT=png' target=_blank>000130 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=jpg' target=_blank>000140 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=png' target=_blank>000140 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=jpg' target=_blank>000150 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=png' target=_blank>000150 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=jpg' target=_blank>000190 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=png' target=_blank>000190 - png - 10291 bytes</a>
#<br>
#__ZOS_EXPECTED__
#<a href='test_047.php?EMPNO=000130&FORMAT=jpg' target=_blank>000130 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000130&FORMAT=png' target=_blank>000130 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=jpg' target=_blank>000140 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=png' target=_blank>000140 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=jpg' target=_blank>000150 - jpg -153988 bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=png' target=_blank>000150 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=jpg' target=_blank>000190 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=png' target=_blank>000190 - png - 10291 bytes</a>
#<br>
#__SYSTEMI_EXPECTED__
#<a href='test_047.php?EMPNO=000130&FORMAT=jpg' target=_blank>000130 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000130&FORMAT=png' target=_blank>000130 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=jpg' target=_blank>000140 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=png' target=_blank>000140 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=jpg' target=_blank>000150 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=png' target=_blank>000150 - png - 10291 bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=jpg' target=_blank>000190 - jpg - 15398 bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=png' target=_blank>000190 - png - 10291 bytes</a>
#<br>
#__IDS_EXPECTED__
#<a href='test_047.php?EMPNO=000130&FORMAT=jpg' target=_blank>000130 - jpg - jpg bytes</a>
#<br><a href='test_047.php?EMPNO=000130&FORMAT=png' target=_blank>000130 - png - png bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=jpg' target=_blank>000140 - jpg - jpg bytes</a>
#<br><a href='test_047.php?EMPNO=000140&FORMAT=png' target=_blank>000140 - png - png bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=jpg' target=_blank>000150 - jpg - jpg bytes</a>
#<br><a href='test_047.php?EMPNO=000150&FORMAT=png' target=_blank>000150 - png - png bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=jpg' target=_blank>000190 - jpg - jpg bytes</a>
#<br><a href='test_047.php?EMPNO=000190&FORMAT=png' target=_blank>000190 - png - png bytes</a>
#<br>
