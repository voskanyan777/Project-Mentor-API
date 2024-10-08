"""create meeting table

Revision ID: 195a6974178c
Revises: 06d2fb98902a
Create Date: 2024-08-21 19:14:17.078920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '195a6974178c'
down_revision: Union[str, None] = '06d2fb98902a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meeting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(), nullable=False),
    sa.Column('mentor_login', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=350), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meeting')
    # ### end Alembic commands ###
