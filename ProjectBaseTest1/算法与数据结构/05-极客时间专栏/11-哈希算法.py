# coding:utf-8

import hashlib

if __name__ == "__main__":
    st1="""
    dl31dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89
55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b
d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080a80dlec69821bcb6a8839396f9652b6ff72a70
    """

    st2="""
    dl31dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89
55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b
d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080280dlec69821bcb6a8839396f965ab6ff72a70
    """
    md5=hashlib.md5()
    md5.update(st1.encode('utf-8'))
    print(md5.hexdigest())

    md5.update(st2.encode('utf-8'))
    print(md5.hexdigest())
