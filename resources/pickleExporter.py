import pickle
print("PickleExporter 1.0")
whatToExport=path=None
def wtep():
    global whatToExport,path
    whatToExport=input("Export worlds? ")
    if whatToExport=="worlds":whatToExport={"1":"Big Goofy Birds","2":"Snowin' Goblins"};path="resources/worlds.pkl"
    else:print("Whoops! Try again.");wtep()
wtep()
with open(path,"wb") as f:pickle.dump(whatToExport,f)
print("Done.")