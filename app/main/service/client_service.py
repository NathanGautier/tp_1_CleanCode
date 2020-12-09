from functools import reduce


# variables
r2_key = 'Z'
r2_identifier = '00'


# fonction qui permet de vérifier la composition d'un identifiant client
def verify_id(key_entry, id_entry):
    # variables
    success = False
    id_entry_list = list(id_entry)
    # on applique la regle 2
    first = first_int(id_entry)
    if first is True:
        if key_entry == r2_key:
            success = True
    else:
        # on applique la regle 1
        id_calc = calculate_id(id_entry_list)
        if id_calc == -1:
            success = False
        else:
            letter = calculate_letter(id_calc)
            if key_entry == letter:
                success = True
    # on renseigne l'objet de retour de la fonction
    if success:
        status = 'success'
        request = key_entry + id_entry
        result = 1
    else:
        status = 'failed'
        request = key_entry + id_entry
        result = 0
    return response_object(status, request, result)


# fonction qui permet d'additionner les chiffres de l'identifiant entre eux
def calculate_id(id_entry):
    str(id_entry)
    list(id_entry)
    res = 0
    if len(id_entry) > 1:
        for char in id_entry:
            res += int(char)
    else:
        res = -1
    return res


# fonction qui retourne le 1er caractere ous forme de int
def first_int(id_entry):
    id = id_entry[:1]
    if id == r2_identifier:
        return True
    else:
        return False


# fonction qui vérifie si le paramètre donné est un int
def is_int(id_entry):
    result = True
    try:
        for char in id_entry:
            if int(char) is False:
                return False
    except ValueError:
        result = False
    return result


# fonction qui permet de retourner une lettre
# par rapport a la valeur du paramètre
def calculate_letter(id_entry):
    index = int(id_entry)
    while index > 15:
        index_list = str(index)
        index_list = list(index_list)
        index = calculate_id(index_list)
    return chr(65 + index)


# fonction qui retourne un objet
def response_object(status, request, result):
    res = {
        'status': status,
        'request': request,
        'result': result
    }
    return res


# fonction de creation de l'identifiant
def creation_id(id_entry):
    status = 'failed'
    request = id_entry
    result = None
    if id_entry[:2] == r2_identifier:
        id_new = r2_key
    else:
        try:
            id = calculate_id(id_entry)
        except Exception:
            return response_object(status, request, result)
        if id == -1:
            return response_object(status, request, result)
        try:
            letter = calculate_letter(id)
        except Exception:
            return response_object(status, request, result)
        id_new = letter
        id_new += str(id_entry)
    return response_object('success', id_entry, id_new)
