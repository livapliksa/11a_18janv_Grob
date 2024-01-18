def ierakstit_faila(vards, faila_nosaukums='lietotajs.txt'):
    
    try:
        with open(faila_nosaukums, 'a') as fails:
            fails.write(vards + '\n')
        print(f"Vārds '{vards}' ierakstīts failā '{faila_nosaukums}'.")
    
    except IOError as e:
        print(f"Kļūda: Nevarēja vārdu ierakstīt failā '{faila_nosaukums}'.")
        print(f"Vairāk informācijas par kļūdu: {e}")
    
    except Exception as e:
        print(f"Neparedzēta kļūda: {e}")

lietotaja_vards = input("Ievadiet savu vārdu: ")

ierakstit_faila(lietotaja_vards)
