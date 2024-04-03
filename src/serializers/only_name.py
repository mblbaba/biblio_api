def serialize_only_names(instance):
    serialized_only_names = []
    for item in instance:
        n_item = {
            "name" : item.name,
            "id" : item.id
        }
        serialized_only_names.append(n_item)
    return serialized_only_names


def serialize_only_name(instance) :
    serialized_instance = {
        "id" : instance.id,
        "name" : instance.name
    }
    return serialized_instance