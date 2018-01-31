def correct_unicode_to_bytes(bad_bytestr=br'Sebastian Pr\u00c3\u00b6dl, Abdoulaye Doucour\u00c3\u00a9'):
    bs = bad_bytestr.decode()
    if bs.find('\\u00') == -1:
        return bs
    else:
        i1 = bs.find('\\u00')
        i2 = i1 + bs[i1+1:].find('\\u00') + 1
        b1 = bs[i1:i1+6]
        b2 = bs[i2:i2+6]
        to_replace = bytes(b1 + b2, 'utf-8')
        ba = bytes.fromhex(b1[4:]+b2[4:])
        corrected = bytes(bs, 'utf-8').replace(to_replace, ba)
        return correct_unicode_to_bytes(corrected)



Response received looks like `Sebastian Pr\\u00c3\\u00b6dl`

(We can ignore the double backslash as not relevant to the main question I think. I think that's from python printing it out at a prompt?)

The JSON standard says that unicode strings should be represented by a `\u` followed by 4 hexidecimal digits (http://www.json.org/) So on the face of it that looks like it contains two unicode characters:
Unicode code point 00c3 and Unicode code point 00b6

But those don't seem to be the right characters:

Unicode 00C3
LATIN CAPITAL LETTER A WITH TILDE
http://www.fileformat.info/info/unicode/char/00c3/index.htm

Unicode 00b6
PILCROW SIGN
http://www.fileformat.info/info/unicode/char/00b6/index.htm

And python3 confirms that:

```
In [6]: s = '\u00c3\u00b6'
In [7]: print(s)
Ã¶
```

However, if we instead treat c3 and b6 as two bytes of UTF-8 encoded text, then
we get the right answer:

```
In [24]: b'\xc3\xb6'.decode('utf-8')
Out[24]: 'ö'
```

So is it possible that this is a bug in the API, and they are incorrectly putting the UTF-8 hexidecimals c3 and b6 into their JSON response and adding `\u` to indicate that it's unicode, whereas what they should be putting in their JSON is the unicode code point 246 (f6)?

We can prove that it's the unicode code point and not the UTF-8 bytes that should be in the JSON:

```
In [47]: o_umlaut = b'\xc3\xb6'.decode('utf-8')

In [49]: ord(o_umlaut)
Out[49]: 246  # Unicode code point 246

In [51]: print(json.dumps(o_umlaut))
"\u00f6"
In [55]: json.loads(json.dumps(o_umlaut))
Out[55]: 'ö'
```

versus

```
In [59]: json.loads('"\u00c3\u00b6"')
Out[59]: 'Ã¶'
```
