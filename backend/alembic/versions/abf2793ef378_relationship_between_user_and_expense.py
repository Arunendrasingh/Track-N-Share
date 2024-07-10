"""relationship between user and expense

Revision ID: abf2793ef378
Revises: da7c4090d32d
Create Date: 2024-07-10 19:03:01.175204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abf2793ef378'
down_revision: Union[str, None] = 'da7c4090d32d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expenses', sa.Column('is_updated', sa.Boolean(), nullable=True))
    op.add_column('expenses', sa.Column('edited_by', sa.String(), nullable=True))
    op.create_foreign_key(None, 'expenses', 'users', ['paid_by_id'], ['id'])
    op.drop_column('expenses', 'paid_by')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expenses', sa.Column('paid_by', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'expenses', type_='foreignkey')
    op.drop_column('expenses', 'edited_by')
    op.drop_column('expenses', 'is_updated')
    # ### end Alembic commands ###
