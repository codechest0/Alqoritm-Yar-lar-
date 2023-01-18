import json

def Promotion(region):
    with open("oldorders.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    promotions = {}

    for order in data["customers"]:
        if order["region"] == region:
            promotion = order["promotion"]
            if promotion in promotions:
                promotions[promotion] += 1
            else:
                promotions[promotion] = 1

    return list(promotions.keys())

print(Promotion("D"))