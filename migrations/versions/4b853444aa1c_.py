"""empty message

Revision ID: 4b853444aa1c
Revises: 804418355dc3
Create Date: 2022-11-12 15:32:15.273507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b853444aa1c'
down_revision = '804418355dc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assessments', sa.Column('release_day', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assessments', 'release_day')
    # ### end Alembic commands ###
