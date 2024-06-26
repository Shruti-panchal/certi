"""empty message

Revision ID: 8332b7051dbf
Revises: 6f29403e170f
Create Date: 2023-07-20 17:11:44.234822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8332b7051dbf'
down_revision = '6f29403e170f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certificate', sa.Column('place', sa.Integer(), nullable=True))
    op.add_column('certificate', sa.Column('team_name', sa.String(length=128), nullable=True))
    op.drop_column('certificate', 'obtained_score')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certificate', sa.Column('obtained_score', sa.INTEGER(), nullable=True))
    op.drop_column('certificate', 'team_name')
    op.drop_column('certificate', 'place')
    # ### end Alembic commands ###
