from hmac import compare_digest

from src.models.device import Device

def is_valid(api_key):
    device = Device.find_by_api_key(api_key)
    if device and compare_digest(device.api_key, api_key):
        return True