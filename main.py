'''Fuel energy values

   1 line - fuel/min
   2 line - energy MW
   3 line - +Fluid per minute with overclocking
'''

'''Oil extractor values
Rare oil
    1 line - impure
    2 line - normal
    3 line - pure
'''
import json
import math
print('Welcome, it is Fuel Energy Calculator (By HLNikNiky)')
input_user_energy = int(input('Input how many MW you need: '))
input_rare_of_oil = int(input("Input Rare of you'r oil: 1-impure, 2-normal, 3-pure: "))
input_user_powershard = int(input('Input how many you powershard: '))


#Просчитывает сколько нужно генераторов для выдачи энергии которую запросил пользователь
def energy_gen_calc():
    with open("fuel_gen_val.json") as json_file:
        energy_gen_need_output = json.load(json_file)
    token = energy_gen_need_output["MW"]
    print("You need fuel generators:")
    calc_ener = input_user_energy / token
    json_file.close()
    return calc_ener


#Просчитывает скольо нужно топлива в минуту для генераторов
def gen_need_fuel():
    with open("fuel_gen_val.json") as json_file:
        fuel_per_min = json.load(json_file)
    #if not input_user_powershard == 0:
        #energy_add = fuel_per_min["fluid_per_minute_with_plus"]

    token_one = fuel_per_min["MW"]
    token_two = fuel_per_min["fuel_per_min"]
    calc_ener = input_user_energy / token_one
    print('Fuel per min need:')
    #calc_add_fuel = energy_add * input_user_powershard
    calc_fuel = calc_ener * token_two
    json_file.close()
    return calc_fuel

#Просчитывает сколько нужно материалов для постройки генераторов
def materials_need_gen():
    with open("fuel_gen_val.json") as json_file:
        gen_need_materials = json.load(json_file)
    token_energy = gen_need_materials["MW"]
    token_one = gen_need_materials["Computers"]
    token_two = gen_need_materials["Heavy_Modular_Frame"]
    token_three = gen_need_materials["Rotors"]
    token_four = gen_need_materials["Rubber"]
    token_five = gen_need_materials["Quickwire"]
    calc_ener = input_user_energy / token_energy
    calc_computers = calc_ener * token_one
    calc_heavy_modular = calc_ener * token_two
    calc_rotors = calc_ener * token_three
    calc_rubber = calc_ener * token_four
    calc_quickwire = calc_ener * token_five

    fin_result = print('You need to build Fuel generators:',
                       math.ceil(calc_computers), '-Computers;',
                       math.ceil(calc_heavy_modular), '-Heavy Modulars Frame;',
                       math.ceil(calc_rotors), '-Rotors;',
                       math.ceil(calc_rubber), '-Rubbers;',
                       math.ceil(calc_quickwire), '-Quickwire')
    json_file.close()
    return fin_result

#Считает сколько нужно очистительных заводов
def refinery():
    with open("refinery_val.json") as json_file:
        refinery_values = json.load(json_file)
    with open("fuel_gen_val.json") as json_file1:
        fuel_gen_values = json.load(json_file1)
    token_energy = fuel_gen_values["MW"]
    calc_ener = input_user_energy / token_energy
    ref_fuel_output = refinery_values["fuel_ouptut_permin"]
    gen_fuel_values = fuel_gen_values["fuel_per_min"]
    calc_gen = gen_fuel_values * calc_ener
    result_ref = calc_gen / ref_fuel_output
    json_file.close()
    json_file1.close()
    print("You need Refiney:")

    return result_ref

#Сичтает сколько нужно насосов нефти для очистительных заводов
def oil_extract():
    with open("oil_ext_val.json") as json_file:
        oil_extra_val = json.load(json_file)
    with open("refinery_val.json") as json_file1:
        refinery_val = json.load(json_file1)
    with open("fuel_gen_val.json") as json_file2:
        fuel_gen = json.load(json_file2)
    token_energy = fuel_gen["MW"]
    calc_ener = input_user_energy / token_energy
    ref_fuel_output = refinery_val["fuel_ouptut_permin"]
    gen_fuel_values = fuel_gen["fuel_per_min"]
    calc_gen = gen_fuel_values * calc_ener
    result_ref = calc_gen / ref_fuel_output
    refinery = refinery_val["need_oil_Fuel_processing_permin"]
    res = result_ref * refinery

    if input_rare_of_oil == 1:
        oil_1 = oil_extra_val["impure"]
        oil_result = res / oil_1
    elif input_rare_of_oil == 2:
        oil_2 = oil_extra_val["normal"]
        oil_result = res / oil_2
    elif input_rare_of_oil == 3:
        oil_3 = oil_extra_val["pure"]
        oil_result = res / oil_3
    print("You need Oil Extractors:")
    return oil_result


print(energy_gen_calc())
print(gen_need_fuel())
materials_need_gen()
print(refinery())
print(oil_extract())
input()
