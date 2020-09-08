__doc__ = '''
Receive the encoded string from your friend and decode it  to check the original 
message. PS:  You will receive Encoded string and the Algorithm used for encoding.

'''
import base64

s = b'This is encoded message!!!'
encStr = "dGhpcyBpcyB0byBjaGVjayBmb3IgZW5jb2RlIGFuZCBkZWNvZGU="
decStr = encStr.encode()
print(f"Encoded String: {encStr.encode()}")
print(f"Decoded String: {decStr.decode()}")

if __name__ == '__main__':
    pass