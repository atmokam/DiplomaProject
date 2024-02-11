import Application


if __name__ == "__main__":
    app = Application.Application()
    app.sim_folder = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/"
    app.spec_path = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/specs_and_measures.txt"
    app.netlist_path = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/two_stage_opamp_ac_deck.txt"

    app.run_genetic_algo(10, 10)