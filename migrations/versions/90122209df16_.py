"""empty message

Revision ID: 90122209df16
Revises: e65dad6031c1
Create Date: 2023-07-20 14:24:09.699152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90122209df16'
down_revision = 'e65dad6031c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certificate', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'certificate', 'users', ['user_id'], ['id'])
    op.drop_column('certificate', 'place')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certificate', sa.Column('place', sa.VARCHAR(length=128), nullable=True))
    op.drop_constraint(None, 'certificate', type_='foreignkey')
    op.drop_column('certificate', 'user_id')
    # ### end Alembic commands ###