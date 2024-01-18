import csv

csv_fails = 'reader.csv'


def lasit_un_drukaz_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r', newline='') as fails:
            csvLasitajs = csv.reader(fails)
            
            print("Otrās kolonnas dati:")
            for rinda in csvLasitajs:
                if len(rinda) >= 2: 
                    print(rinda[1])  
                else:
                    print("Ļoti grūts darbins.")

    except FileNotFoundError:
        print(f"Kļūda: Fails '{csv_fails}' netika atrasts.")
    except Exception as e:
        print(f"Kļūda: Neparedzēta kļūda: {e}")


csv_fails = 'reader.csv'
lasit_un_drukaz_otro_kolonnu(csv_fails)
