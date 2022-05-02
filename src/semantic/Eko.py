
from .QualifiedName import QualifiedName
from .Key import Key

class Eko: 

    def __init__(self, imports, dictionary):

        self.imports = imports
        self.dictionary = dictionary

        self.resolve_reference(self.dictionary)
        self.collapsed = self.get_collapsed(self.dictionary)

        print("==EKO==")
        print(self.collapsed)
        

    def resolve_reference(self,dictionary):

        for key,value in dictionary.items():
            if type(value) == QualifiedName: 
                # search in current dictionary
                walked_dict = self.dictionary
                for name in value:
                    if Key(name) not in walked_dict: break
                    walked_dict = walked_dict[Key(name)]
                else: 
                    dictionary[key] = walked_dict

                # search in import dictionaries
                for imp in self.imports:
                    walked_dict = imp.eko.dictionary
                    for name in value:
                        if Key(name) not in walked_dict: break
                        walked_dict = walked_dict[Key(name)]
                    else:
                        dictionary[key] = walked_dict

            if type(value) == dict: self.resolve_reference(dictionary[key])

    def get_collapsed(self,dictionary):
        return {key.key:(self.get_collapsed(value) if type(value) == dict else value) for key,value in dictionary.items()}


