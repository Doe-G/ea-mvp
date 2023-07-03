from lib import Message, DataBase, Gatherer, FrontEnd
# Aquí va la logica de fucnionamiento del condigo y la ejecucion normal del mismo

can0 = Gatherer("can0", 1000000)
can1 = Gatherer("can1", 500000)
db0 = DataBase("can0.csv")
db1 = DataBase("can1.csv")
front = FrontEnd()
