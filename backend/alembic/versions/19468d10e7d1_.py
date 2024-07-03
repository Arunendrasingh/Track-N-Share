"""empty message

Revision ID: 19468d10e7d1
Revises: aa73dcd15fa6
Create Date: 2024-07-03 20:55:00.462478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19468d10e7d1'
down_revision: Union[str, None] = 'aa73dcd15fa6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
