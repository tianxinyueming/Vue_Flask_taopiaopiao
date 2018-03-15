"""empty message

Revision ID: 6af4ac047995
Revises: 80fa74cb0571
Create Date: 2018-03-15 17:52:25.299630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6af4ac047995'
down_revision = '80fa74cb0571'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinemas',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('city', sa.String(length=32), nullable=True),
    sa.Column('district', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=1024), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Integer(), nullable=True),
    sa.Column('astrict', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinemas')
    # ### end Alembic commands ###
