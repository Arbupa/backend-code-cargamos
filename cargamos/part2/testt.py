# a = 5 * 2
# print(a)
values = [i for i in range(1, 10)]
# squares = ["" for i in range(1, 85)]
# leng = 12


def add_value(val, x, y, z):
    max_num2 = x * y * z
    print("max_num2 es: ", max_num2)

    max_num = x * y * z
    z_maximum = max_num = int(max_num / z)  # 3
    # print(max_num)
    print("z increment by: ", z_maximum)
    # print()
    y_maximum = max_num = int(max_num / y)  # 1
    # print(max_num)
    print("y increment by: ", y_maximum)
    # print()
    x_maximum = max_num = int(max_num / x)  # 1
    # print(max_num)
    print("x increment by: ", x_maximum)

    x_counter = 1
    y_counter = 1
    z_counter = 1

    x_val = 1
    y_val = 1
    z_val = 1

    cube_list = []
    for i in range(1, max_num2 + 1):

        if i == 1:
            cube_list.append({f"{z_val}{y_val}{x_counter}": {i}})
            continue

        z_counter += 1

        if z_counter == z_maximum+1:
            z_val += 1
            z_counter = 1
        # cube_list.append({f"{z_val}{y_val}{x_counter}": {i}})

        x_counter += 1
        y_counter += 1

        # if z_counter == z_maximum:
        #     z_val += 1
        # if y_counter ==
        if y_counter == y_maximum+1:
            y_val += 1
            y_counter = 1
        # aqui va lo del valor del dict

        # aqui va lo del valor del dict
        if y_val == y + 1:
            y_val = 1
        # z_counter += 1
        # esto va al final, son las reglas para reiniciar el contador
        if x_counter == 4:
            x_counter = 1

        cube_list.append({f"{z_val}{y_val}{x_counter}": {i}})

        # if x_val == x_maximum and x_val <= x:
        #     x_val += 1

        # if y_val == y_maximum and y_val <= y:
        #     y_val += 1

        # if z_val == z_maximum and z_val <= z:
        #     z_val += 1

        # cube_list.append({f"{z_val}{y_val}{x_val}": i})

    print(cube_list)


lista = {'latitude1': 41.123, 'longitude1': 71.091,
         #  'latitude2': 41.123, 'longitude2': 71.091,
         #  'latitude3': 41.123, 'longitude3': 71.091,
         #  'latitude4': 41.123, 'longitude4': 71.091,
         #  'latitude5': 41.123, 'longitude5': 71.091,
         }

# for k, v in lista:
#     print("Key es: ", k)
#     print("Value es: ", v)

lista["segundo"] = 2
key = "segundo"

if key in lista:
    print("Key exists")
    print(lista[key])
else:
    print("Key does not exist")


print(lista)


list_of_values = ['Miau', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                  '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

values_list = [val for val in list_of_values if val != '']
print(values_list)
# add_value("a", 3, 4, 7)


# print(squares)
