import pyjudemq
import time

def handle_auth(args):
    print(args)
    return "OK"

def main():
    lmq = pyjudemq.JudeMQ()
    lmq.listen_plain("ipc:///tmp/lmq.sock")
    lmq.add_anonymous_category("llarp")
    lmq.add_request_command("llarp", "auth", handle_auth)
    lmq.start()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
