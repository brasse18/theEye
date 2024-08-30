
def main():
    #(1 = ON, 0 = OFF)
    input_data = [1, 0, 1, 1]
    print(input_data)
    leaning_data = get_training_data("training_data.txt")
    print(leaning_data)

def get_training_data(file_path):
    data_points = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' = ')
            array_str = parts[0]
            value_str = parts[1]

            array = list(map(int, array_str.split(',')))

            value = int(value_str)

            data_point = DataPoint(array, value)
            data_points.append(data_point)

    return data_points

class DataPoint:
    def __init__(self, input_array = [1,1,1,1], output_value = 1):
        self.input_array = input_array
        self.output_value = output_value

    def __repr__(self):
        return f"(Input={self.input_array}, output={self.output_value})"

if __name__ == "__main__":
    main()

