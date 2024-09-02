"""deleted session table + changed review table

Revision ID: 422806539a37
Revises: 0b3cc7661816
Create Date: 2024-09-02 19:36:38.379440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '422806539a37'
down_revision: Union[str, None] = '0b3cc7661816'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meeting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(), nullable=False),
    sa.Column('mentor_login', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=350), nullable=False),
    sa.Column('start_time', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.CheckConstraint("role = 'Mentor' OR role = 'User'"),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.Column('specialization', sa.String(length=40), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('mentor_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=False),
    sa.CheckConstraint('rating in (1, 2, 3, 4, 5)'),
    sa.ForeignKeyConstraint(['mentor_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('profile')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('meeting')
    # ### end Alembic commands ###
