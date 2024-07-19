# Fun with circular imports in Python

This repository contains an example of how circular imports in Python can
result in really surprising behavior.

For example, there's a circular dependency here that works from one entrypoint,
but fails from a different entrypoint.

When running `mod.lower_bound` as an entrypoint, this actually works:

    $ python -m mod.lower_bound
    __main__: start
    mod.upper_bound: start
    mod.lower_bound: start
    mod.lower_bound: just imported <module 'mod.upper_bound' from '/home/jeremy/tmp/2024-07-19-pyhack-1/mod/upper_bound.py'>
    mod.lower_bound: just set pi_lower_bound=4
    mod.upper_bound: from foo.py: pi_lower_bound=4
    mod.upper_bound: just set pi_upper_bound=5
    __main__: just imported <module 'mod.upper_bound' from '/home/jeremy/tmp/2024-07-19-pyhack-1/mod/upper_bound.py'>
    __main__: just set pi_lower_bound=4

Whereas if you run `mod.upper_bound` as an entrypoint, you'll see a crash:

    $ python -m mod.upper_bound
    __main__: start
    mod.lower_bound: start
    mod.upper_bound: start
    Traceback (most recent call last):
      File "<frozen runpy>", line 198, in _run_module_as_main
      File "<frozen runpy>", line 88, in _run_code
      File "/home/jeremy/tmp/2024-07-19-pyhack-1/mod/upper_bound.py", line 2, in <module>
        from .lower_bound import pi_lower_bound
      File "/home/jeremy/tmp/2024-07-19-pyhack-1/mod/lower_bound.py", line 2, in <module>
        from . import upper_bound
      File "/home/jeremy/tmp/2024-07-19-pyhack-1/mod/upper_bound.py", line 2, in <module>
        from .lower_bound import pi_lower_bound
    ImportError: cannot import name 'pi_lower_bound' from partially initialized module 'mod.lower_bound' (most likely due to a circular import) (/home/jeremy/tmp/2024-07-19-pyhack-1/mod/lower_bound.py)
