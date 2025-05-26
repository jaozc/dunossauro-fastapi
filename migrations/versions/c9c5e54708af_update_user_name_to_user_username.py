"""update user.name to user.username

Revision ID: c9c5e54708af
Revises: 84f7f7b91fdd
Create Date: 2025-05-26 17:25:51.064465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9c5e54708af'
down_revision: Union[str, None] = '84f7f7b91fdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
