def lasit_un_drukat(txt_fails):
    try:
        with open(txt_fails, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{txt_fails}' netika atrasts.")
    except Exception as e:
        print(f"Kļūda: Neparedzēta kļūda: {e}")

txt_fails = 'jusu_fails.txt'
lasit_un_drukat(txt_fails)
