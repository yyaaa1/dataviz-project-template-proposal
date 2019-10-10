import pandas as pd

def generate_crime_rate_vs_years(input_path,output_path):
    map_ = {}
    with open(input_path) as f:
        f.readline()
        serial = [4,5,6,7,8]
        for line in f:
            line = line.split(',')
            total_crimes = 0
            for i in serial:
                if line[i].isdigit():
                    total_crimes += int(line[i])
            pop = int(line[3]) if line[3].isdigit() else 0
            if line[1] not in map_:
                map_[line[1]] = [total_crimes,pop]
            else:
                map_[line[1]][0] += total_crimes
                map_[line[1]][1] += pop
    data = {'year':[],'crime_rate':[]}
    for k in map_:
        data['year'].append(k)
        data['crime_rate'].append(map_[k][0]/map_[k][1])
    pd.DataFrame.from_dict(data).to_csv(output_path,index = False)


if __name__ == "__main__":
    input_path = '/Users/yy/Desktop/2019Fall/DV/ucr_crime_1975_2015.csv'
    output_path = '/Users/yy/Desktop/crime_rate.csv'
    generate_crime_rate_vs_years(input_path,output_path)