def format_paise(paise):
    negative = ""
    if paise < 0:
        negative = "-"
        paise = -paise
    rupees = paise // 100
    cents = paise % 100
    if cents < 10:
        return negative + str(rupees) + ".0" + str(cents)
    return negative + str(rupees) + "." + str(cents)

def make_member(name):
    return {"name": name}

def make_expense(description, amount, paid_by, shares, split_type="equal"):
    return {
        "description": description,
        "amount": amount,
        "paid_by": paid_by,
        "shares": shares,
        "split_type": split_type,
    }

def make_settlement(payer, paid, amount):
    return {
        "payer": payer,
        "paid": paid,
        "amount": amount,
    }

def make_group(name):
    return {
        "name": name,
        "members": [],
        "expenses": [],
    }

def find_member(group, name):
    name = name.strip().lower()
    for member in group["members"]:
        if member["name"].lower() == name:
            return member
    return None

def member_names(group):
    names = []
    for member in group["members"]:
        names.append(member["name"])
    return names

def add_member(group, name):
    member = make_member(name)
    group["members"].append(member)
    return member

def add_expense(group, expense):
    group["expenses"].append(expense)
    return expense

def total_spent(group):
    total = 0
    for expense in group["expenses"]:
        total += expense["amount"]
    return total