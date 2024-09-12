import json

def print_json(filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        classes = file_data[0]
        relationships = file_data[1]
        print("CLASSES --")
        for cls in classes:
            class_name = cls["class_name"]
            print("  "+class_name)
            attr_list = cls["attr_list"]
            for attribute in attr_list:
                print("    - " + attribute["attr_name"])
        print()
        print("RELATIONSHIPS --")
        for rela in relationships:
            source_cls = rela["source"]
            dest_cls = rela["dest"]
            relat_name = rela["relation"]
            print("  "+source_cls + " --> " + dest_cls + "     called " + relat_name)

def class_exists(class_name, classes:list):
    for cls in classes:
        if (cls["class_name"] == class_name):
            return True
    return False    

