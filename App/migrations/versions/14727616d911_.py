"""empty message

Revision ID: 14727616d911
Revises: dbba2e8654b0
Create Date: 2022-06-02 21:29:27.269609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14727616d911'
down_revision = 'dbba2e8654b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('nickname', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.String(length=100), nullable=True),
    sa.Column('date_updated', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###