import Application


if __name__ == "__main__":
    app = Application.Application()
    app.sim_folder = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/"
    app.spec = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/specs_and_measures.txt"
    app.netlist = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/two_stage_opamp_ac_deck.txt"
    app.parameter_constraints = {"w": (0.2, 2.4), "l": (0.03, 0.03), "nf": (1, 10)}
    app.scales = {"pic": 10**-12, "pico": 10**-12, "nan": 10**-9, "nano": 10**-9, "0": 1, "kil": 10**3 , "kilo": 10**3, "meg": 10**6, "mega":  10**6}


    print(app.run_genetic_algo(100, 100))