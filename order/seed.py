# run from shell
from django_seed import Seed
from order.models import Restaurants, RestaurantMenuItem

seeder = Seed.seeder()


seeder.add_entity(RestaurantMenuItem, 40)

inserted_pks = seeder.execute()
