# https://github.com/python/cpython/commits/master/Lib/lib2to3/fixes/fix_urllib.py
# https://github.com/python/cpython/blob/531d1e541284bfd7944f8c66a5e8c3c3234afaff/Lib/lib2to3/fixes/fix_urllib.py#L12-L45
MAPPING = {"urllib":  [
                ("urllib.request",
                    ["URLopener", "FancyURLopener", "urlretrieve",
                     "_urlopener", "urlopen", "urlcleanup",
                     "pathname2url", "url2pathname", "getproxies"]),
                ("urllib.parse",
                    ["quote", "quote_plus", "unquote", "unquote_plus",
                     "urlencode", "splitattr", "splithost", "splitnport",
                     "splitpasswd", "splitport", "splitquery", "splittag",
                     "splittype", "splituser", "splitvalue", ]),
                ("urllib.error",
                    ["ContentTooShortError"])],
           "urllib2" : [
                ("urllib.request",
                    ["urlopen", "install_opener", "build_opener",
                     "Request", "OpenerDirector", "BaseHandler",
                     "HTTPDefaultErrorHandler", "HTTPRedirectHandler",
                     "HTTPCookieProcessor", "ProxyHandler",
                     "HTTPPasswordMgr",
                     "HTTPPasswordMgrWithDefaultRealm",
                     "AbstractBasicAuthHandler",
                     "HTTPBasicAuthHandler", "ProxyBasicAuthHandler",
                     "AbstractDigestAuthHandler",
                     "HTTPDigestAuthHandler", "ProxyDigestAuthHandler",
                     "HTTPHandler", "HTTPSHandler", "FileHandler",
                     "FTPHandler", "CacheFTPHandler",
                     "UnknownHandler"]),
                ("urllib.error",
                    ["URLError", "HTTPError"]),
           ]
}

# Duplicate the url parsing functions for urllib2.
MAPPING["urllib2"].append(MAPPING["urllib"][1])

for old in MAPPING:
    for new, names in MAPPING[old]:
        for name in names:
            print(f"'library/{old}.html#{old}.{name}': 'library/{new}.html#{new}.{name}',")
