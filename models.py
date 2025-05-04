from tortoise.models import Model
from tortoise import fields
from enum import Enum

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class Status(str, Enum):
    DECEASED = "Deceased"
    ALIVE = "Alive"


class Ethnicity(str, Enum):
    EAST_ASIAN = "East Asian"
    SOUTH_ASIAN = "South Asian"
    SOUTHEAST_ASIAN = "Southeast Asian"
    CENTRAL_ASIAN = "Central Asian"
    BLACK_OR_AFRICAN_AMERICAN = "Black or African American"
    AFRO_CARIBBEAN = "Afro-Caribbean"
    WHITE_NON_HISPANIC = "White (Non-Hispanic)"
    WHITE_HISPANIC = "White (Hispanic/Latino)"
    LATINO_OR_HISPANIC = "Latino or Hispanic"
    MIDDLE_EASTERN = "Middle Eastern"
    NORTH_AFRICAN = "North African"
    NATIVE_AMERICAN = "Native American"
    ALASKA_NATIVE = "Alaska Native"
    PACIFIC_ISLANDER = "Pacific Islander"
    NATIVE_HAWAIIAN = "Native Hawaiian"
    MIXED_RACE = "Mixed Race / Multiracial"
    JEWISH = "Jewish"
    ROMANI = "Romani"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class HairColor(str, Enum):
    BLACK = "Black"
    DARK_BROWN = "Dark Brown"
    BROWN = "Brown"
    LIGHT_BROWN = "Light Brown"
    BLONDE = "Blonde"
    DIRTY_BLONDE = "Dirty Blonde"
    PLATINUM_BLONDE = "Platinum Blonde"
    RED = "Red"
    AUBURN = "Auburn"
    STRAWBERRY_BLONDE = "Strawberry Blonde"
    GRAY = "Gray"
    WHITE = "White"
    BALD = "Bald"
    
    # Dyed / Fantasy Colors
    BLUE = "Blue"
    GREEN = "Green"
    PURPLE = "Purple"
    PINK = "Pink"
    ORANGE = "Orange"
    SILVER = "Silver"
    TEAL = "Teal"
    RAINBOW = "Rainbow"
    OTHER = "Other"


class CriminalRecord(Model):
    id = fields.BigIntField(pk=True)
    first_name = fields.CharField(max_length=120)
    last_name = fields.CharField(max_length=120)
    crimes = fields.TextField()
    age = fields.IntField()
    height = fields.FloatField()
    gender = fields.CharEnumField(Gender, max_length=20)
    ethnicity = fields.CharEnumField(Ethnicity, max_length=100)
    hair_color = fields.CharEnumField(HairColor, max_length=100)
    additional_description = fields.TextField(null=True)
    in_custody = fields.BooleanField(null=True)
    has_past_convictions = fields.BooleanField(null=True)



