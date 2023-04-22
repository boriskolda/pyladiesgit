def prijmeni(jmeno):
    if jmeno.endswith("ová") or jmeno.endswith("á"):
        return "zena"
    else:
        return "muz"
    

jmeno = print(prijmeni(input("Zadej prijmeni: ")))

