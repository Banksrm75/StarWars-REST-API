"""empty message

Revision ID: 3217b89e6e31
Revises: bc3356c44a8f
Create Date: 2024-12-04 02:54:19.087403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3217b89e6e31'
down_revision = 'bc3356c44a8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user__favorites', schema=None) as batch_op:
        batch_op.alter_column('character_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('planet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('vehicle_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user__favorites', schema=None) as batch_op:
        batch_op.alter_column('vehicle_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('planet_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('character_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
