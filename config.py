from dotenv import load_dotenv
import os 


load_dotenv()

MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_DB = os.environ['MYSQL_DB']
OLLAMA_MODEL_ID = os.environ['OLLAMA_MODEL_ID']
DB_CONN_STRING = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@127.0.0.1:3306/{MYSQL_DB}"

TORTOISE_ORM = {
    "connections": {
        "default": DB_CONN_STRING
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default"
        }
    }
}

CRIMES = [
    # Violent Crimes
    "Homicide",
    "Manslaughter",
    "Aggravated Assault",
    "Robbery",
    "Rape",
    "Sexual Assault",
    
    # Property Crimes
    "Burglary",
    "Larceny-Theft",
    "Motor Vehicle Theft",
    "Arson",
    
    # White-Collar Crimes
    "Fraud",
    "Embezzlement",
    "Identity Theft",
    "Money Laundering",
    "Insider Trading",
    "Bribery",
    
    # Drug & Alcohol Offenses
    "Drug Possession",
    "Drug Trafficking",
    "DUI (Driving Under the Influence)",
    "Public Intoxication",
    
    # Cybercrime
    "Hacking",
    "Phishing",
    "Cyberstalking",
    "Online Fraud",
    
    # Organized Crime
    "Racketeering",
    "Extortion",
    "Human Trafficking",
    "Illegal Gambling",
    
    # Weapons Offenses
    "Illegal Firearm Possession",
    "Unlawful Discharge of a Weapon",
    "Possession of a Firearm by a Felon",
    
    # Public Order Crimes
    "Disorderly Conduct",
    "Loitering",
    "Resisting Arrest",
    "Obstruction of Justice",
    
    # Immigration Offenses
    "Illegal Entry",
    "Visa Fraud",
    
    # Miscellaneous
    "Child Abuse",
    "Stalking",
    "Animal Cruelty",
    "Perjury",
    "Contempt of Court"
]

