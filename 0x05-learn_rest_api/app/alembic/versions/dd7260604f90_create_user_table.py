"""create user table

Revision ID: dd7260604f90
Revises: a145379f5261
Create Date: 2023-02-21 10:40:36.429275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd7260604f90'
down_revision = 'a145379f5261'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """create user table"""
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
        server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    """remove user table"""
    op.drop_table('users')
    pass
