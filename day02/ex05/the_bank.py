class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if isinstance(new_account, Account):
            if new_account.name not in [account.name for account in self.accounts]:
                if not self.is_corrupted(new_account):
                    self.accounts.append(new_account)
                    return True
        return False

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if origin in [account.name for account in self.accounts] and dest in [account.name for account in self.accounts]:
            origin_account = [account for account in self.accounts if account.name == origin][0]
            dest_account = [account for account in self.accounts if account.name == dest][0]
            # Vérifier la validité de la transaction
            if amount < 0 or amount > origin_account.value:
                return False
            # Effectuer le transfert de fonds
            origin_account.value -= amount
            dest_account.value += amount
            return True
        return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if isinstance(name, str) and name in [account.name for account in self.accounts]:
            account_to_fix = [account for account in self.accounts if account.name == name][0]
            if self.is_corrupted(account_to_fix):
                account_to_fix.__dict__ = {key: value for key, value in account_to_fix.__dict__.items() if key in ['name', 'id', 'value']}
                return True
        return False

    def is_corrupted(self, account):
        """ Check if an account is corrupted
        @account: Account object
        @return True if account is corrupted, False otherwise
        """
        if len(account.__dict__) % 2 != 0:
            return True
        if any(key.startswith('b') for key in account.__dict__.keys()):
            return True
        if not any(key.startswith('zip') or key.startswith('addr') for key in account.__dict__.keys()):
            return True
        if not all(key in account.__dict__ for key in ['name', 'id', 'value']):
            return True
        if not isinstance(account.name, str):
            return True
        if not isinstance(account.id, int):
            return True
        if not isinstance(account.value, (int, float)):
            return True
        return False
