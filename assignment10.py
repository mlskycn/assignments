age = input("Are you a cigarette addict older than 75 years old? (Yes/No)").strip().capitalize()
chronic = input("Do you have a severe chronic disease? (Yes/No)").strip().capitalize()
immune = input("Is your immune system too weak? (Yes/No)").strip().capitalize()

is_age_risky = age == "Yes"
has_chronic_disease = chronic == "Yes"
is_immune_weak = immune == "Yes"

if is_age_risky or has_chronic_disease or is_immune_weak:
    print("You are in the risky group.")
else:
    print("You are not in the risky group.")