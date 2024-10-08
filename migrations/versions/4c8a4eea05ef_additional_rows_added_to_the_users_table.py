"""Additional rows added to the users table.

Revision ID: 4c8a4eea05ef
Revises: 433e8d5ce980
Create Date: 2024-07-14 12:08:23.854254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c8a4eea05ef'
down_revision: Union[str, None] = '433e8d5ce980'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('login', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('role', sa.String(length=10), nullable=True))
    op.drop_index('ix_users_email', table_name='user')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_index('ix_users_email', 'user', ['email'], unique=True)
    op.drop_column('user', 'role')
    op.drop_column('user', 'login')
    # ### end Alembic commands ###
