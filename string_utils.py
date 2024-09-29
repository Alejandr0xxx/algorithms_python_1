def explode_string(string):
    return [x if x != '.' else None  for x in string]

def explode_list_of_strings(string_list):   
    return [explode_string(s) for s in string_list if s != "|" and s != ""]