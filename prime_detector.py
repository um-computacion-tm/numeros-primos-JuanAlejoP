import unittest

#IS PRIME
def is_prime(value):
    index = 0
    divisors = [2,3,4,5,6,7,8,9]
    while index < len(divisors):
        if value % divisors[index] == 0 and value != divisors[index] or value == 1:
            return False
        index += 1
    return True

#TESTS
class TestIsPrime(unittest.TestCase):
    def test_num01(self):
        result = is_prime(1)
        self.assertFalse(result)

    def test_num02(self):
        result = is_prime(2)
        self.assertTrue(result)
    
    def test_num03(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_num04(self):
        result = is_prime(4)
        self.assertFalse(result)

    def test_num05(self):
        result = is_prime(5)
        self.assertTrue(result)
    
    def test_num06(self):
        result = is_prime(6)
        self.assertFalse(result)
    
    def test_num07(self):
        result = is_prime(7)
        self.assertTrue(result)
    
    def test_num08(self):
        result = is_prime(8)
        self.assertFalse(result)
    
    def test_num09(self):
        result = is_prime(9)
        self.assertFalse(result)
    
    def test_num10(self):
        result = is_prime(10)
        self.assertFalse(result)

    def test_num11(self):
        result = is_prime(11)
        self.assertTrue(result)

    def test_num12(self):
        result = is_prime(12)
        self.assertFalse(result)
    
    def test_num13(self):
        result = is_prime(13)
        self.assertTrue(result)
    
    def test_num14(self):
        result = is_prime(14)
        self.assertFalse(result)

    def test_num15(self):
        result = is_prime(15)
        self.assertFalse(result)
    
    def test_num16(self):
        result = is_prime(16)
        self.assertFalse(result)
    
    def test_num17(self):
        result = is_prime(17)
        self.assertTrue(result)
    
    def test_num18(self):
        result = is_prime(18)
        self.assertFalse(result)
    
    def test_num19(self):
        result = is_prime(19)
        self.assertTrue(result)
    
    def test_num20(self):
        result = is_prime(20)
        self.assertFalse(result)

    def test_num21(self):
        result = is_prime(21)
        self.assertFalse(result)

    def test_num22(self):
        result = is_prime(22)
        self.assertFalse(result)
    
    def test_num23(self):
        result = is_prime(23)
        self.assertTrue(result)
    
    def test_num24(self):
        result = is_prime(24)
        self.assertFalse(result)

    def test_num25(self):
        result = is_prime(25)
        self.assertFalse(result)
    
    def test_num26(self):
        result = is_prime(26)
        self.assertFalse(result)
    
    def test_num27(self):
        result = is_prime(27)
        self.assertFalse(result)
    
    def test_num28(self):
        result = is_prime(28)
        self.assertFalse(result)
    
    def test_num29(self):
        result = is_prime(29)
        self.assertTrue(result)
    
    def test_num30(self):
        result = is_prime(30)
        self.assertFalse(result)
    
    def test_num31(self):
        result = is_prime(31)
        self.assertTrue(result)

    def test_num32(self):
        result = is_prime(32)
        self.assertFalse(result)
    
    def test_num33(self):
        result = is_prime(33)
        self.assertFalse(result)
    
    def test_num34(self):
        result = is_prime(34)
        self.assertFalse(result)

    def test_num35(self):
        result = is_prime(35)
        self.assertFalse(result)
    
    def test_num36(self):
        result = is_prime(36)
        self.assertFalse(result)
    
    def test_num37(self):
        result = is_prime(37)
        self.assertTrue(result)
    
    def test_num38(self):
        result = is_prime(38)
        self.assertFalse(result)
    
    def test_num39(self):
        result = is_prime(39)
        self.assertFalse(result)
    
    def test_num40(self):
        result = is_prime(40)
        self.assertFalse(result)
    
    def test_num41(self):
        result = is_prime(41)
        self.assertTrue(result)

    def test_num42(self):
        result = is_prime(42)
        self.assertFalse(result)
    
    def test_num43(self):
        result = is_prime(43)
        self.assertTrue(result)
    
    def test_num44(self):
        result = is_prime(44)
        self.assertFalse(result)

    def test_num45(self):
        result = is_prime(45)
        self.assertFalse(result)
    
    def test_num46(self):
        result = is_prime(46)
        self.assertFalse(result)
    
    def test_num47(self):
        result = is_prime(47)
        self.assertTrue(result)
    
    def test_num48(self):
        result = is_prime(48)
        self.assertFalse(result)
    
    def test_num49(self):
        result = is_prime(49)
        self.assertFalse(result)
    
    def test_num50(self):
        result = is_prime(50)
        self.assertFalse(result)
    
    def test_num51(self):
        result = is_prime(51)
        self.assertFalse(result)

    def test_num52(self):
        result = is_prime(52)
        self.assertFalse(result)
    
    def test_num53(self):
        result = is_prime(53)
        self.assertTrue(result)
    
    def test_num54(self):
        result = is_prime(54)
        self.assertFalse(result)

    def test_num55(self):
        result = is_prime(55)
        self.assertFalse(result)
    
    def test_num56(self):
        result = is_prime(56)
        self.assertFalse(result)
    
    def test_num57(self):
        result = is_prime(57)
        self.assertFalse(result)
    
    def test_num58(self):
        result = is_prime(58)
        self.assertFalse(result)
    
    def test_num59(self):
        result = is_prime(59)
        self.assertTrue(result)
    
    def test_num60(self):
        result = is_prime(60)
        self.assertFalse(result)

    def test_num61(self):
        result = is_prime(61)
        self.assertTrue(result)

    def test_num62(self):
        result = is_prime(62)
        self.assertFalse(result)
    
    def test_num63(self):
        result = is_prime(63)
        self.assertFalse(result)
    
    def test_num64(self):
        result = is_prime(64)
        self.assertFalse(result)

    def test_num65(self):
        result = is_prime(65)
        self.assertFalse(result)
    
    def test_num66(self):
        result = is_prime(66)
        self.assertFalse(result)
    
    def test_num67(self):
        result = is_prime(67)
        self.assertTrue(result)
    
    def test_num68(self):
        result = is_prime(68)
        self.assertFalse(result)
    
    def test_num69(self):
        result = is_prime(69)
        self.assertFalse(result)
    
    def test_num70(self):
        result = is_prime(70)
        self.assertFalse(result)

    def test_num71(self):
        result = is_prime(71)
        self.assertTrue(result)

    def test_num72(self):
        result = is_prime(72)
        self.assertFalse(result)
    
    def test_num73(self):
        result = is_prime(73)
        self.assertTrue(result)
    
    def test_num74(self):
        result = is_prime(74)
        self.assertFalse(result)

    def test_num75(self):
        result = is_prime(75)
        self.assertFalse(result)
    
    def test_num76(self):
        result = is_prime(76)
        self.assertFalse(result)
    
    def test_num77(self):
        result = is_prime(77)
        self.assertFalse(result)
    
    def test_num78(self):
        result = is_prime(78)
        self.assertFalse(result)
    
    def test_num79(self):
        result = is_prime(79)
        self.assertTrue(result)
    
    def test_num80(self):
        result = is_prime(80)
        self.assertFalse(result)
    
    def test_num81(self):
        result = is_prime(81)
        self.assertFalse(result)

    def test_num82(self):
        result = is_prime(82)
        self.assertFalse(result)
    
    def test_num83(self):
        result = is_prime(83)
        self.assertTrue(result)
    
    def test_num84(self):
        result = is_prime(84)
        self.assertFalse(result)

    def test_num85(self):
        result = is_prime(85)
        self.assertFalse(result)
    
    def test_num86(self):
        result = is_prime(86)
        self.assertFalse(result)
    
    def test_num87(self):
        result = is_prime(87)
        self.assertFalse(result)
    
    def test_num88(self):
        result = is_prime(88)
        self.assertFalse(result)
    
    def test_num89(self):
        result = is_prime(89)
        self.assertTrue(result)
    
    def test_num90(self):
        result = is_prime(90)
        self.assertFalse(result)
    
    def test_num91(self):
        result = is_prime(91)
        self.assertFalse(result)

    def test_num92(self):
        result = is_prime(92)
        self.assertFalse(result)
    
    def test_num93(self):
        result = is_prime(93)
        self.assertFalse(result)
    
    def test_num94(self):
        result = is_prime(94)
        self.assertFalse(result)

    def test_num95(self):
        result = is_prime(95)
        self.assertFalse(result)
    
    def test_num96(self):
        result = is_prime(96)
        self.assertFalse(result)
    
    def test_num97(self):
        result = is_prime(97)
        self.assertTrue(result)
    
    def test_num98(self):
        result = is_prime(98)
        self.assertFalse(result)
    
    def test_num99(self):
        result = is_prime(99)
        self.assertFalse(result)
    
    def test_num100(self):
        result = is_prime(100)
        self.assertFalse(result)
        
unittest.main()