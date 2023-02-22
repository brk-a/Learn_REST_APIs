"""add fkey for `posts` and `users`

Revision ID: a2f89f81278d
Revises: dd7260604f90
Create Date: 2023-02-21 11:02:46.709505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f89f81278d'
down_revision = 'dd7260604f90'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """add fkey constraint"""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    """remove fkey constraint"""
    op.drop_constraint("posts_users_fk", table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
