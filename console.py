#!/usr/bin/python3
"""console module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """console class for HBNB; AirBnb clone
    """
    available_dictionary = {"BaseModel": BaseModel, "User": User}
    available_names = ['BaseModel', 'User']
    prompt = "(hbnb)"

    def do_quit(self, line):
        """implements the quit command
        """
        return True

    def do_EOF(self, line):
        """implements EOF input
        """
        print()
        return True

    def emptyline(self):
        """implements empty line as command
        """
        pass

    def do_create(self, line):
        """creates a new instance, saves to json file then prints it's id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.available_names:
            print("** class doesn't exist **")
        else:
            class_ = self.available_dictionary[line]
            dummy = class_()
            dummy.save()
            print(dummy.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            # classname, id_value = line.split(" ")
            parts = line.split()
            classname = parts[0]
            if classname not in self.available_names:
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                id_value = parts[1]
                obj_dictionary = storage.all()
                name_and_id = classname + "." + id_value
                if name_and_id not in obj_dictionary.keys():
                    print("** no instance found **")
                else:
                    actual_object = obj_dictionary[name_and_id]
                    print(actual_object)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id and saves the changes into the JSON file
        """
        if not line:
            print("** class name missing **")
        else:
            parts = line.split()
            classname = parts[0]
            if classname not in self.available_names:
                print("** class doesn't exist **")
            elif len(parts) < 2:
                print("** instance id missing **")
            else:
                id_value = parts[1]
                obj_dictionary = storage.all()
                name_and_id = classname + "." + id_value
                if name_and_id not in obj_dictionary.keys():
                    print("** no instance found **")
                else:
                    obj_dictionary.pop(name_and_id)
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all
        """
        if line and line not in self.available_names:
            print("** class doesn't exist **")
        else:
            obj_dictionary = storage.all()
            new_dictionary = {}
            if line:
                for key, value in obj_dictionary.items():
                    if key.startswith(line):
                        new_dictionary[key] = value
            else:
                for key, value in obj_dictionary.items():
                    new_dictionary[key] = value
            # next we iterate over new_dictionary.values() calling __str__ on it
            ls = []
            for value in new_dictionary.values():
                ls.append(value.__str__())
            if len(ls) < 1:
                pass
            else:
                print(ls)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute and saves the change into the JSON file
        """
        parts = line.split()
        # if not line:
        if len(parts) == 0:
            """ (ex: $ update)
            """
            print("** class name missing **")
        elif len(parts) > 0:
            _name = parts[0]
            if _name not in self.available_names:
                """ (ex: $ update MyModel)
                """
                print("** class doesn't exist **")
            elif len(parts) == 1:
                """ (ex: $ update BaseModel)
                """
                print("** instance id missing **")
            elif len(parts) == 2:
                """ (ex: $ update BaseModel 121212)
                """
                _name = parts[0]
                _id = parts[1]
                unique_id = _name+ "." + _id
                obj_dictionary = storage.all()
                if unique_id not in obj_dictionary.keys():
                    print("** no instance found **")
            elif len(parts) == 3:
                """(ex: $ update BaseModel existing-id)
                """
                print("** attribute name missing **")
            else:
                _name = parts[0]
                _id = parts[1]
                _key = parts[2]
                _value = parts[3]
                unique_id = _name + "." + _id
                obj_dictionary = storage.all()
                """for key in obj_dictionary.keys():
                    flag = 0
                    if unique_id == key:
                        flag = 1
                if flag == 0:
                    print("** no instance found **")
                """
                if _key == "My_Number":
                    """type cast to correct attribute name
                    """
                    _val = int(_val)
                unique_object = obj_dictionary[unique_id]
                setattr(unique_object, _key, _value)
                unique_object.save()
                """unique_object_dictionary = unique_object.to_dict()
                unique_object_dictionary[_key] = _value
                unique_object.save()
                """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
