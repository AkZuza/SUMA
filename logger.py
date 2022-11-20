log_file = None

def log(text):
    from datetime import datetime
    when = '[ ' + datetime.today().strftime('%Y-%m-%d | %H:%M:%S') + ' ]'
    log_file.write(when + ' ' + text + '\n')

def init():
    global log_file
    log_file = open("log.txt", "a")
    log_file.flush()

def close():
    log_file.close()

