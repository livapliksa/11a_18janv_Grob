def nolasit(faila_nosaukums):
    
    try:
        with open(faila_nosaukums, 'r') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2].strip() 
                print(f"Trešās rindas saturs no faila '{faila_nosaukums}':")
                print(tresa_rinda)
            
            else:
                print(f"Failā '{faila_nosaukums}' nav pietiekami daudz rindu!")
    
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' netika atrasts.")
    
    except PermissionError:
        print(f"Kļūda: Nevar nolasīt failu '{faila_nosaukums}'.")
    
    except Exception as e:
        print(f"Neparedzēta kļūda: {e}")


faila_nosaukums = input("Ievadiet teksta faila nosaukumu: ")


nolasit(faila_nosaukums)