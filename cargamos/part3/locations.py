class Locations:

    def __init__(self, x_position: int, y_position: int, z_position: int) -> None:
        self.value = ""
        self.x_position = x_position
        self.y_position = y_position
        self.z_position = z_position
        self.cube_length = x_position * y_position * z_position
        self.list_of_values = ["" for i in range(1, self.cube_length + 1)]
        self.coordinates_and_value_index = {}
        # crear una lista con valores vacios en 0 del largo inicial de la instancia de
        # la clase, para después checar si la nueva posicion ingresada supera ese largo,
        # mostrar algun error o algo

    def save_value(self, value, x_position: int, y_position: int, z_position: int):

        key = f"{z_position}{y_position}{x_position}"

        if key in self.coordinates_and_value_index:
            index = self.coordinates_and_value_index[key]
            self.list_of_values[index - 1] = value
            print(f"Value {self.list_of_values[index]} saved successfully")
            print(self.list_of_values)

            return self.coordinates_and_value_index[key]

        else:
            print("Coordinates not found. Value not saved")
            return

    def get_value(self, x_position: int, y_position: int, z_position: int):

        key = f"{z_position}{y_position}{x_position}"

        if key in self.coordinates_and_value_index:
            # and self.coordinates_and_value_index[key] != ''
            # print("value is: ", self.coordinates_and_value_index[key])
            index = self.coordinates_and_value_index[key]
            value = self.list_of_values[index - 1]
            if value != '':
                print(value)
                return value

            else:
                print("Coordinates not found.")

    def create_cube(self) -> None:

        max_num2 = self.x_position * self.y_position * self.z_position
        print("max_num2 es: ", max_num2)
        max_num = max_num2
        z_maximum = max_num = int(max_num / self.z_position)  # 3
        print("z_position increment by: ", z_maximum)
        y_maximum = max_num = int(max_num / self.y_position)  # 1
        print("y_position increment by: ", y_maximum)
        x_maximum = max_num = int(max_num / self.x_position)  # 1
        print("x_position increment by: ", x_maximum)

        x_counter = 1
        y_counter = 1
        z_counter = 1
        y_val = 1
        z_val = 1

        for i in range(1, max_num2 + 1):

            if i == 1:
                # self.coordinates_and_value_index.append(
                #     {f"{z_val}{y_val}{x_counter}": {i}})
                self.coordinates_and_value_index[f"{z_val}{y_val}{x_counter}"] = i
                continue

            z_counter += 1

            if z_counter == z_maximum + 1:
                z_val += 1
                z_counter = 1

            x_counter += 1
            y_counter += 1

            if y_counter == y_maximum + 1:
                y_val += 1
                y_counter = 1

            if y_val == self.y_position + 1:
                y_val = 1

            if x_counter == 4:
                x_counter = 1

            # self.coordinates_and_value_index.append(
            #     {f"{z_val}{y_val}{x_counter}": {i}})
            self.coordinates_and_value_index[f"{z_val}{y_val}{x_counter}"] = i
        print(self.coordinates_and_value_index)

    def get_all(self):
        # print(self.list_of_values)
        values_list = [val for val in self.list_of_values if val != '']
        print(values_list)
        return values_list


if __name__ == "__main__":
    l = Locations(3, 4, 7)
    print(l.cube_length)
    l.create_cube()
    l.save_value("Miau", 1, 1, 1)
    l.save_value("guau", 3, 4, 5)
    l.get_value(1, 1, 2)
    l.get_value(1, 1, 1)
    l.get_all()
