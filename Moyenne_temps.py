#Initialisation de la variable "Total"
Total = 0 

#Initialisation des variables pour la température minimale et maximale
temps = float('inf')


for i in range(31): #Répétez 31 fois
    
    temps = float(input("Veuillez entrer un temps ")) #demande de rentrer la température à l'utilisateur
                        
    Total = Total + temperature #Ajoute la temperature à la variable totale

    #Mets à hour la température minimale et maximale
    if temperature < temperature_min:
        temperature_min = temperature
    if temperature > temperature_max:
        temperature_max = temperature

    Moyenne = Total/31 #Calcule la moyenne

    etendue = temperature_max - temperature_min #Calcule l'étendue

print(f"La moyenne des températures est de {Moyenne}") #Affiche la moyenne 
print(f"La température minimale est de {temperature_min}") #Affiche la température minimale
print(f"La température maximale est de {temperature_max} ") #Affiche la température maximale
print(f"L'étendue est de {etendue}") #Affiche l'étendue