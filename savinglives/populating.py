import os

def populate():
  add_operation("Send text","send")
  add_operation("View texts received","texts")
  add_operation("Call them","call")
  add_operation("Database","data")


def add_operation(name,url):
    o = Operation.objects.get_or_create(name=name,url=url)[0]
    return o

# Start execution here!
if __name__ == '__main__':
    print "Starting main population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'savinglives.settings')
    from main.models import Operation
    populate()
