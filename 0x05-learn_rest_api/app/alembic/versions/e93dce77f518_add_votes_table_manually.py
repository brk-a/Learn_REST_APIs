"""add 'votes' table manually

Revision ID: e93dce77f518
Revises: b1c1775e8af3
Create Date: 2023-02-27 14:27:54.235884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e93dce77f518'
down_revision = 'b1c1775e8af3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """add 'votes' table"""
    op.create_table('votes',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade() -> None:#
    """remove'votes' table"""
    op.drop_table('votes')
    pass
