import random


class Generator(object):
    @staticmethod
    def NPC() -> dict:
        stages: list = ["Child", "Teenager", "Young", "Adult", "Mature", "Elderly"]
        names: list = ["Isadora", "Emilia", "Adriana", "Ariane", "Teresa", "Rita", "Alana", "Bruna", "Aurora", "Amanda", "Helena", "Elisa", "Paola", "Natasha", "Julieta", "Julia", "Vivian", "Catarina", "Erica", "Larissa", "Aurea", "Livia", "Lorena", "Francisca", "Elza", "Maiara", "Marcela", "Alice", "Anna", "Samanta", "Jaqueline", "Gabriela", "Soraia", "Mirela", "Elisandra", "Andressa", "Carina", "Lavinia", "Luisa", "Daniela", "Victoria", "Angelica", "Laís", "Milena", "Laura", "Isabelle", "Olivia", "Emma", "Charlotte", "Clara", "Valeria", "Mia", "Astrid", "Liana", "Monica", "Alessandra", "Natalia", "Ingrid", "Cordelia", "Luna", "Mateus", "Tomas", "Carlos", "Neto", "Tadeu", "Angelo", "Douglas", "Eric", "Alex", "Alvaro", "Reinaldo", "Sergio", "Cassio", "Julio", "Nicolas", "Armando", "Cauã", "Victor", "Mauro", "Henrique", "Fabricio", "Giovane", "Joaquim", "Heitor", "Geraldo", "Alfredo", "Samuel", "Adriano", "Igor", "Osvaldo", "Hugo", "Valdomiro", "Conrado", "Sebastiao", "Jorge", "Roberto", "Arnoldo", "Breno", "Renato", "Aurelio", "Teodoro", "Reginaldo", "Jose", "Alceu", "Lorenzo", "Diogo", "Cicero", "Erico", "Guilherme", "Evandro", "Vicente", "Benedito", "Nelson", "Renan", "Davi", "Arthur", "Saulo", "Antenor", "Tulio", "Osmar"]
        appearances: list = ["One-eyed", "Burn marks on the skin", "Freckles on the face", "Crooked or broken nose", "Colored hair (purple, blue...)", "Stutter", "Delicate facial features", "Deep eye bags", "Hunched posture", "Wears old, faded, or tattered clothes", "Very short", "Big nose", "Scar on the face", "Overweight", "Short", "Small tattoos", "Angular and elegant face", "Proud posture", "Slim", "Tall", "Square and firm face", "Broad shoulders", "Round and friendly face", "Small nose", "Wears piercings", "Wears formal clothes", "Long hair (down to the shoulders)", "Large visible tattoos", "Stylish beard or makeup", "Extremely tall", "Stylish haircut (mohawk, undercut...)", "Wears designer clothes", "Very long hair (down to the waist)", "Eye twitch", "Bald, balding, or shaved head", "Large and expressive eyes", "Toothless", "Rare eye colors (blue, green, amber...)", "Eyes of different colors"]
        personalities: list = ["Very religious, quotes sacred passages", "Follows the law to the letter", "Can't remember proper names", "Always fixing their hair", "Energetic, doesn't let anyone stand still", "Romantic and believes in the good in everyone", "Anxious and bites nails", "Methodical and perfectionist", "Gets angry easily and doesn't take insults lightly", "Observant and curious", "Ambitious and calculating", "Friendly and loves to party", "Thoughtful and absent-minded", "Respectful and polite", "Careful, thinks before speaking", "Courageous", "Excitable and talkative", "Serious and formal", "Innocent and optimistic", "Stubborn", "Distrustful and pessimistic", "Playful and informal", "Shy and modest", "Cowardly", "Impulsive, speaks before thinking", "Rude and vulgar", "Talks non-stop and with everyone", "Likes to be alone", "Bossy and authoritarian", "Annoying and clingy", "Cynical and insensitive", "Proud of their work", "Always tries to gain an advantage", "Responsible and takes their word very seriously", "Lazy and yawns constantly", "Sneezes or coughs frequently", "Enjoys humming cheerfully", "Likes to negotiate favors", "Superstitious, carries lucky charms"]

        name: str = random.choice(names)
        stage: str = random.choice(stages)
        age: int = 0
        appearance: str = random.choice(appearances)
        personality: str = random.choice(personalities)

        match stage:
            case "Elderly":
                age = random.randint(1, 20) + 64
            case "Mature":
                age = random.randint(1, 20) + 44
            case "Adult":
                age = random.randint(1, 20) + 24
            case "Young":
                age = random.randint(1, 8) + 16
            case "Teenager":
                age = random.randint(1, 4) + 12
            case "Child":
                age = random.randint(1, 6) + 6

        return {
            "Name": name,
            "Stage": stage,
            "Age": age,
            "Appearance": appearance,
            "Personality": personality,
        }

    @staticmethod
    def MISSION() -> dict:
        elements = ["Blood", "Death", "Knowledge", "Energy"]
        subjects = ["Curious innocent", "Criminal", "Influential person", "Cult gang", "Independent cultist", "Former agent of Ordo Realitas", "Cursed item", f"Paranormal Creature of {random.choice(elements)}"]
        actions = [f"Intentionally summoned a {random.choice(elements)} creature", f"Accidentally summoned a {random.choice(elements)} creature", "Kidnapping innocent people", "Murdering innocent people", "Using a cursed ritual or item to commit mundane crimes", "Recruiting occultists", "Researching a dangerous ritual", "Collecting cursed items", "Killed an Ordo Realitas agent"]
        locations = ["School", "Hospital", "Village", "Deep forest", "Metropolitan alleys", "Skyscraper", "Large department store", "Sewer", "Industrial area of the city", "Shopping center", "Orphanage", "Museum", "Cemetery", "Police station or military base", "Mansion", "Former headquarters of Ordo Realitas", "Ship", "Remote island"]
        allies = ["Unaware civilian", "Exposed civilian", "Former acquaintance of one of the agents", "Another agent of Ordo Realitas"]
        objects = ["Equipment", "Ingredient for a powerful ritual", f"Equipment with {random.randint(1, 2)} modifications"]
        events = ["Appearance of another powerful paranormal creature", "Arrival of enemy reinforcements", "A paranormal disease/curse affecting the ally", "Civilians rebelling against them", "Revelation that the ally was the villain", "Revelation that the enemy's actions were justified", "Loss of their equipment", "Having to protect a civilian", "Loss of communication with Ordo Realitas and access to the credit system", "Law enforcement agents bothering them", "A disaster (fire, storm, hurricane, blackout, civil unrest...)", "Appearance of an old enemy"]

        return {
            "Element": random.choice(elements),
            "Subject": random.choice(subjects),
            "Action": random.choice(actions),
            "Location": random.choice(locations),
            "Ally": random.choice(allies),
            "Object": random.choice(objects),
            "Event": random.choice(events)
        }
