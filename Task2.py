import requests
import json

metadata_url= 'https://169.254.169.254/latest/'
def expand_tree(url,arr):

    output= { }
    for item in arr:
        new_url=url+item
        r=requests.get(new_url)
        text=r.text
        if item[-1]== "/":
            list_of_values= r.text.splitlines()
            output[item[:-1]]= expand_tree(new_url,list_of_values)
        elif is_json(text):
            output[item]= text
            return output
        def get_metadata():
            initial= ["meta-data/"]
            result= expand_tree(metadata_url,initial)
            return result
        def get_metadata_json():
            metadata_json()= json.dumps(metadata,indent=4,sort_keys=true)
            return metadata_json
        def is_json(myjson):
            try:
                json.loads(myjson)
                expectvalueerror:
                return false
            return true
        if __name__== '__main__':
            print(get_metadata_json()
