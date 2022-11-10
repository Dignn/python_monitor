# Project description
# python_monitor Package
## python_monitor package will help you to monitor python process

# Installation
## Install python_monitor package using command

`pip install python_monitor`

# Examples
```
    import time

    from python_monitor import run_http_server
    
    
    def do_something():
        time.sleep(20)


    while 1:
        run_http_server(8000)
        do_something()
        time.sleep(10)
```

