
from pracmln import MLN
from pracmln import Database
from pracmln import MLNQuery

mln = MLN(mlnfile='./data/smokers/mlns/smoking_trained.mln',grammar='PRACGrammar', logic='FirstOrderLogic')
mln.write()

db = Database.load(mln,'./data/smokers/dbs/smoking-test.db')[0]
db.write()

print("Running Query...")
result = MLNQuery(mln=mln, db=db).run()
print(result)
