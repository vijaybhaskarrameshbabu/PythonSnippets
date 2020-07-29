
import json
import objectpath
import pprint 

with open ('YourJSONFileName.json') as f:
    data = json.load(f)  #Load JSON File 
json_tree = objectpath.Tree(data['YOUR_JSON_FIELD_NAME'])
result_tuple = tuple(json_tree.execute('$.origin_domain'))
pprint.pprint (result_tuple)

with open ('output.txt', 'w') as outfile:
    json.dump(result_tuple, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)




