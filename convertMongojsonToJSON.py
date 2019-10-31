import json
import re

#This will outputs a iterator that converts each file line into a dict.
def readBsonFile(filename):
    data = []
    with open(filename, "r") as data_in:
        for line in data_in:
            # convert the TenGen JSON to Strict JSON
            jsondata = re.sub(r'\:\s*\S+\s*\(\s*(\S+)\s*\)',
                              r':\1',
                              line)

            # parse as JSON
            line_out = json.loads(jsondata)

            #yield line_out
            data.append(line_out)
    return data


if __name__ == '__main__':
    import sys
    result = readBsonFile(sys.argv[1])
    
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile)