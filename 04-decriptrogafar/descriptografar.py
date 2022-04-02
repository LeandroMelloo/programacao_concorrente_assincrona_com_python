import base64
import json
from base64 import b64decode

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad


def decrypt(params):
    try:
        privateKey = open('./private.pem').read()

        string64 = params
        decode_64 = base64.b64decode(string64)
        values = json.loads(decode_64)

        res_iv = values['iv']
        res_keys = list(values['keys'].values())[0]
        res_cipher = values['cipher']

        ciphertext = base64.b64decode(res_keys)
        key = RSA.importKey(privateKey)
        cipher = PKCS1_OAEP.new(key)
        message = cipher.decrypt(ciphertext)
        hex_message = message.hex()

        iv = b64decode(res_iv)[:AES.block_size]
        key = bytes.fromhex(hex_message)
        ciphertext = b64decode(res_cipher)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

        return print(decrypted.decode('utf-8'))
    except Exception as error:
        print(error)

message = 'IHsidiI6Imh5YnJpZC1jcnlwdG8tanNfMC4yLjQiLCJpdiI6InNWNjRrT2VrbVF3OFpoM2U5UjhKWEU4dVR0T2tHcUlRcUxWclRHRFFiSms9Iiwia2V5cyI6eyI3OTpmNTo5NTpkMzo0Mzo4Yzo0NDo5YjowNTphOTo2NDowMTo4MjpiZjo4Nzo1YzpkMDpmNjowNzozNCI6ImJZV3VZQktaZjIvdWV6WTQyZmpFY3NnSHloakhERDlYVHRpa3pzZDEvWWcrZm9TUHVESTc1WUlIejIyLzgwZlJMSnRpcW5zQXNwK2lndUhhaXZ0WnI3ckZRR2o3a2tzaWo0U2lCalhOcE1BdmJrSlA1UkNTeW5ocDV5MDhSZUFOWEE5bHlwVU14TU1OUW9qRmZyNTJ0MHhWNGJPWGk5RXhnR3VNSEV4bktxWGxpU3g3aCtWYWNRcnNxalRSZlkrT2Q4RzVzbkpHSGxhUnBpQXNDQjZaUjlNQjJHSlRQTzJuTHMrSCt6d0xyaDF3SkNlaU9kWFliL3FiYkxvei9ZUnZ0VzBPTjVxKzJXSWl4UVhBb3M0NmI3T0ViOUpTNzc1RmpTOGoyV1FydDhVaHZDSGpIang2TUY0RzNZd3orcitUaGd0OWVqSGUzY2pEUVJ4bTdCbkoxZS9MRGhIRWJLOTFwVkY5NTNtUSswT2k0WVg3elNpTUF2QTMzTzU4eDJLZzI0TUdLVmJNcjhKcjJLemN1bGEwdStXZDJYdEdHeWp4K00wY2dVUXBZT2RIOFlVcTN0bjlRRzdoNFgyV3BqYzF4Mk51NE5DZG93U05UNTEwNHhQTHdtV1BZNnpCWW92aXN2TFdhdU1MeDE3a1NmdVVBb2lpTjIzSDFIa1ZzRGZ2Z0V3UXdBZmU1c0RuVml1NytHd0RQdlkyZUNLelQ3ZVNEaHQwUXJVQTFUL05OVm9OQU5Wc3VPc01aeVAyZG1ZK2JvcXFaUkV2RHBUZTlEemJtWDBNY3lmSUpXWW92ZXhuY2kreVhNZEdxcTVWL3dDQ05ueFJZUjdvRjlVYXFSSFFwc1g5eHhCVlkzOUpKamovOVZMRGtLTTdDWndWRDZ5d3AyZGFBTTQ4biswPSJ9LCJjaXBoZXIiOiJ0eUpwUWJrNmFyQXpPRzB4MUdHZlF3PT0ifQ=='

decrypt(message)
