import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('nombre: ', name,'-- uso_cpu: ', cpu_usage)
        app_name_dict.update({name:cpu_usage})
        
#--------nombres de las apps------------------
keymax=max(app_name_dict,key=app_name_dict.get)
print(keymax)
keymin=min(app_name_dict,key=app_name_dict.get)
print(keymin)
name_list=[keymax,keymin]
print(name_list)


#--------------------USO DEL CPU-------
app=app_name_dict.values()
max_app=max(app)
print("máximo", max_app)
min_app=min(app)
print("mínimo",min_app)
max_min_list=[max_app,min_app]
print(max_min_list)


#----------------------trazado------------
plt.figure(figsize=(15,8))
plt.xlabel("Consumo mínimo-máximo de la CPU")
plt.ylabel("Uso")
plt.bar(name_list,max_min_list,width=0.6,color=("blue","red") )
plt.show()

        