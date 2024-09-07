"""create todos table

Revision ID: 395e67adbf6b
Revises: 
Create Date: 2024-09-06 20:33:33.100772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '395e67adbf6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)

def downgrade():
    op.execute("drop table todos;")
