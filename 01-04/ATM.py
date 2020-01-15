import random

class Account:
    def __init__(self, id, balance=0, ):
        self.id = id
        self.balance = balance
    
    def getId(self):
        return self.id
    
    def getBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

#membuat akun ATM
def main():
    accounts = []
    for i in range (1000, 9999):
        account = Account(i, 0)
        accounts.append(account)


    while True:
        id = int(input("\nMasukkan pin: "))

        while id<1000 or id > 9999:
            id = int(input("\nPin salah, ketik ulang: "))
        
        while True:
            print("1 - Saldo \t 2 - Tarik tunai \t 3 - Deposit \t 4 - Keluar ")

            selection = int(input("\nMasukkan pilihan: "))

            for acc in accounts:
                if acc.getId() == id:
                    accountObj = acc
                    break
                
            #opsi 1 saldo
            if selection == 1:
                print(accountObj.getBalance())

            #opsi 2 tarik tunai
            elif selection == 2:
                amt = float(input("\nMasukkan jumlah penarikan: "))
                ver_withdraw = input("apakah jumlah ini sudah benar? y atau n " + str(amt) + " ")
                

                if ver_withdraw == "y":
                    print("Verivikasi penarikan")
                else:
                    break
                
                if amt < accountObj.getId():
                    accountObj.withdraw(amt)
                    print("\nSaldo: " + str(accountObj.getBalance()) + " n")
                else:
                    print("\nSaldo tidak mencukupi");
 
            #opsi 3 deposit
            elif selection == 3:
                amt = float(input("\nMasukkan jumlah deposit: "))
                ver_deposit = input("Apakah jumlah ini sudah benar? y atau n ? " + str(amt) + " ")

                if ver_deposit == "y":
                    accountObj.deposit(amt);
                    print("\nSaldo: " + str(accountObj.getBalance()) + " n")
                else:
                    break

            #opsi 4 selesai
            elif selection == 4:
                print("\nTransaksi selesai: ")
                print("\nNomer transaksi: ", random.randint(10000, 1000000))
                print("\nTerima kasih sudah menggunakan jasa kami")
                exit()
            #opsi lain invalid
            else:
                print("Pilihan salah.")
main()
