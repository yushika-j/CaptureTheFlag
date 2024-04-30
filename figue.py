def parse_fig_file(file_path):
    shapes = []
    with open(file_path, 'r') as fig_file:
        for line in fig_file:
            if line.startswith('3'):  # Assuming lines starting with '3' represent coordinate data
                # Split the line and extract the coordinate values
                coordinates = line.strip().split()[1:]
                print(coordinates)
              
                # Assuming each coordinate is represented as a pair of x, y values
                coordinates = [(float(coordinates[i]), float(coordinates[i+1])) for i in range(0, len(coordinates), 2)]
                shapes.append(coordinates)
    return shapes

def main():
    file_path = 'figue.fig'  # Replace 'your_fig_file.fig' with the path to your FIG file
    parsed_shapes = parse_fig_file(file_path)
    # Print the parsed coordinate data
    for shape in parsed_shapes:
        print(shape)

if __name__ == "__main__":
    main()