from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `meetings` ADD `location` VARCHAR(255) NOT NULL  DEFAULT '';
        ALTER TABLE `meetings` ADD `start_date` DATE;
        ALTER TABLE `meetings` ADD `title` VARCHAR(255) NOT NULL  DEFAULT '';
        ALTER TABLE `meetings` ADD `end_date` DATE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `meetings` DROP COLUMN `location`;
        ALTER TABLE `meetings` DROP COLUMN `start_date`;
        ALTER TABLE `meetings` DROP COLUMN `title`;
        ALTER TABLE `meetings` DROP COLUMN `end_date`;"""
