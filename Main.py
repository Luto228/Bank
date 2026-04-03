import random

class Account():
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.__password = password
        self.__balance = 0
        self.id = random.randint(1, 10000000)
    def get_balance(self, PasswordSaid):
        if PasswordSaid == self.__password:
            print(self.__balance)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print('баланс успешно пополнен!')
        else:
            print('вы должны зачислить хоть какие то деньги!')
    def withdraw(self, amount, PasswordSaid):
        if PasswordSaid == self.__password and amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f'Деньги собраны! На кошельке осталось {self.__balance}')
        elif PasswordSaid != self.__password:
            print('Не верный пароль! Попробуйте снова!')
        else:
            print('недостаточно средств')

class Bank():
    def __init__(self):
        self.account = []
    def createAccount(self, nickname, password):
        newAcc = Account(nickname, password)
        self.account.append(newAcc)
        print(f'Аккаунт создан для {nickname}! Его ID - {newAcc.id}')
        return newAcc
    def findAcc(self, searchID):
        for x in self.account:
            if x.id == searchID:
                print('Аккаунт найден!')
                print(x.nickname)
                return x
        print(f'Аккаунт с ID {searchID} не найден!')

tinkoff = Bank()
tinkoff.createAccount('Alex', 44444)
a = tinkoff.createAccount('Oleg', 9999)
tinkoff.findAcc(a.id)