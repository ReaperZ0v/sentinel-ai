from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `criminalrecord` ADD `crimes` LONGTEXT NOT NULL;
        ALTER TABLE `criminalrecord` DROP COLUMN `crime`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `criminalrecord` ADD `crime` JSON NOT NULL;
        ALTER TABLE `criminalrecord` DROP COLUMN `crimes`;"""
