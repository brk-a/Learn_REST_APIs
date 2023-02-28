"""add the rest of the columns of 'posts' table

Revision ID: b1c1775e8af3
Revises: a2f89f81278d
Create Date: 2023-02-27 14:12:50.616240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1c1775e8af3'
down_revision = 'a2f89f81278d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """add the rest of the columns of `posts` table"""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    """remove the rest of the columns of `posts` table"""
    op.drop_column(table_name='posts', column_name='published')
    op.drop_column('posts', 'created_at')
    pass
