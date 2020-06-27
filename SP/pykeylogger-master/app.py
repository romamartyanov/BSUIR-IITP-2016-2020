import keylogger
import time

now = time.time()
done = lambda: time.time() > now + 60
def print_keys(t, modifiers, keys): print "%.2f   %r   %r" % (t, keys, modifiers)

keylogger.log(done, print_keys)
