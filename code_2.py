import unittest

from fun2 import ScoureStudents

class StudentScoure(unittest.TestCase):
    def test_scoures(self):
        self.assertEqual(ScoureStudents(-1),"Invalid" )
        self.assertEqual(ScoureStudents(0),"Failed")
        self.assertEqual(ScoureStudents(49),"Failed")
        self.assertEqual(ScoureStudents(50),"Passed")
        self.assertEqual(ScoureStudents(64),"Passed")
        self.assertEqual(ScoureStudents(65),"Good")
        self.assertEqual(ScoureStudents(74),"Good")
        self.assertEqual(ScoureStudents(75),"V.Good")
        self.assertEqual(ScoureStudents(84),"V.Good")
        self.assertEqual(ScoureStudents(85),"Excellent")
        self.assertEqual(ScoureStudents(99),"Excellent")
        self.assertEqual(ScoureStudents(100),"Excellent")
        self.assertEqual(ScoureStudents(101),"Invalid")

        

if __name__ == '__main__':
    unittest.main()