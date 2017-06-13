'''
In Python 3, str is a Unicode string.
Unicode is a standard for working with a wide range of characters. 
Each symbol has a codepoint (a number), and these codepoints can be encoded 
(converted to a sequence of bytes) using a variety of encodings.
UTF-8 is one such encoding. The low codepoints are encoded using a single byte, 
and higher codepoints are encoded as sequences of bytes.
The line s = unistring.encode('utf-8') encodes the Unicode string using UTF-8. 
This converts each codepoint to the appropriate byte or sequence of bytes. 
The result is a collection of bytes, which is returned as a str.


'''
text = ['\u2014']
print(text) #['—']
#print(str(text, encoding='utf-8', errors='ignore')) #erroe
print(ascii(text)) #['\u2014']