#labo application de quizz


questionnaire = {
"En quelle année la compétition de la Coupe du monde a-t-elle commencé ? ": ["1930","1946","1928","1960"],
"À quelle fréquence la Coupe du monde a-t-elle lieu ?": ["Chaque quatre ans", "Chaque deux ans","Chaque cinq ans","Chaque huit ans"],
"Quel pays a remporté le plus de coupes du monde ?": ["Brésil","Allemagne","Argentine","Italie"],
"Quel est le pays hôte de la Coupe du monde 2022 ?": ['Qatar', 'Russie', 'USA', 'Japon'],"Combien de équipes participent à la Coupe du monde ?" : ["32","24","16","28"],
"Quel est le stade le plus grand utilisé pour la Coupe du monde ?" : ["Maracanã", "Wembley", "Estadio Azteca", "Camp Nou"],
"Quel est le nom de la mascotte officielle de la Coupe du monde de 2018 ?" : ["Zabivaka", "Goleo VI", "Pique", "Fuleco"],
"Quelle est la devise officielle de la Coupe du monde de 2018 ?" : ["A time to make friends", "Uniting nations", "For the love of the game", "All in one rhythm"],
"Qui a remporté la Coupe du monde de 2018 ?" : ["France", "Allemagne", "Espagne", "Argentine"]
}

def monQuizz(questionnaire):
    compteur_de_points = 0
    print("================================================")
    print("bienvenue a ce Quizz special coupe du monde ! : ")
    print("================================================")
    print("================================================")
    reponse1 = input("Etes vous pret a jouer  ? : y/n ")
    print("================================================")
    print("================================================")
    if(reponse1 == "y" or reponse1 == "Y"):
        print("Parfait bienvenue on commence avec les questions ")
    else:
        print("Daccord ! merci pour votre passage  ")
    print("================================================")
    print("=====================AU-REVOIR==================")
    for question ,reponse in questionnaire.items():
        responseUser = input(question)
        if responseUser.lower() == reponse[0].lower():
            print("Bravo ! vous avez eu la bonne reponse : ", reponse[0])
            compteur_de_points +=1
    print("================================================")
    print("Votre score est de : ", compteur_de_points)
    print("================================================")
    return compteur_de_points


#for("")
test1 = monQuizz(questionnaire)
