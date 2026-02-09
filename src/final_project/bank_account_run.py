from final_project.bank_account import Account, Transaction

acc = Account("Иван", 100)
print(acc)
print(acc.__repr__())
acc.add_transaction(Transaction(50, "Пополнение"))
# acc.balance теперь должен быть 150
# len(acc) должен быть 1
# acc.add_transaction(Transaction(-200, "Покупка")) -> вызовет TransactionError
