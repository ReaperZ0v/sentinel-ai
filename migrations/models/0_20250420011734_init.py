from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `criminalrecord` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(120) NOT NULL,
    `last_name` VARCHAR(120) NOT NULL,
    `crime` JSON NOT NULL,
    `age` INT NOT NULL,
    `height` DOUBLE NOT NULL,
    `gender` VARCHAR(20) NOT NULL COMMENT 'MALE: male\nFEMALE: female',
    `ethnicity` VARCHAR(100) NOT NULL COMMENT 'EAST_ASIAN: East Asian\nSOUTH_ASIAN: South Asian\nSOUTHEAST_ASIAN: Southeast Asian\nCENTRAL_ASIAN: Central Asian\nBLACK_OR_AFRICAN_AMERICAN: Black or African American\nAFRO_CARIBBEAN: Afro-Caribbean\nWHITE_NON_HISPANIC: White (Non-Hispanic)\nWHITE_HISPANIC: White (Hispanic/Latino)\nLATINO_OR_HISPANIC: Latino or Hispanic\nMIDDLE_EASTERN: Middle Eastern\nNORTH_AFRICAN: North African\nNATIVE_AMERICAN: Native American\nALASKA_NATIVE: Alaska Native\nPACIFIC_ISLANDER: Pacific Islander\nNATIVE_HAWAIIAN: Native Hawaiian\nMIXED_RACE: Mixed Race / Multiracial\nJEWISH: Jewish\nROMANI: Romani\nOTHER: Other\nPREFER_NOT_TO_SAY: Prefer not to say',
    `hair_color` VARCHAR(100) NOT NULL COMMENT 'BLACK: Black\nDARK_BROWN: Dark Brown\nBROWN: Brown\nLIGHT_BROWN: Light Brown\nBLONDE: Blonde\nDIRTY_BLONDE: Dirty Blonde\nPLATINUM_BLONDE: Platinum Blonde\nRED: Red\nAUBURN: Auburn\nSTRAWBERRY_BLONDE: Strawberry Blonde\nGRAY: Gray\nWHITE: White\nBALD: Bald\nBLUE: Blue\nGREEN: Green\nPURPLE: Purple\nPINK: Pink\nORANGE: Orange\nSILVER: Silver\nTEAL: Teal\nRAINBOW: Rainbow\nOTHER: Other',
    `additional_description` LONGTEXT,
    `in_custody` BOOL,
    `has_past_convictions` BOOL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
