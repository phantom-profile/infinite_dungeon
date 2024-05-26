import launcher.initialize  # noqa
from dungeons.models import Item

if __name__ == '__main__':
    print(Item.objects.create(name="aaa"))
