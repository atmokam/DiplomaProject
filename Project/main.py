import Application


if __name__ == "__main__":
    app = Application.Application()
    app.spec_file = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/specs_and_measures.txt"
    app.netlist_file = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/two_stage_opamp_ac_deck.txt"
    app.run_genetic_algo(10, 10)