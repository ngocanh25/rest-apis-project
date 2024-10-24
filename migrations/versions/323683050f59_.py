"""empty message

Revision ID: 323683050f59
Revises: 6c7f884ece8d
Create Date: 2024-10-21 22:36:55.788286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323683050f59'
down_revision = '6c7f884ece8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
