"""User model has been changed

Revision ID: ceab27919ec0
Revises: 06d2fb98902a
Create Date: 2024-08-09 21:03:15.782747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceab27919ec0'
down_revision: Union[str, None] = '06d2fb98902a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
