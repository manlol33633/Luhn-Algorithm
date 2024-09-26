class Luhn:
    def pass_luhn(self, acct):
        try:
            test = int(acct)
            totalCheck = int(acct[-1:])
        except:
            return False

        for i in range(len(acct) - 1):
            cNum = int(acct[-i - 2:-i - 1])
            if (i % 2 == 0):
                str2Num = str(cNum * 2)

                if (cNum * 2 > 9):
                    totalCheck += int(str2Num[:1]) + int(str2Num[1:])
                else:
                    totalCheck += cNum * 2
            else:
                    totalCheck += cNum
        if (totalCheck % 10 == 0):
            return True
        else:
            return False

    def is_amex(self, acct):
        if Luhn().pass_luhn(acct):
            if len(acct) == 15 and (int(acct[:2]) == 34 or int(acct[:2]) == 37):
                return True
        return False

    def is_visa(self, acct):
        if Luhn().pass_luhn(acct):
            if len(acct) == 13 or len(acct) == 16 and int(acct[:1]) == 4:
                return True
        return False

    def is_mastercard(self, acct):
        if Luhn().pass_luhn(acct):
            if len(acct) == 16 and int(acct[:2]) in range(51, 55):
                return True
        return False

    def is_discover(self, acct):
        if Luhn().pass_luhn(acct):
            if len(acct) == 16 and int(acct[:4]) == 6011:
                return True
        return False

    def is_valid_cc(self, acct):
        if Luhn().is_amex(acct):
            return True
        elif Luhn().is_visa(acct):
            return True
        elif Luhn().is_mastercard(acct):
            return True
        elif Luhn().is_discover(acct):
            return True
        else:
            return False