"""Initial migration.

Revision ID: 22d0383ff8f4
Revises: 
Create Date: 2024-06-06 23:59:18.025757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22d0383ff8f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone_no', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connected_items',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('reporter_id', sa.Integer(), nullable=True),
    sa.Column('date_connected', sa.DateTime(), nullable=True),
    sa.Column('location_connected', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['reporter_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('items_found',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_found', sa.DateTime(), nullable=True),
    sa.Column('location_found', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(length=64000), nullable=True),
    sa.Column('filename', sa.String(length=50), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items_found')
    op.drop_table('connected_items')
    op.drop_table('users')
    # ### end Alembic commands ###
