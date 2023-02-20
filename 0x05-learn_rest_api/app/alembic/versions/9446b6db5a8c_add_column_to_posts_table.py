"""add column to posts table

Revision ID: 9446b6db5a8c
Revises: c305292504c7
Create Date: 2023-02-19 17:17:26.403763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9446b6db5a8c'
down_revision = 'c305292504c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """add column to `posts` table"""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """downgrade to previous version"""
    op.drop_column('posts', 'content')
    pass
