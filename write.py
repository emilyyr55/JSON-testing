import json

# Create a new class
def add_class(class_name:str, filename='data.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        if not file_data:
            file_data = [[{"class_name": class_name, "attr_list" : []}],[]]
        else:
            # Join new_data with file_data inside emp_details
            file_data[0].append({"class_name": class_name, "attr_list" : []})
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        file.close()



def delete_class(class_name: str, filename='data.json'):
    obj  = json.load(open(filename))
    classes = obj[0]
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
    for i in range(len(classes)):
        if (classes[i]["class_name"] == class_name):
            classes.pop(i)
            break

    # Output the updated file with pretty JSON                                      
    open("data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )

def edit_class(old_class_name: str, new_class_name:str, filename='data.json'):
    obj  = json.load(open(filename))
    classes = obj[0]                                                     
    for i in range(len(classes)):
        if (classes[i]["class_name"] == old_class_name):
            classes[i]["class_name"] = new_class_name
            break

    # Output the updated file with pretty JSON                                      
    open("data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )
    
def add_attr(class_name: str,attr_name:str, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        classes = file_data[0]
        for cls in classes:
            if (cls["class_name"] == class_name):
                attr_list = cls["attr_list"]
                attr_list.append({"attr_name": attr_name})
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        file.close()

def delete_attr(class_name: str,attr_name: str, filename='data.json'):
    obj  = json.load(open(filename))
    classes = obj[0]
    for cls in classes:
        if (cls["class_name"] == class_name):
            attr_list = cls["attr_list"]
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
            for i in range(len(attr_list)):
                if (attr_list[i]["attr_name"] == attr_name):
                    attr_list.pop(i)
                    break

    # Output the updated file with pretty JSON                                      
    open("data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )

def edit_attr(class_name: str,old_attr_name: str, new_attr_name:str, filename='data.json'):
    obj  = json.load(open(filename))
    classes = obj[0]
    for cls in classes:
        if (cls["class_name"] == class_name):
            attr_list = cls["attr_list"]
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
            for i in range(len(attr_list)):
                if (attr_list[i]["attr_name"] == old_attr_name):
                    attr_list[i]["attr_name"] = new_attr_name
                    break

    # Output the updated file with pretty JSON                                      
    open("data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )

def add_relation(source:str,dest:str, relation:str, filename='data.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[1].append({"source": source, "dest": dest,"relation": relation})
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        file.close()

def delete_relation(source:str, dest:str, relation:str, filename='data.json'):
    obj  = json.load(open(filename))
    relations = obj[1]
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
    for i in range(len(relations)):
        if (relations[i]["source"] == source):
            if (relations[i]["dest"] == dest):
                if (relations[i]["relation"] == relation):
                    relations.pop(i)
                    break

    # Output the updated file with pretty JSON                                      
    open("data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )

def edit_relation(source: str, dest: str, relation:str,new_relation:str, filename='data.json'):
    obj  = json.load(open(filename))
    relations = obj[1]
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
    for i in range(len(relations)):
        if (relations[i]["source"] == source):
            if (relations[i]["dest"] == dest):
                if (relations[i]["relation"] == relation):
                    relations[i]["relation"] = new_relation
                    break

    # Output the updated file with pretty JSON                                      
    open("data.json", "w").write(
        json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    )
