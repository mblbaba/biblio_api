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

def serialize_notification(notification):
    serialized_notification = {
            'id': notification.id,
            'icon': notification.icon,
            'message': notification.message,
            'created_at': notification.created_at,
            'read': notification.read,
            'user_id': notification.user_id
    }
    return serialized_notification

def serialize_notifications(notifications):
    serialized_notifications = []
    for notification in notifications:
        serialized_notification = serialize_notification(notification)
        serialized_notifications.append(serialized_notification)
    return serialized_notifications


    