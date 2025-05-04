from faker import Faker
from models import HairColor, Gender, Status, Ethnicity, CriminalRecord
from config import * 
from tortoise import Tortoise
from aerich import Command
import random 
import asyncio 


fake = Faker()

async def gen_seed_data():
    for x in range(257):
        selected_gender = gender=random.choice(list(Gender)).value
        first_name = None 
        last_name = None 

        if selected_gender == "male":
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()

        else:
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()

        await CriminalRecord.create(
            first_name=first_name,
            last_name=last_name,
            crimes=",".join([
                random.choice(CRIMES) for x in range(random.randint(1, 5))
            ]),
            age=random.randint(18, 45),
            height=round(
                random.uniform(1.65, 1.95),
                2
            ),
            gender=selected_gender,
            ethnicity=random.choice(list(Ethnicity)).value,
            hair_color=random.choice(list(HairColor)).value,
            in_custody=random.choice([True, False]),
            additional_description="",
            has_past_convictions=random.choice([True, False])
        )

async def main():
    await Tortoise.init(
        config=TORTOISE_ORM,
    )

    command = Command(tortoise_config=TORTOISE_ORM, app="models")
    await command.init()
    await command.upgrade()

    await gen_seed_data()

asyncio.run(main())
