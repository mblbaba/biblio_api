def serialize_users(users):
    serialized_users = []
    for user in users:
        serialized_user = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'fisrt_name': user.fisrt_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'avatar_url': user.avatar_url,
            }
        serialized_users.append(serialized_user)
    return serialized_users

def serialize_user(user):
    serialized_user = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'fisrt_name': user.fisrt_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'avatar_url': user.avatar_url,
        }
    return serialized_user


    