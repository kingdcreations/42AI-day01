
class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, src, dst, amount):
        """
        @src: int(id) or str(name) of the first account
        @dst: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        _dst = None
        _src = None
        for x in self.account:
            if (isinstance(src, str) and hasattr(x, "name") and x.name == src
               or isinstance(src, int) and hasattr(x, "id") and x.id == src):
                if (isinstance(x, Account) and hasattr(x, "value")
                   and len(dir(x)) % 2) and isgoodstart(x):
                    if (amount >= 0 and amount <= x.value):
                        _src = x
                        break
        for x in self.account:
            if (isinstance(dst, str) and hasattr(x, "name") and x.name == dst
               or isinstance(dst, int) and hasattr(x, "id") and x.id == dst):
                if (isinstance(x, Account) and hasattr(x, "value")
                   and len(dir(x)) % 2) and isgoodstart(x):
                    _dst = x
                    break
        if not _dst or not _src:
            return False
        _src.value -= amount
        _dst.transfer(amount)
        return True

    def fix_account(self, acc):
        """
        fix the corrupted account
        @acc: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """

        obj = None
        for x in self.account:
            if (isinstance(acc, str) and hasattr(x, "name") and x.name == acc
               or isinstance(acc, int) and hasattr(x, "id") and x.id == acc):
                obj = x

        if isinstance(obj, Account):
            if not hasattr(obj, "value"):
                setattr(obj, "value", 0)
        for x in dir(obj):
            if (x.startswith("b") or x.startswith("zip")
               or x.startswith("addr")):
                delattr(obj, x)
        return self.transfer(acc, acc, 0)


def isgoodstart(obj):
    for x in dir(obj):
        if x.startswith("b") or x.startswith("zip") or x.startswith("addr"):
            return False
    return True


thais = Account("thais", value=100)
miguel = Account("mig", bzip="lol", mdr="gdf")
robin = Account("robin", value=100, test="mdr", ipapt="ahah")
thais.transfer(2000)
print(thais.__dict__)
print(robin.__dict__)

bb = Bank()
bb.add(thais)
bb.add(robin)
bb.add(miguel)


print(bb.transfer(1, "mig", 1000))
print(thais.__dict__)
print(robin.__dict__)
print(miguel.__dict__)
print(bb.fix_account("mig"))
print(bb.transfer(1, "mig", 1000))
print(miguel.__dict__)
