def nolasit_un_drukaz_faila_saturu(faila_nosaukums):
    
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print(f"Faila '{faila_nosaukums}' saturs:")
            print(saturs)
    
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' netika atrasts.")
    
    except PermissionError:
        print(f"Kļūda: Nav tiesību nolasīt failu '{faila_nosaukums}'.")
    
    except Exception as e:
        print(f"Neparedzēta kļūda: {e}")


faila_nosaukums = input("Ievadiet faila nosaukumu: ")
faila_formats = input("Ievadiet faila formātu : ")


pilns_faila_nosaukums = f"{faila_nosaukums}.{faila_formats}"


nolasit_un_drukaz_faila_saturu(pilns_faila_nosaukums)