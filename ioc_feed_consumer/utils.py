from .models import Ioc
from django.db.utils import IntegrityError


# checks if an ioc is already added to the database!
def is_added(ioc):
    return Ioc.objects.filter(ioc=ioc['ioc']).exists()

# adds an ioc to the database
def add(ioc):
    try:
        # transform the singular source into an array of sources!
        Ioc.objects.create(
            ioc=ioc["ioc"],
            type=ioc["type"],
            source=ioc["source"]
        )
        return True
    except IntegrityError as e:
        print(f"Ioc: {ioc['ioc']} already exists!")
        return False

# updates the ioc!
# i.e if an ioc is in 2 or more feeds!
def update(ioc):
    try:
        pass
    except DoesNotExistError as e:
        pass
    # Ioc.objects.filter(ioc=ioc["ioc"]).update()
    pass