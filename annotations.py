import traceback

def safe_run(func):
    def func_wrapper(*args, **kwargs):
        try:
           return func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return None

    return func_wrapper